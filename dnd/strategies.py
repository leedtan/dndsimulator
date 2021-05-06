from character import Character
from utils import move_to_enemy


class Charger(Character):
    def strategy(self, npcs, pcs, table, state):
        coor = self.coor
        if self.party:
            enemies = npcs
        else:
            enemies = pcs
        if self.charge:
            closest_enemy = enemies[0]
            distance = 10000
            for enemy in enemies:
                if enemy.hp > 0:
                    this_dist = abs(enemy.coor[0] - coor[0]) + abs(
                        enemy.coor[1] - coor[1]
                    )
                    if this_dist < distance:
                        distance = this_dist
                        closest_enemy = enemy
            move_to_enemy(self, closest_enemy)
            table[self.coor[0], self.coor[1]] = self
            enemy = closest_enemy
        atk_distance = max(
            abs(enemy.coor[0] - self.coor[0]), abs(enemy.coor[1] - self.coor[1]),
        )
        if atk_distance <= self.reach:
            for attack in self.attacks:
                attack.roll_hit(
                    enemy=enemy,
                    advantage=self.has_adv,
                    disadvantage=enemy.imposes_disadv,
                )
                end_val = check_death(state)
                if end_val >= 0:
                    return end_val


def check_death(state):
    for char_group, return_val in [["pcs", 0], ["npcs", 1]]:
        alive = [c for c in state[char_group] if c.hp > 0]
        if len(alive) == 0:
            return return_val
    return -1


class PreserveLife:
    def __init__(self):
        self.time = "action"
        pass

    def check_cast(self, allies, enemies):
        num_dead = len([ally for ally in allies if ally.hp == 0])
        return len(num_dead >= 2)

    def cast(self, allies, enemies):
        targets = [ally for ally in allies if ally.hp == 0]
        num_targets = len(targets)
        amount_heal = 15 // num_targets
        for target in targets:
            target.hp += amount_healed
        return True
