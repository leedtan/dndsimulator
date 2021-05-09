from character import Character
from utils import move_to_enemy

flag = 0


def get_closest_enemy(enemies, coor):
    closest_enemy = enemies[0]
    distance = 10000
    if flag:
        breakpoint()
        a = 2
    for enemy in enemies:
        if enemy.hp > 0:
            this_dist = (
                abs(enemy.coor[0] - coor[0])
                + abs(enemy.coor[1] - coor[1])
                + max(abs(enemy.coor[0] - coor[0]), abs(enemy.coor[1] - coor[1])) / 10
            )
            if this_dist < distance:
                distance = this_dist
                closest_enemy = enemy
    return closest_enemy


def get_order(current, reverse_path, self):
    order = [current]
    while True:
        current = reverse_path[current]
        if current is None:
            break
        order.append(current)
        if current == self.coor:
            break
    return order


def check_react(char, enemy, last_loc, loc, table):
    new_dist = max_distance(loc, enemy.coor)
    last_dist = max_distance(last_loc, enemy.coor)
    if (
        new_dist <= enemy.reach
        and last_dist >= enemy.reach
        and enemy.PAM
        and enemy.has_react
    ):
        for pam_attack in enemy.PAM:
            hits = pam_attack.roll_hit(
                enemy=char,
                advantage=enemy.has_adv,
                disadvantage=char.imposes_disadv,
                caster=char,
                table=table,
            )
        enemy.has_react = False


def move_path(table, order, char, enemies, move_remaining):
    movement = 0
    for loc in order[::-1]:
        if loc == char.coor:
            continue

        # step_size = max_distance(char.coor, loc)
        # if step_size != 1:
        #     breakpoint()
        #     raise ValueError("moved more than 1 at a time")
        if table[loc] == 0:
            last_loc = char.coor
            table[last_loc] = 0
            char.coor = loc
            movement += 1
            for enemy in enemies:
                reactions = check_react(char, enemy, last_loc, loc, table)
            if char.coor != loc:
                return movement, 1
            if movement >= move_remaining:
                return movement, 0
    return movement, 0


def max_distance(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


def get_destination(closest_enemy, current, reverse_path):
    min_distance = 99999
    for dest_option in reverse_path.keys():
        distance_to_dest = max_distance(dest_option, closest_enemy.coor)
        if distance_to_dest < min_distance:
            min_distance = distance_to_dest
            current = dest_option
    return current


class Charger(Character):
    def strategy(self, npcs, pcs, table, state):
        coor = self.coor
        if self.party:
            enemies = npcs
        else:
            enemies = pcs
        move_remaining = self.movespeed
        if self.charge:
            stop_move = False
            i = 0
            while move_remaining > 0 and stop_move == False:
                if i > 3:
                    stop_move = True
                    a = 2
                i += 1
                closest_enemy = get_closest_enemy(enemies, self.coor)
                atk_distance = max(
                    abs(closest_enemy.coor[0] - self.coor[0]),
                    abs(closest_enemy.coor[1] - self.coor[1]),
                )
                if atk_distance <= self.reach:
                    stop_move = True
                    break
                final_destination, reverse_path, path_scores = move_to_enemy(
                    self, closest_enemy, table
                )
                current = final_destination
                # if current not in reverse_path.keys():
                #     final_destination = current = get_destination(
                #         closest_enemy, current, reverse_path
                #     )
                order = get_order(current, reverse_path, self)
                moves_used, enemy_moved_me = move_path(
                    table, order, self, enemies, move_remaining
                )
                table[self.coor] = self
                move_remaining -= moves_used
                if enemy_moved_me:
                    continue

                if i > 10:
                    breakpoint()
                    a = 2
                closest_enemy = get_closest_enemy(enemies, self.coor)
                atk_distance = max(
                    abs(closest_enemy.coor[0] - self.coor[0]),
                    abs(closest_enemy.coor[1] - self.coor[1]),
                )
                if atk_distance <= self.reach:
                    stop_move = True
                    break
        atk_distance = max(
            abs(closest_enemy.coor[0] - self.coor[0]),
            abs(closest_enemy.coor[1] - self.coor[1]),
        )
        if atk_distance <= self.reach:
            for attack in self.attacks:
                attack.roll_hit(
                    enemy=closest_enemy,
                    advantage=self.has_adv,
                    disadvantage=closest_enemy.imposes_disadv,
                    caster=self,
                    table=table,
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
