import copy

import numpy as np
from joblib import Parallel, delayed

from classes import giant, goblin, paladin8, umberhulk
from combat import combat


def gauntlet(party):
    stages_completed = 0
    table = np.zeros([20, 20], dtype=object)
    party = [copy.copy(char) for char in party]
    for i, enemies in enumerate(
        [
            [goblin] * 3,
            [umberhulk] * 1,
            [umberhulk] * 1,
            [umberhulk] * 2,
            [umberhulk] * 2,
            [umberhulk] * 3,
            [umberhulk] * 3,
            [giant] * 1,
            [giant] * 2,
            [giant] * 3,
            [giant] * 4,
            [giant] * 5,
            [giant] * 6,
            [giant] * 7,
            [giant] * 8,
        ]
    ):
        if ((i % 2) == 0) and (i > 0):
            [char.shortrest() for char in party]
        if ((i % 6) == 0) and (i > 0):
            [char.longrest() for char in party]

        result = combat(party, [copy.copy(char) for char in enemies], copy.copy(table),)
        if not result:
            return stages_completed
        stages_completed += 1
        party = [char for char in party if char.hp > 0]
    return stages_completed


def main():
    dreamteam = [paladin8, paladin8]
    if 0:
        gauntlets = Parallel(n_jobs=5)(delayed(gauntlet)(dreamteam) for _ in range(10))
    else:
        gauntlets = [gauntlet(dreamteam) for _ in range(30)]
    print(gauntlets)
    return gauntlets


if __name__ == "__main__":
    main()

