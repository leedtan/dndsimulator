from attacks import Attack, Damage, MeleeAttack, MeleeMultiAttack, MultiAttack, RangedAttack, RangedMultiAttack  # noqa
from character import Character
from effects import BlastBack
from spells import HealingWord, MagicMissile

# from strategies import Character, Defender, PreserveLife
from strategies import PreserveLife

barbarian3 = Character(
    hp=36,
    ac=16,
    attacks=Attack(to_hit=5, damage=Damage(rolls=[12], flat_bonus=3)),
    stats={"dex": 2},
    name="barbarian3",
    resistance="all",
    level=3,
)
cleric = Character(
    hp=10,
    ac=18,
    attacks=Attack(to_hit=5, damage=Damage(rolls=[8], flat_bonus=5)),
    spells=[set([HealingWord()])],
    spell_slots=[2],
    stats={"dex": -1},
    spellcasting_modifier=5,
    name="cleric",
    once_per_long_rest=[PreserveLife()],
    level=1,
)
fighter = Character(
    hp=13,
    ac=18,
    attacks=Attack(to_hit=4, damage=Damage(rolls=[6], flat_bonus=2)),
    stats={"dex": -1},
    name="fighter",
    level=1,
)
PAMfighter = Character(
    hp=13,
    ac=18,
    attacks=Attack(to_hit=4, damage=Damage(rolls=[6], flat_bonus=2)),
    stats={"dex": -1},
    name="fighter",
    level=1,
    PAM=[Attack(to_hit=4, damage=Damage(rolls=[6], flat_bonus=2))],
)
cleric3 = Character(
    hp=27,
    ac=18,
    attacks=Attack(to_hit=5, damage=Damage(rolls=[8], flat_bonus=5)),
    spells=[set([HealingWord()]), set([HealingWord()])],
    spell_slots=[4, 2],
    stats={"dex": -1},
    spellcasting_modifier=5,
    name="cleric3",
    once_per_long_rest=[PreserveLife()],
    level=3,
)
PAMfighterBig = Character(
    hp=60,
    ac=18,
    attacks=[
        Attack(to_hit=4, damage=Damage(rolls=[6], flat_bonus=2)),
        Attack(to_hit=4, damage=Damage(rolls=[6], flat_bonus=2)),
        Attack(to_hit=4, damage=Damage(rolls=[4], flat_bonus=2)),
    ],
    stats={"dex": -1},
    name="fighter",
    PAM=Attack(to_hit=4, damage=Damage(rolls=[6], flat_bonus=2)),
    level=3,
)
rogue = Character(
    hp=11,
    ac=14,
    attacks=[
        Attack(to_hit=5, damage=Damage(rolls=[6], flat_bonus=3)),
        Attack(to_hit=5, damage=Damage(rolls=[6], flat_bonus=0)),
    ],
    stats={"dex": 3},
    name="rogue",
    level=1,
)

sorcerer = Character(
    hp=9,
    ac=15,
    attacks=Attack(to_hit=5, damage=Damage(rolls=[10], flat_bonus=0)),
    spells=[set([MagicMissile()])],
    spell_slots=[1],
    stats={"dex": 2},
    name="sorcerer",
    level=1,
)
sorcerer3 = Character(
    hp=23,
    ac=15,
    attacks=Attack(to_hit=5, damage=Damage(rolls=[10], flat_bonus=0)),
    spells=[set([MagicMissile()]), set([MagicMissile()])],
    spell_slots=[3, 2],
    stats={"dex": 2},
    name="sorcerer3",
    level=3,
)
goblin = Character(
    hp=10,
    ac=8,
    attacks=[Attack(to_hit=2, damage=Damage(rolls=[4], flat_bonus=2))],
    stats={"dex": -1},
    name="goblin",
    level=1,
)
umberhulk = Character(
    hp=93,
    ac=18,
    attacks=[
        Attack(to_hit=8, damage=Damage(rolls=[8], flat_bonus=5)),
        Attack(to_hit=8, damage=Damage(rolls=[8, 8], flat_bonus=5)),
    ],
    stats={"dex": -1},
    name="umberhulk",
    imposes_disadv=True,
    has_adv=True,
    level=3,
)
giant = Character(
    hp=300,
    ac=18,
    attacks=[
        Attack(to_hit=12, damage=Damage(rolls=[12], flat_bonus=7)),
        Attack(to_hit=12, damage=Damage(rolls=[12, 12], flat_bonus=7)),
        Attack(to_hit=12, damage=Damage(rolls=[12, 12], flat_bonus=7)),
    ],
    stats={"dex": -1},
    name="giant",
    level=3,
)
warlock = Character(
    hp=11,
    ac=15,
    attacks=Attack(to_hit=5, damage=Damage(rolls=[6], flat_bonus=3)),
    stats={"dex": 2},
    name="warlock",
    level=1,
)
paladin8 = Character(
    hp=100,
    ac=18,
    attacks=[
        RangedMultiAttack(
            [
                Attack(to_hit=6, damage=Damage(rolls=[10], flat_bonus=4), on_hit=[BlastBack(10)], max_distance=24),
                Attack(to_hit=6, damage=Damage(rolls=[10], flat_bonus=4), on_hit=[BlastBack(10)], max_distance=24),
            ]
        ),
        MeleeMultiAttack(
            [
                Attack(to_hit=6, damage=Damage(rolls=[10], flat_bonus=4)),
                Attack(to_hit=6, damage=Damage(rolls=[10], flat_bonus=4)),
                Attack(to_hit=6, damage=Damage(rolls=[4], flat_bonus=4)),
            ]
        ),
    ],
    stats={"dex": 2},
    name="pal6hex2",
    reach=2,
    PAM=[
        RangedMultiAttack(
            [
                Attack(to_hit=6, damage=Damage(rolls=[10], flat_bonus=4), on_hit=[BlastBack(10)], max_distance=24),
                Attack(to_hit=6, damage=Damage(rolls=[10], flat_bonus=4), on_hit=[BlastBack(10)], max_distance=24),
            ]
        ),
        MeleeMultiAttack(
            [
                Attack(to_hit=6, damage=Damage(rolls=[10], flat_bonus=4)),
                Attack(to_hit=6, damage=Damage(rolls=[10], flat_bonus=4)),
                Attack(to_hit=6, damage=Damage(rolls=[4], flat_bonus=4)),
            ]
        ),
    ],
    level=8,
    charge_forward=False,
)
