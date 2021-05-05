import copy
import itertools
import random

import numpy as np

from attacks import Attack, Damage
from character import Character


class HealingWord:
    def __init__(self):
        self.time = "bonus"
        self.type = "heal"
        pass

    def cast(self, targets, ava_spell_slots, spellcasting_modifier, *args, **kwargs):
        spell_level = 1 + max([i for i, v in enumerate(ava_spell_slots) if v > 0])
        amount_healed = (
            sum([d4.roll() for _ in range(spell_level)]) + spellcasting_modifier
        )
        life_cleric = True
        if life_cleric:
            amount_healed += 2 + spell_level
        targets.hp += amount_healed
        return spell_level


class MagicMissile:
    def __init__(self):
        self.time = "action"
        self.type = "attack"
        pass

    def cast(self, enemies, ava_spell_slots, *args, **kwargs):
        spell_level = 1 + max([i for i, v in enumerate(ava_spell_slots) if v > 0])
        missle = 2 + spell_level
        if not isinstance(enemies, list):
            enemies = [enemies] * missle
        for enemy in enemies:
            damage = d4.roll() + 1
            enemy.hp -= damage
        return spell_level
