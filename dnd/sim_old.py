import copy
import itertools
import random

import numpy as np

from attacks import Attack, Damage
from character import Character
from classes import (
    barbarian3,
    cleric,
    cleric3,
    fighter,
    goblin,
    rogue,
    sorcerer,
    sorcerer3,
    umberhulk,
    warlock,
)
from combat import combat

# def check_heal(time, state, c):
#     available_spells = possible_spells(c, time, "heal")
#     ally = get_target(c, state, "ally", "dead")
#     if len(available_spells) == 0 or ally == -1:
#         return -1
#     spell = available_spells[0]
#     slot = spell.cast(ally, c.spell_slots, c.spellcasting_modifier)
#     return slot


# def possible_spells(c, time, spell_type):
#     available_spells = [
#         spells for spells, slots in zip(c.spells, c.spell_slots) if slots > 0
#     ]
#     available_spells = list(itertools.chain(*available_spells))
#     available_spells = [
#         spell
#         for spell in available_spells
#         if spell.time == time and spell.type == spell_type
#     ]
#     return available_spells


# def get_available_targets(characters, target_hps):
#     if target_hps == "dead":
#         return [c for c in characters if c.hp == 0]
#     if target_hps == "alive":
#         return [c for c in characters if c.hp >= 1]
#     return characters


# def get_target(character, state, target_type="enemy", target_hps=None):
#     if target_type == "enemy":
#         target_hps = "alive"
#     if bool(character in state["pcs"]) ^ bool(target_type == "ally"):
#         targets = get_available_targets(state["npcs"], target_hps)
#     else:
#         targets = get_available_targets(state["pcs"], target_hps)
#     if len(targets) > 0:
#         return targets[0]
#     else:
#         return -1


# team_PCs = [fighter, cleric, rogue, warlock]

# num_trials = 1000

# table = np.zeros([100, 100], dtype=object)

# strongest_team = [copy.copy(c) for c in [fighter, sorcerer, sorcerer, cleric]]
# bigger_team = [
#     copy.copy(c) for c in [fighter, fighter, sorcerer, cleric, cleric, cleric]
# ]
# biggest_team = [
#     copy.copy(c)
#     for c in [fighter, fighter, sorcerer, sorcerer, sorcerer, cleric, cleric, cleric]
# ]
# biggest_team = [copy.copy(c) for c in [fighter] * 2 + [sorcerer] * 6 + [cleric] * 2]
# lvl_3s = [copy.copy(c) for c in [barbarian3] * 1 + [sorcerer3] * 1 + [cleric3] * 1]

# cleric_team = [copy.deepcopy(cleric) for _ in range(4)]
# rogue_team = [copy.deepcopy(rogue) for _ in range(4)]
# sorc_team = [copy.deepcopy(sorcerer) for _ in range(4)]
# warlock_team = [copy.deepcopy(warlock) for _ in range(4)]
# fighter_team = [copy.deepcopy(fighter) for _ in range(4)]
# "0.97" means team 1 wins 97% of the team against team 2
# print(sum([combat(sorc_team, cleric_team, 'last') for _ in range(100)])/100)
# combat(cleric_team, sorc_team)
# sum(
#     [
#         combat(
#             [copy.copy(char) for char in sorc_team],
#             [copy.copy(char) for char in strongest_team],
#             table,
#         )
#         for _ in range(num_trials)
#     ]
# ) / num_trials


def gauntlet(party):
    stages_completed = 0
    table = np.zeros([100, 100], dtype=object)
    for enemies in [
        [copy.copy(goblin)],
        [copy.copy(goblin) for _ in range(10)],
        [copy.copy(umberhulk)],
        [copy.copy(umberhulk), copy.copy(umberhulk)],
    ]:
        result = combat([copy.copy(char) for char in party], enemies, table)
        if not result:
            return stages_completed
        stages_completed += 1
    return stages_completed


gauntlets = [gauntlet(sorc_team) for _ in range(100)]
print(gauntlets)
# sum([combat(lvl_3s, [umberhulk], table) for _ in range(num_trials)]) / num_trials

# sum(
#     [
#         combat(lvl_3s, [umberhulk, copy.copy(umberhulk)], table)
#         for _ in range(num_trials)
#     ]
# ) / num_trials
