from movement_utils import place_closest_position


class BlastBack:
    def __init__(self, distance):
        self.distance = distance

    def apply(self, enemy, caster, table):
        ecoor = enemy.coor
        ccoor = caster.coor

        if ecoor[0] > ccoor[0]:
            enemy.coor[0] = ecoor[0] + distance
        if ecoor[0] < ccoor[0]:
            enemy.coor[0] = ecoor[0] - distance

        if ecoor[1] > ccoor[1]:
            enemy.coor[1] = ecoor[1] + distance
        if ecoor[1] < ccoor[1]:
            enemy.coor[1] = ecoor[1] - distance

        place_closest_position(enemy, enemy.coor, table)
