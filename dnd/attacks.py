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
    def __init__(self, to_hit, damage):
        self.to_hit = to_hit
        self.damage = damage

    def apply_damage(self, to_hit, damage, enemy):
        if to_hit >= enemy.ac:
            enemy.hp -= damage

    def roll_hit(self, advantage=False, disadvantage=False, enemy=None):
        if advantage and disadvantage:
            advantage = disadvantage = False
        roll1 = self.to_hit + d20.roll()
        if advantage:
            roll2 = self.to_hit + d20.roll()
            self.apply_damage(max(roll1, roll2), self.damage.roll(), enemy)
        elif disadvantage:
            roll2 = self.to_hit + d20.roll()
            self.apply_damage(min(roll1, roll2), self.damage.roll(), enemy)
        else:
            self.apply_damage(roll1, self.damage.roll(), enemy)

