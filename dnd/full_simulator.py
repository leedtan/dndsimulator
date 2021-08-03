import copy
import random

import matplotlib.pyplot as plt  # noqa
import numpy as np
import pandas as pd
from joblib import Parallel, delayed

from built_characters import hexadin, paladin  # noqa
from classes import giant, goblin, umberhulk
from combat import combat

random.seed(1)
np.random.seed(1)


def gauntlet(party, level=3):
    stages_completed = 0
    table = np.zeros([15, 15], dtype=object)
    party = [char.sample_at_level(level, name=str(i)) for i, char in enumerate(party)]
    for i, enemies in enumerate(
        [
            [goblin] * 3,
            [umberhulk] * 1,
            [umberhulk] * 2,
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

        result = combat(party, [copy.copy(char) for char in enemies], copy.copy(table), i)
        if not result:
            return stages_completed
        stages_completed += 1
        party = [char for char in party if char.hp > 0]
    return stages_completed


def main():
    scores = pd.DataFrame()
    for lvl in range(11, 16):
        dreamteam = [paladin, paladin, paladin]
        if 0:
            gauntlets = Parallel(n_jobs=5)(delayed(gauntlet)(dreamteam, lvl) for _ in range(10))
        else:
            gauntlets = [gauntlet(dreamteam, lvl) for _ in range(10)]
        print(gauntlets)
        scores[lvl] = gauntlets
    return scores


if __name__ == "__main__":
    main()
