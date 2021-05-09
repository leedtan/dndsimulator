from collections import defaultdict
from queue import PriorityQueue


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


def move_to_enemy(self, closest_enemy, table):
    frontier = PriorityQueue()
    frontier.put(self.coor, 0)
    came_from, cost_so_far = (
        {self.coor: None},
        {self.coor: 0},
    )
    i = 0
    while not frontier.empty():
        i = i + 1
        current = frontier.get()
        distance = abs(current[0] - closest_enemy.coor[0]) + abs(
            current[1] - closest_enemy.coor[1]
        )
        reach_distance = max(
            abs(current[0] - closest_enemy.coor[0]),
            abs(current[1] - closest_enemy.coor[1]),
        )
        neighbors = get_neighbors(table, current, closest_enemy.coor, self.party)

        if reach_distance <= self.reach and (
            table[current] == 0 or table[current] == self
        ):
            break
        for next_item in neighbors:
            new_cost = cost_so_far[current] + 1 + (table[next_item] != 0)
            if next_item not in cost_so_far or new_cost < cost_so_far[next_item]:
                cost_so_far[next_item] = new_cost
                priority = new_cost + calc_distance(next_item, closest_enemy.coor)
                frontier.put(next_item, priority)
                came_from[next_item] = current

    return current, came_from, cost_so_far

