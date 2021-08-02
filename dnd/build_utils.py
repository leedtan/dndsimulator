from collections import defaultdict

from armor import armor as armorsmith  # noqa
from attacks import Attack, Damage, MeleeMultiAttack, RangedMultiAttack  # noqa
from character import Character
from effects import BlastBack
from weapons import weapons as weaponsmith  # noqa

# file = os.getcwd()
# sys.path.append(os.path.join("..", os.getcwd(), ".."))


def get_proficiency(level):
    return ((level - 1) // 4) + 2


class CharacterModifier:
    def __init__(self, fcn):
        self.fcn = fcn

    def apply(self, character):
        self.fcn(character)


class ASI:
    def __init__(self, stats):
        self.stats = stats


class Feat:
    def __init__(self, feats):
        self.individual_feats = feats


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
    spell_slots[4] = min((spell_level >= 9) * (spell_level - 8), 2) + (spell_level >= 18)
    spell_slots[5] = (spell_level >= 11) + (spell_level >= 19)
    spell_slots[6] = (spell_level >= 13) + (spell_level >= 20)
    spell_slots[7] = spell_level >= 15
    spell_slots[8] = spell_level >= 17
    return spell_slots


def calc_pact_slots(class_levels):
    spell_level = class_levels["warlock"]
    spell_slots = [0 for _ in range(5)]
    if spell_level > 0:
        pact_level = min((spell_level + 1) // 2, 5)
        num_spell_slots = 1 + (spell_level >= 2) + (spell_level >= 11) + (spell_level >= 17)
        spell_slots[pact_level] = num_spell_slots
    return spell_slots


class CharacterProgression:
    def __init__(
        self,
        starting_stats,
        classes,
        weapon,
        armor,
        meleevsrange,
        feats,
        attacks_use=[],
        hasshield=False,
        name="",
    ):
        self.attacks = 1
        self.stats = self.starting_stats = starting_stats
        self.classes = classes
        self.weapon = weapon
        self.armor = armor
        self.feats = feats
        self.hasshield = hasshield
        self.class_levels = defaultdict(lambda: 0)
        self.attackmodifiers = []
        self.mirrorimages = []
        self.max_hps = 0
        self.meleevsrange = meleevsrange
        self.binary_feats = defaultdict(lambda: 0)
        self.attacks_use = attacks_use
        self.name = name
        self.spells = []

    def calc_ac(self):
        self.armor_type = armorsmith[self.armor]
        self.armor_class = self.armor_type["armor_class"]
        self.base_armor = self.armor_class["base"]
        if "dex_mod_max" in self.armor_class.keys():
            self.dex_mod_ac = min(2, self.modifiers["dex"])
        elif "dex_mod" in self.armor_class.keys():
            self.dex_mod_ac = self.modifiers["dex"]
        else:
            self.dex_mod_ac = 0
        self.ac = self.base_armor + self.dex_mod_ac
        if self.hasshield:
            self.ac += 2

    def calc_melee_attack(self):
        self.weapon_type = weaponsmith[self.weapon]
        self.weapon_properties = self.weapon_type["properties"]
        self.range = 1 + ("reach" in self.weapon_properties)
        self.pam = self.binary_feats["pam"] and (
            self.weapon in ["glaive", "halberd", "quarterstaff", "spear"]
        )
        if len(self.attacks_use) == 0:
            self.attacks_use += ["str"] + (["dex"] if "finesse" in self.weapon_properties else [])
        self.damage_bonus = max([self.modifiers[stat] for stat in self.attacks_use])
        self.attackbonus = self.proficiency + self.damage_bonus
        self.damage = self.weapon_type["damage"]

    def sample_at_level(self, level, name=""):
        name = self.name + name
        self.character_level = level
        for lvl in range(level):
            self.apply_level(lvl)
        self.modifiers = calc_modifiers(self.stats)
        self.proficiency = get_proficiency(level)
        self.max_hps += level * self.modifiers["con"]
        self.spell_slots = self.max_spell_slots = calc_spell_slots(self.class_levels)
        self.pact_slots = self.max_pact_slots = calc_pact_slots(self.class_levels)
        self.calc_ac()
        self.calc_melee_attack()
        if level >= 5:

            pam = [
                RangedMultiAttack(
                    [
                        Attack(
                            to_hit=self.attackbonus,
                            damage=Damage(rolls=[10], flat_bonus=self.modifiers["cha"]),
                            on_hit=[BlastBack(10)],
                            max_distance=24,
                        ),
                        Attack(
                            to_hit=self.attackbonus,
                            damage=Damage(rolls=[10], flat_bonus=self.modifiers["cha"]),
                            on_hit=[BlastBack(10)],
                            max_distance=24,
                        ),
                    ]
                )
            ]
        else:
            pam = False
        return Character(
            hp=self.max_hps,
            ac=self.ac,
            attacks=MeleeMultiAttack(
                [
                    Attack(
                        to_hit=self.attackbonus,
                        damage=Damage(rolls=[self.damage], flat_bonus=self.damage_bonus),
                        max_distance=self.range,
                    )
                    for attack in range(self.attacks)
                ]
            ),
            stats=self.stats,
            name=name,
            level=level,
            spells=self.spells,
            spell_slots=self.spell_slots,
            spellcasting_modifier=max([self.modifiers[stat] for stat in ["wis", "int", "cha"]]),
            imposes_disadv=False,
            has_adv=False,
            resistance=None,
            once_per_long_rest=[],
            long_rest_uses=[],
            party=True,
            PAM=pam,
            reach=self.range,
            maxreach=self.range,
            charge_forward=False,
        )

    def apply_feats(self, feats):
        if feats is not None:
            for feat in feats.individual_feats:
                if isinstance(feat, ASI):
                    for stat in feat.stats:
                        self.stats[stat] += 1
                elif feat == "pam":
                    self.binary_feats["pam"] == 1
                elif isinstance(feat, CharacterModifier):
                    feat.apply(self)
                elif isinstance(feat, Spell):
                    self.spells.append(Spell)
                else:
                    raise ValueError(feat)

    def apply_level(self, level):
        self.apply_class(self.classes[level])
        self.apply_feats(self.feats[level])

    def apply_class(self, clss):
        if clss not in self.class_levels.keys():
            self.class_levels[clss] = 0
        self.class_levels[clss] += 1
        self.levelup(clss, self.class_levels[clss])

    def levelup(self, clss, level):
        self.attacks = 1
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

    # def take_turn(self):
