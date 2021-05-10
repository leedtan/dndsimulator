# from character import Character

flag = 0
PLAN_NORMAL = 0
PLAN_CHANGED = 1
PLAN_DEAD = -1


def get_closest_enemy(enemies, coor):
    closest_enemy = enemies[0]
    distance = 10000
    if flag:
        breakpoint()
        a = 2  # noqa
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


def check_react(char, enemy, last_loc, loc, table, state):
    hits = 0
    new_dist = max_distance(loc, enemy.coor)
    last_dist = max_distance(last_loc, enemy.coor)
    if new_dist <= enemy.reach and last_dist >= enemy.reach and enemy.PAM and enemy.has_react:
        for pam_attack in enemy.PAM:
            # hit = pam_attack.roll_hit(
            #     enemy=char, advantage=enemy.has_adv, disadvantage=char.imposes_disadv, caster=char, table=table,
            # )
            # hits += hit

            end_val = enemy.make_attack(enemy.PAM, new_dist, char, table, state, check_death)
            if end_val >= 0:
                return end_val
        enemy.has_react = False
    return hits


def move_path(table, order, char, enemies, move_remaining, state):
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
                reactions = check_react(char, enemy, last_loc, loc, table, state)
                if reactions != 0:
                    return movement, PLAN_DEAD
            if char.coor != loc:
                return movement, PLAN_CHANGED
            if movement >= move_remaining:
                return movement, PLAN_NORMAL
    return movement, PLAN_NORMAL


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


# class Charger(Character):
#     def __init__(self, *args, **kwargs):
#         super(Charger).__init__(*args, **kwargs)
#         self.charge = True


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

    # def cast(self, allies, enemies):
    #     targets = [ally for ally in allies if ally.hp == 0]
    #     num_targets = len(targets)
    #     amount_heal = 15 // num_targets
    #     for target in targets:
    #         target.hp += amount_healed
    #     return True
