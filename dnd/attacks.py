import copy
import itertools
import random

import numpy as np

from dice import Dice

d20 = Dice(20)


class Damage:
    def __init__(self, rolls, flat_bonus):
        self.rolls = rolls
        self.flat_bonus = flat_bonus

    def roll(self):
        rolls = sum([random.randint(1, roll) for roll in self.rolls])
        return rolls + self.flat_bonus


class Attack:
    def __init__(self, to_hit, damage, on_hit=[]):
        self.to_hit = to_hit
        self.damage = damage
        self.on_hit = on_hit

    #     enemy.hp -= damage

    def roll_hit(
        self, advantage=False, disadvantage=False, enemy=None, caster=None, table=None
    ):
        if advantage and disadvantage:
            advantage = disadvantage = False
        roll1 = self.to_hit + d20.roll()
        roll2 = self.to_hit + d20.roll()
        if advantage:
            hits = max(roll1, roll2) > enemy.ac
        elif disadvantage:
            hits = max(roll1, roll2) > enemy.ac
        else:
            hits = roll1 > enemy.ac
        if hits:
            enemy.hp -= self.damage.roll()
        if hits:
            for effect in self.on_hit:
                effect.apply(enemy, caster, table)
        return hits

