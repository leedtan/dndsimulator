# from build_features import agonizing, repelling

from attacks import MeleeMultiAttack  # noqa

# from attacks import Attack, Damage, MeleeAttack, MultiAttack, RangedAttack, RangedMultiAttack
from build_utils import CharacterProgression, Feat, Spell  # , ASI

# from character import Character
# from effects import BlastBack
# from spells import HealingWord, MagicMissile

# # from strategies import Character, Defender, PreserveLife
# from strategies import PreserveLife

hexadin = CharacterProgression(
    starting_stats={"str": 16, "dex": 8, "con": 15, "int": 8, "wis": 8, "cha": 16},
    classes=["pal"] * 6 + ["warlock"] * 5 + ["pal"] * 12,
    weapon="glaive",
    armor="scalemail",
    feats=[Feat(["pam"]), None, None, Feat(["cha", "cha"]), None, None]
    # Warlock
    + [Feat([Spell("eb"), Spell("hex")]), Feat(["agonize"]), Feat(["pactblade", "pactweapon", Spell("mirrorimage")])]
    + [Feat(["warcaster"]), Feat([Spell("spiritshroud")])]
    # Paladin
    + [None, Feat(["resilientcon"])] + [None, None, None],
)

# starting_stats={
#     k: v
#     for k, v in zip(
#         ["str", "dex", "con", "int", "wis", "cha"], [16, 8, 15, 8, 8, 17]
#     )
# }
