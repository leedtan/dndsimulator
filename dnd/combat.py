import numpy as np


def check_death(state):
    for char_group, return_val in [["pcs", 0], ["npcs", 1]]:
        alive = [c for c in state[char_group] if c.hp > 0]
        if len(alive) == 0:
            return return_val
    return -1


def roll_init(x):
    init = [xi.roll_init() for xi in x]
    order = np.argsort(init)
    init_order = [x[i] for i in order[::-1]]
    return init_order


def combat(pcs, npcs, table):
    avg = table.shape[0]
    for i, pc in enumerate(pcs):
        table[i + avg, -1] = pc
        pc.coor = (i + avg, table.shape[1] - 1)
    for i, npc in enumerate(npcs):
        table[i + avg, 0] = npc
        npc.coor = (i + avg, 0)
        npc.party = False
    all_characters = pcs + npcs
    state = {"pcs": pcs, "npcs": npcs}
    initiative = roll_init(all_characters)
    for _ in range(100):
        for character in initiative:
            if character.hp <= 0:
                continue
            character.reset_turn()
            end_val = character.strategy(npcs, pcs, table, state)
            end_val = check_death(state)
            if end_val >= 0:
                return end_val

        end_val = check_death(state)
        if end_val >= 0:
            return end_val
    return -1
