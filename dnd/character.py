import copy
import itertools
import random

import numpy as np
from dice import Dice

from attacks import Attack, Damage

d20 = Dice(20)


class Character:
    def __init__(
        self,
        hp,
        ac,
        attacks,
        stats,
        name,
        spells=[],
        spell_slots=[],
        spellcasting_modifier=0,
        imposes_disadv=False,
        has_adv=False,
        resistance=None,
        once_per_long_rest=[],
        long_rest_uses=[],
        party=True,
    ):
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
        self.attacks = attacks
        self.stats = stats
        self.name = name
        self.spellcasting_modifier = spellcasting_modifier
        self.resistance = resistance
        self.once_per_long_rest = once_per_long_rest
        self.long_rest_uses = long_rest_uses
        self.long_rest_uses_max = copy.copy(long_rest_uses)
        self.reach = 1
        self.movespeed = 6
        self.charge = True

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
