from queue import PriorityQueue

import numpy as np


def heuristic(char, enemy):
    return abs(char.coor[0] - enemy.coor[0]) + abs(char.coor[1] - enemy.coor[1])


# def get_neighbors(table, coor, destination, party):
#     neighbors = []
#     for i in range(-1, 2):
#         for j in range(-1, 2):
#             if i == j == 0:
#                 continue
#             elif coor[0] + i < 0 or coor[0] + i >= table.shape[0]:
#                 continue
#             elif coor[1] + j < 0 or coor[1] + j >= table.shape[1]:
#                 continue
#             else:
#                 next_loc = (coor[0] + i, coor[1] + j)
#                 if (
#                     table[next_loc] == 0 or table[next_loc].party == party
#                 ) or next_loc == destination:
#                     neighbors.append((coor[0] + i, coor[1] + j))
#     return neighbors
def check_table(state, table):
    if len(state["pcs"] + state["npcs"]) != len([c for c in table.flatten() if c != 0]):
        print([(c, c.hp) for c in table.flatten() if c != 0])
        breakpoint()
        blah = 3
        return blah


def get_chars(table):
    return [(c, c.hp) for c in table.flatten() if c != 0]


def get_neighbors(table, coor, destination, party):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (
                not (i == j == 0)
                and not (coor[0] + i < 0 or coor[0] + i >= table.shape[0])
                and not (coor[1] + j < 0 or coor[1] + j >= table.shape[1])
            ):
                next_loc = (coor[0] + i, coor[1] + j)
                if (
                    table[next_loc] == 0 or table[next_loc].party == party
                ) or next_loc == destination:
                    yield next_loc


def calc_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def move_to_enemy(self, closest_enemy, table, move_remaining=None):
    frontier = PriorityQueue()
    frontier.put(self.coor, 0)
    came_from, cost_so_far = (
        {self.coor: None},
        {self.coor: 0},
    )
    i = 0
    best_so_far = (self.coor, np.inf)
    final_destination = None
    while not frontier.empty():
        # if i > 50:
        #     breakpoint()
        i = i + 1
        current = frontier.get()
        # distance = abs(current[0] - closest_enemy.coor[0]) + abs(current[1] - closest_enemy.coor[1])
        reach_distance = max(
            abs(current[0] - closest_enemy.coor[0]),
            abs(current[1] - closest_enemy.coor[1]),
        )
        if reach_distance < best_so_far[1]:
            best_so_far = [current, reach_distance]
        neighbors = get_neighbors(table, current, closest_enemy.coor, self.party)

        if reach_distance <= self.reach and (
            table[current] == 0 or table[current] == self
        ):
            final_destination = current
            break
        if cost_so_far[current] >= move_remaining and table[current] == 0:
            final_destination = best_so_far[0]
            continue
        for next_item in neighbors:
            new_cost = cost_so_far[current] + 1 + (table[next_item] != 0)
            if next_item not in cost_so_far or new_cost < cost_so_far[next_item]:
                cost_so_far[next_item] = new_cost
                priority = new_cost + calc_distance(next_item, closest_enemy.coor)
                frontier.put(next_item, priority)
                came_from[next_item] = current
    # print(i)
    if final_destination is None:
        breakpoint()
        print("figure out what to do if neither conclusion is reached")
    return final_destination, came_from, cost_so_far
