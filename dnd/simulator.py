import copy
import itertools
import random

import numpy as np

from attacks import Attack, Damage
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
        [copy.copy(goblin) for _ in range(3)],
        [copy.copy(goblin) for _ in range(7)],
        [copy.copy(goblin) for _ in range(8)],
        [copy.copy(umberhulk)],
        [copy.copy(umberhulk), copy.copy(umberhulk)],
    ]:
        result = combat([copy.copy(char) for char in party], enemies, table)
        if not result:
            return stages_completed
        stages_completed += 1
    return stages_completed


def main():
    sorc_team = [sorcerer, sorcerer, sorcerer, sorcerer, fighter, fighter]
    gauntlets = [gauntlet(sorc_team) for _ in range(100)]
    print(gauntlets)


if __name__ == "__main__":
    main()
