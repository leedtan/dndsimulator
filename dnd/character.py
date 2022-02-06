import copy
import math
import random

from attacks import MultiAttack, RangedMultiAttack
from dice import Dice
from strategies import check_death, get_closest_enemy, get_order, move_path
from table_utils import viz_table  # noqa
from utils import check_table, move_to_enemy  # noqa

d20 = Dice(20)

flag = 0
PLAN_NORMAL = 0
PLAN_CHANGED = 1
PLAN_DEAD = -1


class Character:
    def __init__(
        self,
        hp,
        ac,
        attacks,
        stats,
        name,
        level,
        spells=[],
        spell_slots=[],
        spellcasting_modifier=0,
        imposes_disadv=False,
        has_adv=False,
        resistance=None,
        once_per_long_rest=[],
        long_rest_uses=[],
        party=True,
        PAM=False,
        reach=1,
        maxreach=None,  # noqa
        charge_forward=True,
        color="",
        *args,
        **kwargs
    ):
        self.color = color
        self.party = party
        self.imposes_disadv, self.has_adv = imposes_disadv, has_adv
        self._hp = hp
        self.max_hp = hp
        self.ac = ac
        self.spells = spells
        self.spell_slots = spell_slots
        self.max_spell_slots = copy.copy(spell_slots)
        if not isinstance(attacks, list):
            attacks = [attacks]
        if not isinstance(attacks[0], MultiAttack):
            attacks = [MultiAttack(attack) for attack in attacks]
        for attack in attacks:
            if attack.max_distance is None:
                attack.max_distance = reach
                for atk in attack.attacks:
                    atk.max_distance = reach
        self.attacks = attacks
        if PAM is not False:
            if not isinstance(PAM, list):
                PAM = [PAM]
            if not isinstance(PAM[0], MultiAttack):
                PAM = [MultiAttack(attack) for attack in PAM]
            for attack in PAM:
                if attack.max_distance is None:
                    attack.max_distance = reach
                    for atk in attack.attacks:
                        atk.max_distance = reach

        self.PAM = PAM
        self.stats = stats
        self.name = name
        self.spellcasting_modifier = spellcasting_modifier
        self.resistance = resistance
        self.once_per_long_rest = once_per_long_rest
        self.long_rest_uses = long_rest_uses
        self.long_rest_uses_max = copy.copy(long_rest_uses)
        self.reach = reach
        self.movespeed = 6
        self.charge_forward = charge_forward
        self.has_react = True
        self.has_action = True
        self.has_bonus = True
        self.has_obj_interract = True
        self.level = self.max_hit_dice = self.hit_dice = level
        self.max_reach = max([atk.max_distance for atk in self.attacks])
        # if maxreach is None:
        #     if attacks[0].max_distance is not None:
        #         maxreach = attacks[0].max_distance
        # self.maxreach = maxreach

    def __repr__(self):
        return self.name

    def roll_init(self):
        return self.stats["dex"] + d20.roll() + self.stats["dex"] / 100.0

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        if hp > self._hp or not self.resistance == "all":
            self._hp = hp
        else:
            self._hp = (self._hp + hp) // 2

    def reset_turn(self):
        self.has_react = True
        self.has_action = True
        self.has_bonus = True
        self.has_obj_interract = True
        [attack.reset() for attack in self.attacks]
        if self.PAM:
            [attack.reset() for attack in self.PAM]

    def shortrest(self):
        if self.hp > 0:
            while (self.hp < (self.max_hp - 3)) and (self.hit_dice > 0):
                self.roll_hit_dice()

    def roll_hit_dice(self):
        self.hp = self.hp + 3 + random.randint(1, 8)
        self.hit_dice -= 1
        self.hp = min(self.hp, self.max_hp)

    def longrest(self):
        if self.hp > 0:
            self.hp = self.max_hp
        self.hit_dice = self.hit_dice + math.ceil(self.max_hit_dice / 2)
        self.hit_dice = min(self.hit_dice, self.max_hit_dice)

    def make_attack(
        self, attacks, atk_distance, closest_enemy, table, state, check_death
    ):
        attack = attacks[0]
        for atk in attacks:
            if atk.priority(atk_distance):
                attack = atk
                break
        for atk in attack.attacks:
            disadvantage = closest_enemy.imposes_disadv
            if atk_distance <= 1 and isinstance(attack, RangedMultiAttack):
                disadvantage = 1
            atk.roll_hit(
                enemy=closest_enemy,
                advantage=self.has_adv,
                disadvantage=disadvantage,
                caster=self,
                table=table,
            )
            end_val = check_death(state, table)
            if end_val >= 0:
                return end_val
        return -1

    def charge(self, move_remaining, enemies, table, state, dbg=False):
        # print(self)
        # print(state["pcs"][0], state["pcs"][0].coor)
        # print(state["npcs"][0], state["npcs"][0].coor)
        if dbg:
            breakpoint()
        stop_move = False
        i = 0
        while move_remaining > 0 and not stop_move:
            if i > 3:
                # stop_move = True
                a = 2
            i += 1
            closest_enemy = get_closest_enemy(enemies, self.coor)
            atk_distance = max(
                abs(closest_enemy.coor[0] - self.coor[0]),
                abs(closest_enemy.coor[1] - self.coor[1]),
            )
            if atk_distance <= self.reach:
                stop_move = True
                break
            final_destination, reverse_path, path_scores = move_to_enemy(
                self, closest_enemy, table, move_remaining=move_remaining
            )
            # print(i)
            if i > 4:
                breakpoint()
                print("wtf")
            current = final_destination
            order = get_order(current, reverse_path, self)
            moves_used, enemy_moved_me = move_path(
                table, order, self, enemies, move_remaining, state
            )
            if enemy_moved_me == PLAN_DEAD:
                return
            table[self.coor] = self
            move_remaining -= moves_used
            if enemy_moved_me == PLAN_CHANGED:
                continue

            if i > 10:
                breakpoint()
                a = 2  # noqa
            closest_enemy = get_closest_enemy(enemies, self.coor)
            atk_distance = max(
                abs(closest_enemy.coor[0] - self.coor[0]),
                abs(closest_enemy.coor[1] - self.coor[1]),
            )
            if atk_distance <= self.reach:
                stop_move = True
                break

    def strategy(self, npcs, pcs, table, state, dbg=False):
        if self.party:
            enemies = npcs
        else:
            enemies = pcs
        move_remaining = self.movespeed
        if self.charge_forward:
            self.charge(move_remaining, enemies, table, state, dbg=dbg)

        closest_enemy = get_closest_enemy(enemies, self.coor)
        atk_distance = max(
            abs(closest_enemy.coor[0] - self.coor[0]),
            abs(closest_enemy.coor[1] - self.coor[1]),
        )
        if atk_distance <= self.max_reach:
            end_val = self.make_attack(
                self.attacks, atk_distance, closest_enemy, table, state, check_death
            )
            if end_val >= 0:
                return end_val
