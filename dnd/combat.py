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
    for i, pc in enumerate(pcs):
        table[i + 10, -1] = pc
        pc.loc = np.array([i + 10, -1])
    for i, npc in enumerate(npcs):
        table[i + 10, 0] = npc
        npc.loc = np.array([i + 10, 0])
        npc.party = False
    all_characters = pcs + npcs
    state = {"pcs": pcs, "npcs": npcs}
    initiative = roll_init(all_characters)
    #     [setattr(c, 'hp', c.max_hp) for c in initiative]
    #     [setattr(c, 'spell_slots', copy.copy(c.max_spell_slots)) for c in initiative]
    #     [setattr(c, 'long_rest_uses', copy.copy(c.long_rest_uses_max)) for c in initiative]
    last_attacked = -1
    for _ in range(100):
        for character in initiative:
            if character.hp <= 0:
                continue
            loc = character.loc
            c = character
            if character.party:
                enemies = npcs
            else:
                enemies = pcs
            if character.charge:
                closest_enemy = enemies[0]
                distance = 10000
                for enemy in enemies:
                    if enemy.hp > 0:
                        this_dist = abs(enemy.loc[0] - loc[0]) + abs(
                            enemy.loc[1] - loc[1]
                        )
                        if this_dist < distance:
                            distance = this_dist
                            closest_enemy = enemy
                moved = 0
                while moved < c.movespeed and closest_enemy.loc[0] > character.loc[0]:
                    moved += 1
                    character.loc[0] += 1
                while moved < c.movespeed and abs(
                    closest_enemy.loc[1] - character.loc[1]
                ):
                    moved += 1
                    direction = (closest_enemy.loc[1] > character.loc[1]) * 2 - 1
                    character.loc[1] += direction
                table[character.loc[0], character.loc[1]] = character
                enemy = closest_enemy
            atk_distance = max(
                abs(enemy.loc[0] - character.loc[0]),
                abs(enemy.loc[1] - character.loc[1]),
            )
            if atk_distance <= character.reach:
                for attack in character.attacks:
                    attack.roll_hit(
                        enemy=enemy,
                        advantage=c.has_adv,
                        disadvantage=enemy.imposes_disadv,
                    )
                    end_val = check_death(state)
                    if end_val >= 0:
                        return end_val
            end_val = check_death(state)
            if end_val >= 0:
                return end_val
    return -1
