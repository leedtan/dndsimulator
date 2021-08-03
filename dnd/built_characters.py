# from build_features import agonizing, repelling

from attacks import MeleeMultiAttack  # noqa

# from attacks import Attack, Damage, MeleeAttack, MultiAttack, RangedAttack, RangedMultiAttack
from build_utils import ASI, CharacterModifier, CharacterProgression, Feat, Spell  # , ASI

# from character import Character
# from effects import BlastBack
# from spells import HealingWord, MagicMissile

# # from strategies import Character, Defender, PreserveLife
# from strategies import PreserveLife


def addchaattack(character):
    character.attacks_use.append("cha")


hexadin = CharacterProgression(
    starting_stats={"str": 16, "dex": 8, "con": 15, "int": 8, "wis": 8, "cha": 16},
    classes=["pal"] * 6 + ["warlock"] * 5 + ["pal"] * 12,
    weapon="glaive",
    armor="splint",
    meleevsrange="meleepreferred",
    feats=[Feat(["pam"]), None, None, Feat([ASI(["cha", "cha"])]), None, None]
    # Warlock
    + [
        Feat([Spell("eb"), Spell("hex"), CharacterModifier(addchaattack)]),
        Feat(["agonize"]),
        Feat(["pactblade", "pactweapon", Spell("mirrorimage")]),
    ]
    + [Feat(["warcaster"]), Feat([Spell("spiritshroud")])]
    # Paladin
    + [None, Feat(["resilientcon"])] + [None, None, None],
    name="hexadin",
    color=2,
)
paladin = CharacterProgression(
    starting_stats={"str": 16, "dex": 8, "con": 15, "int": 8, "wis": 8, "cha": 16},
    classes=["pal"] * 6 + ["warlock"] * 5 + ["pal"] * 9,
    weapon="glaive",
    armor="splint",
    meleevsrange="meleepreferred",
    feats=[Feat(["pam"]), None, None, Feat([ASI(["cha", "cha"])]), None, None]
    # Warlock
    + [
        Feat([Spell("eb"), Spell("hex"), CharacterModifier(addchaattack)]),
        Feat(["agonize"]),
        Feat(["pactblade", "pactweapon", Spell("mirrorimage")]),
    ]
    + [Feat(["warcaster"]), Feat([Spell("spiritshroud"), "repel"])]
    # Paladin
    + [None, Feat(["resilientcon"]), None, None, None],
    name="paladin",
    color=2,
)

# starting_stats={
#     k: v
#     for k, v in zip(
#         ["str", "dex", "con", "int", "wis", "cha"], [16, 8, 15, 8, 8, 17]
#     )
# }
