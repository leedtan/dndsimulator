from collections import defaultdict


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
    spell_slots = [0 for _ in range(9)]]

class CharacterProgression:
    def __init__(starting_stats, classes, weapon, armor, feats, hasshield=False):
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
        if self.armor in ["scalemail"]:
            self.ac = 16
        if self.hasshield:
            self.ac += 2

    def sample_at_level(level):
        for lvl in range(level):
            self.apply_level(lvl)
        self.modifiers = calc_modifiers(self.stats)
        self.max_hps += level * self.modifiers["con"]
        self.spell_slots = self.max_spell_slots = calc_spell_slots(self.class_levels)
        self.ac = self.calc_ac()

    def apply_feats(feats):
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
