import numpy as np

from strategies import check_death
from table_utils import viz_table
from utils import check_table, get_chars  # noqa


def roll_init(x):
    init = [xi.roll_init() for xi in x]
    order = np.argsort(init)
    init_order = [x[i] for i in order[::-1]]
    return init_order


def combat(pcs, npcs, table, i):
    for i, pc in enumerate(pcs):
        start_x = table.shape[0] // 2 - len(pcs) // 2
        table[i + start_x, -1] = pc
        pc.coor = (i + start_x, table.shape[1] - 1)
    for i, npc in enumerate(npcs):
        start_x = table.shape[0] // 2 - len(npcs) // 2
        table[i + start_x, 0] = npc
        npc.coor = (i + start_x, 0)
        npc.party = False
    all_characters = pcs + npcs
    state = {"pcs": pcs, "npcs": npcs}
    initiative = roll_init(all_characters)
    dbg = False
    for i_combat in range(100):
        for char in initiative:
            if char.hp <= 0:
                continue
            # if i == 1 and i_combat == 3 and char == initiative[3]:
            #     dbg = True
            # breakpoint()
            char.reset_turn()
            # check_table(state, table)
            end_val = char.strategy(npcs, pcs, table, state, dbg=dbg)
            # check_table(state, table)
            end_val = check_death(state, table)
            # check_table(state, table)
            # print(" turn: ", char, [(char, char.hp) for char in table.flatten() if char != 0])
            # check_table(state, table)
            if 0:
                print(
                    char,
                    state,
                    get_chars(table),
                )
                viz_table(table)
            if end_val >= 0:
                return end_val

        end_val = check_death(state, table)
        if end_val >= 0:
            return end_val
    return -1
