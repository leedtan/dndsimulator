import copy
import itertools
import random

import numpy as np

from attacks import Attack, Damage
from classes import (
    PAMfighter,
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
    table = np.zeros([8, 8], dtype=object)
    for enemies in [
        [goblin] * 1,
        [goblin] * 2,
        [umberhulk] * 1,
        [umberhulk] * 1,
    ]:
        result = combat(
            [copy.copy(char) for char in party],
            [copy.copy(char) for char in enemies],
            copy.copy(table),
        )
        print("finished a combat", result)
        if not result:
            return stages_completed
        stages_completed += 1
    return stages_completed


def main():
    dreamteam = [PAMfighter, PAMfighter]
    gauntlets = [gauntlet(dreamteam) for _ in range(10)]
    print(gauntlets)
    return gauntlets


if __name__ == "__main__":
    main()
