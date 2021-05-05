import copy
import itertools
import random

import numpy as np

from attacks import Attack, Damage
from character import Character
from classes import (
    barbarian3,
    cleric,
    cleric3,
    fighter,
    goblin,
    rogue,
    sorcerer,
    sorcerer3,
    umberhulk,
    warlock,
)
from combat import combat


def gauntlet(party):
    stages_completed = 0
    table = np.zeros([100, 100], dtype=object)
    for enemies in [
        [copy.copy(goblin)],
        [copy.copy(goblin) for _ in range(10)],
        [copy.copy(umberhulk)],
        [copy.copy(umberhulk), copy.copy(umberhulk)],
    ]:
        result = combat([copy.copy(char) for char in party], enemies, table)
        if not result:
            return stages_completed
        stages_completed += 1
    return stages_completed


sorc_team = [copy.deepcopy(sorcerer) for _ in range(4)]
gauntlets = [gauntlet(sorc_team) for _ in range(100)]
print(gauntlets)

