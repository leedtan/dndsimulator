def move_to_enemy(self, closest_enemy):
    moved = 0
    while moved < self.movespeed and abs(closest_enemy.coor[0] - self.coor[0]) > 1:
        moved += 1
        direction = (closest_enemy.coor[0] > self.coor[0]) * 2 - 1
        self.coor[0] += direction
    while moved < self.movespeed and abs(closest_enemy.coor[1] - self.coor[1]):
        moved += 1
        direction = (closest_enemy.coor[1] > self.coor[1]) * 2 - 1
        self.coor[1] += direction
