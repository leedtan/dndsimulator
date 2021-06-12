import os.path
import sys
from collections import defaultdict

file = os.getcwd()
# sys.path.append(
#     os.path.abspath(os.path.join(os.path.dirname(file), os.path.pardir)))
sys.path.append(os.path.join("..", os.getcwd(), ".."))
from armor import armor as armorsmith  # noqa
from weapons import weapons as weaponsmith  # noqa


class ASI:
    def __init__(self, stats):
        self.stats = stats


class Feat:
    def __init__(self, feats):
        self.feats = feats


class Spell:
    def __init__(self, spellname):
        self.spellname = spellname


def calc_modifiers(stats):
    return {k: (v - 10) // 2 for k, v in stats.items()}


def calc_spell_slots(class_levels):
    spell_level = 0
    for clss, level in class_levels.items():
        if clss in ["wiz", "sor", "clr", "brd"]:
            spell_level += level
        if clss in ["pal", "rng"]:
            spell_level += level // 2

    spell_slots = [0 for _ in range(9)]
    spell_slots[0] = min((spell_level >= 1) * (1 + spell_level), 4)
    spell_slots[1] = min((spell_level >= 3) * (spell_level - 1), 3)
    spell_slots[2] = min((spell_level >= 5) * (spell_level - 3), 3)
    spell_slots[3] = min((spell_level >= 7) * (spell_level - 6), 3)
    spell_slots[4] = min((spell_level >= 9) * (spell_level - 8), 2) + (
        spell_level >= 18
    )
    spell_slots[5] = (spell_level >= 11) + (spell_level >= 19)
    spell_slots[6] = (spell_level >= 13) + (spell_level >= 20)
    spell_slots[8] = spell_level >= 15
    spell_slots[9] = spell_level >= 17
    return spell_slots


def calc_pact_slots(class_levels):
    spell_level = class_levels["warlock"]
    spell_slots = [0 for _ in range(5)]
    if spell_level > 0:
        pact_level = min((spell_level + 1) // 2, 5)
        num_spell_slots = (
            1 + (spell_level >= 2) + (spell_level >= 11) + (spell_level >= 17)
        )
        spell_slots[pact_level] = num_spell_slots
    return spell_slots


class CharacterProgression:
    def __init__(self, starting_stats, classes, weapon, armor, feats, hasshield=False):
        self.attacks = 1
        self.stats = self.starting_stats = starting_stats
        self.classes = classes
        self.weapon = weapon
        self.armor = armor
        self.feats = feats
        self.hasshield = hasshield
        self.class_levels = {}
        self.attackmodifiers = []
        self.mirrorimages = []
        self.max_hps = 0
        self.binary_feats = defaultdict(lambda: 0)

    def calc_ac(self):
        self.armor_type = armorsmith[self.armor]
        self.armor_class = self.armor_type["armor_class"]
        self.base_armor = self.armor_class["base"]
        self.dex_mod_ac = self.armor_class["dex_mod"] * self.modifiers["dex"]
        if self.armor_class["dex_mod_max"]:
            self.dex_mod_ac = min(
                self.armor_class["dex_mod_max"], self.modifiers["dex"]
            )
        self.ac = self.base_armor + self.dex_mod_ac
        if self.hasshield:
            self.ac += 2

    def sample_at_level(self, level):
        for lvl in range(level):
            self.apply_level(lvl)
        self.modifiers = calc_modifiers(self.stats)
        self.max_hps += level * self.modifiers["con"]
        self.spell_slots = self.max_spell_slots = calc_spell_slots(self.class_levels)
        self.pact_slots = self.max_pact_slots = calc_pact_slots(self.class_levels)
        self.ac = self.calc_ac()

    def apply_feats(self, feats):
        for feat in self.feats:
            if isinstance(feat, ASI):
                for stat in feat.stats:
                    self.stats[stat] += 1
            elif feat == "pam":
                self.binary_feats["pam"] == 1
            else:
                raise ValueError(feat)

    def apply_level(self, level):
        self.apply_class(self.classes[level])
        self.apply_feats(self.feats[level])

    def apply_class(self, clss):
        if clss in self.class_levels.keys():
            self.class_levels[clss] = 0
        self.class_levels[clss] += 1
        self.levelup(clss, self.class_levels[clss])

    def levelup(self, clss, level):
        if clss == "pal":
            self.max_hps += 6
            if level == 2:
                self.binary_feats["smite"] = 1
            if level == 5:
                self.attacks = 2
            if level == 11:
                self.attackmodifiers.append("improvedsmite")

        elif clss == "warlock":
            self.max_hps += 5
