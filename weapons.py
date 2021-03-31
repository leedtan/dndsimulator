club = {
    'category': 'simple',
    'type': 'melee',
    'cost': {'currency': 'sp', 'amount': 1},
    'damage': {'dice': 'd4', 'num_to_roll': 1},
    'damage_type': 'bludgeoning',
    'weight': 2,
    'properties':['light']}
dagger = {
    'category': 'simple',
    'type': 'melee',
    'cost': {'currency': 'gp', 'amount': 2},
    'damage':{'dice': 'd4', 'num_to_roll': 1},
    'damage_type': 'piercing',
    'weight': 1,
    'properties':['finesse', 'light', 'thrown'],
    'range':{'short':20, 'long':60}}
greatclub = {
    'category': 'simple',
    'type': 'melee',
    'cost':{'currency': 'sp', 'amount':2},
    'damage': {'dice': 'd8', 'num_to_roll': 1},
    'damage_type': 'bludgeoning',
    'weight': 10,
    'properties':['two-handed']}
handaxe = {
    'category': 'simple',
    'type': 'melee',
    'cost':{'currency': 'gp', 'amount': 5},
    'damage':{'dice': 'd6', 'num_to_roll': 2},
    'damage_type': 'slashing',
    'weight': 2,
    'properties':['light', 'thrown'],
    'range':{'short':20, 'long':60}}
javelin = {
    'category': 'simple',
    'type': 'melee',
    'cost':{'currency': 'sp', 'amount': 5},
    'damage':{'dice': 'd6', 'num_to_roll': 1},
    'damage_type': 'piercing',
    'weight': 2,
    'properties':['light', 'thrown'],
    'range':{'short':30, 'long':120}}
light_hammer = {
    'category': 'simple',
    'type': 'melee',
    'cost':{'currency':'gp', 'amount': 2},
    'damage':{'dice':'d4', 'num_to_roll':1},
    'damage_type': 'bludgeoning',
    'weight': 2,
    'properties':['light', 'thrown'],
    'range':{'short':20, 'long':60}}
mace = {
    'category': 'simple',
    'type': 'melee',
    'cost':{'currency':'gp', 'amount': 5},
    'damage':{'dice':'d6', 'num_to_roll': 1},
    'damage_type': 'bludgeoning',
    'weight':4,
    'properties': False}
quarterstaff = {
    'category': 'simple',
    'type': 'melee',
    'cost':{'currency': 'sp', 'amount': 2},
    'damage':{'dice':'d6', 'num_to_roll': 1},
    'damage_type': 'bludgeoning',
    'weight': 4,
    'properties':['versetile'],
    'two_handed_damage':{'dice': 'd8', 'num_to_roll': 1}}
sickle = {
    'category': 'simple',
    'type': 'melee',
    'cost':{'currency': 'gp', 'amount':1},
    'damage':{'dice': 'd4', 'num_to_roll': 1},
    'damage_type': 'slashing',
    'weight': 2,
    'properties':['light']}
spear = {
    'category': 'simple',
    'type': 'melee',
    'cost':{'currency': 'gp', 'amount': 1},
    'damage':{'dice': 'd6', 'num_to_roll': 1},
    'damage_type':'piercing',
    'weight': 3,
    'properties':['thrown', 'versitile'],
    'range':{'short': 20, 'long': 60},
    'two_handed_damage':{'dice': 'd8', 'num_to_roll': 1}}