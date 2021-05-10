import random

from dice import Dice

d20 = Dice(20)


class Damage:
    def __init__(self, rolls, flat_bonus):
        self.rolls = rolls
        self.flat_bonus = flat_bonus

    def roll(self, critical=False):
        rolls = sum([random.randint(1, roll) for roll in self.rolls])
        if critical:
            rolls += sum([random.randint(1, roll) for roll in self.rolls])
        return rolls + self.flat_bonus


class AttackBase:
    def priority(self, distance):
        return True


class MultiAttack(AttackBase):
    def __init__(self, attacks, max_distance=None, triple_adv=False, on_hit=[]):
        self.used = 1
        if not isinstance(attacks, list):
            attacks = [attacks]
        for attack in attacks:
            if max_distance is not None:
                attack.max_distance = max_distance
            if triple_adv:
                attack.triple_adv = True
            if len(on_hit) > 0:
                attack.on_hit = attack.on_hit + on_hit
        self.attacks = attacks
        self.multi = True
        self.max_distance = attacks[0].max_distance
        self.triple_adv = attacks[0].triple_adv
        self.on_hit = attacks[0].on_hit
        self.used = [1 for _ in self.attacks]

    def reset(self):
        self.using = False
        self.used = [0 for _ in self.attacks]


class Attack(AttackBase):
    def __init__(self, to_hit, damage, on_hit=[], triple_adv=False, max_distance=None):
        self.to_hit = to_hit
        self.damage = damage
        self.on_hit = on_hit
        self.triple_adv = triple_adv
        self.using = False
        self.multi = False
        self.max_distance = max_distance

    def reset(self):
        self.using = False
        self.used = 0

    def roll_hit(self, advantage=False, disadvantage=False, enemy=None, caster=None, table=None):
        self.used = 1
        if advantage and disadvantage:
            advantage = disadvantage = False
        roll1 = self.to_hit + d20.roll()
        roll2 = self.to_hit + d20.roll()
        if advantage:
            if self.triple_adv:
                roll3 = self.to_hit + d20.roll()
                options = [roll1, roll2, roll3]
            else:
                options = [roll1, roll2]
            to_hit = max(options)
        elif disadvantage:
            to_hit = min(roll1, roll2)
        else:
            to_hit = roll1
        if to_hit == 20:
            hits = True
            enemy.hp -= self.damage.roll(critical=True)
        else:
            hits = to_hit >= enemy.ac
            if hits:
                enemy.hp -= self.damage.roll()
        if hits:
            for effect in self.on_hit:
                effect.apply(enemy, caster, table)
        return hits


class RangedAttack(Attack):
    def priority(self, distance):
        return distance > 1


class RangedMultiAttack(MultiAttack):
    def priority(self, distance):
        return distance > 1


class MeleeAttack(Attack):
    def priority(self, distance):
        return distance <= self.max_distance


class MeleeMultiAttack(MultiAttack):
    def priority(self, distance):
        return distance <= self.max_distance
