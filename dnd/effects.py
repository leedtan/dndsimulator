from movement_utils import place_closest_position
from table_utils import viz_table


class BlastBack:
    def __init__(self, distance):
        self.distance = distance

    def apply(self, enemy, caster, table):
        ecoor = enemy.coor
        ccoor = caster.coor
        # print("blasting back ", enemy)
        # viz_table(table)
        if ecoor[1] > ccoor[1]:
            enemy.coor = enemy.coor[0], ecoor[1] + self.distance
        if ecoor[1] < ccoor[1]:
            enemy.coor = enemy.coor[0], ecoor[1] - self.distance

        if ecoor[0] > ccoor[0]:
            enemy.coor = ecoor[0] + self.distance, enemy.coor[1]
        if ecoor[0] < ccoor[0]:
            enemy.coor = ecoor[0] - self.distance, enemy.coor[1]
        h, w = table.shape
        enemy.coor = (max(0, enemy.coor[0]), max(0, enemy.coor[1]))
        enemy.coor = (min(h - 1, enemy.coor[0]), min(w - 1, enemy.coor[1]))
        place_closest_position(enemy, enemy.coor, table)
        # print("blasted from ", ecoor, " to: ", enemy.coor)
