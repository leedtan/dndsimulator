import copy
import itertools
import random

import numpy as np

from attacks import Attack, Damage
from character import Character
from effects import BlastBack
from spells import HealingWord, MagicMissile
from strategies import Charger, PreserveLife

barbarian3 = Charger(
    hp=36,
    ac=16,
    attacks=Attack(to_hit=5, damage=Damage(rolls=[12], flat_bonus=3)),
    stats={"dex": 2},
    name="barbarian3",
    resistance="all",
)
cleric = Charger(
    hp=10,
    ac=18,
    attacks=Attack(to_hit=5, damage=Damage(rolls=[8], flat_bonus=5)),
    spells=[set([HealingWord()]),],
    spell_slots=[2,],
    stats={"dex": -1},
    spellcasting_modifier=5,
    name="cleric",
    once_per_long_rest=[PreserveLife()],
)
cleric3 = Charger(
    hp=27,
    ac=18,
    attacks=Attack(to_hit=5, damage=Damage(rolls=[8], flat_bonus=5)),
    spells=[set([HealingWord()]), set([HealingWord()])],
    spell_slots=[4, 2],
    stats={"dex": -1},
    spellcasting_modifier=5,
    name="cleric3",
    once_per_long_rest=[PreserveLife()],
)
fighter = Charger(
    hp=13,
    ac=18,
    attacks=Attack(to_hit=4, damage=Damage(rolls=[6], flat_bonus=2)),
    stats={"dex": -1},
    name="fighter",
)
PAMfighter = Charger(
    hp=13,
    ac=18,
    attacks=Attack(to_hit=4, damage=Damage(rolls=[6], flat_bonus=2)),
    stats={"dex": -1},
    name="fighter",
    PAM=[Attack(to_hit=4, damage=Damage(rolls=[6], flat_bonus=2))],
)
PAMfighterBig = Charger(
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
)
rogue = Charger(
    hp=11,
    ac=14,
    attacks=[
        Attack(to_hit=5, damage=Damage(rolls=[6], flat_bonus=3)),
        Attack(to_hit=5, damage=Damage(rolls=[6], flat_bonus=0)),
    ],
    stats={"dex": 3},
    name="rogue",
)

sorcerer = Character(
    hp=9,
    ac=15,
    attacks=Attack(to_hit=5, damage=Damage(rolls=[10], flat_bonus=0)),
    spells=[set([MagicMissile()]),],
    spell_slots=[1,],
    stats={"dex": 2},
    name="sorcerer",
)
sorcerer3 = Charger(
    hp=23,
    ac=15,
    attacks=Attack(to_hit=5, damage=Damage(rolls=[10], flat_bonus=0)),
    spells=[set([MagicMissile()]), set([MagicMissile()])],
    spell_slots=[3, 2,],
    stats={"dex": 2},
    name="sorcerer3",
)
goblin = Charger(
    hp=10,
    ac=8,
    attacks=[Attack(to_hit=2, damage=Damage(rolls=[4], flat_bonus=2))],
    stats={"dex": -1},
    name="goblin",
)
umberhulk = Charger(
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
)
giant = Charger(
    hp=300,
    ac=18,
    attacks=[
        Attack(to_hit=12, damage=Damage(rolls=[12], flat_bonus=7)),
        Attack(to_hit=12, damage=Damage(rolls=[12, 12], flat_bonus=7)),
        Attack(to_hit=12, damage=Damage(rolls=[12, 12], flat_bonus=7)),
    ],
    stats={"dex": -1},
    name="giant",
)
warlock = Charger(
    hp=11,
    ac=15,
    attacks=Attack(to_hit=5, damage=Damage(rolls=[6], flat_bonus=3)),
    stats={"dex": 2},
    name="warlock",
)
paladin8 = Charger(
    hp=100,
    ac=18,
    attacks=[
        Attack(to_hit=6, damage=Damage(rolls=[10], flat_bonus=4)),
        Attack(to_hit=6, damage=Damage(rolls=[10], flat_bonus=4)),
        Attack(to_hit=6, damage=Damage(rolls=[4], flat_bonus=4)),
    ],
    stats={"dex": 2},
    name="warlock",
    reach=2,
    PAM=[
        Attack(
            to_hit=6, damage=Damage(rolls=[10], flat_bonus=4), on_hit=[BlastBack(10)]
        ),
        Attack(
            to_hit=6, damage=Damage(rolls=[10], flat_bonus=4), on_hit=[BlastBack(10)]
        ),
    ],
)
