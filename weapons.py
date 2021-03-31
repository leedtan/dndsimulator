#### simple melee weapons
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
#### simple ranged weapons
crossbow_light = {
    'category': 'simple',
    'type': 'ranged',
    'cost':{'currency': 'gp', 'amount': 25},
    'damage':{'dice': 'd8', 'num_to_roll': 1},
    'damage_type': 'piercing',
    'weight': 5,
    'properties': ['ammunition', 'loading', 'two_handed'],
    'range':{'short':80, 'long':320}}
dart = {
    'category': 'simple',
    'type': 'ranged',
    'cost':{'currency': 'cp', 'amount': 5},
    'damage':{'dice': 'd4', 'num_to_roll': 1},
    'damage_type': 'piercing',
    'weight': .25,
    'properties': ['finesse', 'thrown'],
    'range':{'short':20, 'long': 60}}
shortbow = {
    'category': 'simple',
    'type': 'ranged',
    'cost':{'currency': 'gp', 'amount': 25},
    'damage':{'dice': 'd6', 'num_to_roll': 1},
    'damage_type': 'piercing',
    'weight': 2,
    'properties': ['ammunition', 'two_handed'],
    'range':{'short': 80, 'long': 320}}
sling = {
    'category': 'simple',
    'type': 'ranged',
    'cost':{'currency': 'sp', 'amount': 1},
    'damage':{'dice': 'd4', 'num_to_roll': 1},
    'damage_type': 'bludgeoning',
    'weight': False,
    'properties': ['ammunition'],
    'range':{'short': 30, 'long': 120}}
#### martial melee weapons
battleaxe = {
    'category': 'martial',
    'type': 'melee',
    'cost':{'currency': 'gp', 'amount': 10},
    'damage':{'dice': 'd8', 'num_to_roll': 1},
    'damage_type': 'slashing',
    'weight': 4,
    'properties': ['versetile'],
    'two_handed':{'dice': 'd10', 'num_to_roll': 1 }}
flail = {
    'category': 'martial',
    'type': 'melee',
    'cost':{'currency': 'gp', 'amount': 10},
    'damage':{'dice': 'd8', 'num_to_roll': 1},
    'damage_type': 'bludgeoning',
    'weight': 2,
    'properties': [False]}
glaive = {
    'category': 'martial',
    'type': 'melee',
    'cost':{'currency': 'gp', 'amount': 20},
    'damage':{'dice': 'd10', 'num_to_roll': 1},
    'damage_type': 'slashing',
    'weight': 6,
    'properties': ['heavy', 'reach', 'two_handed']}
greataxe = {
    'category': 'martial',
    'type': 'melee',
    'cost':{'currency': 'gp', 'amount': 30},
    'damage':{'dice': 'd12', 'num_to_roll': 1},
    'damage_type': 'slashing',
    'weight': 7,
    'properties': ['heavy', 'two_handed']}
greatsword = {
    'category': 'martial',
    'type': 'melee',
    'cost':{'currency': 'gp', 'amount': 50},
    'damage':{'dice': 'd6', 'num_to_roll': 2},
    'damage_type': 'slashing',
    'weight': 6,
    'properties': ['heavy', 'two_handed']}
halberd= {
    'category': 'martial',
    'type': 'melee',
    'cost':{'currency': 'gp', 'amount': 20},
    'damage':{'dice': 'd10' , 'num_to_roll': 1},
    'damage_type': 'slashing',
    'weight': 6,
    'properties': ['heavy', 'reach', 'two_handed']}
lance = {
    'category': 'martial',
    'type': 'melee',
    'cost':{'currency': 'gp', 'amount': 10},
    'damage':{'dice': 'd12', 'num_to_roll': 1},
    'damage_type': 'piercing',
    'weight': 6,
    'properties': ['reach', 'special']}
longsword = {
    'category': 'martial',
    'type': 'melee',
    'cost':{'currency': 'gp', 'amount': 15},
    'damage':{'dice': 'd8', 'num_to_roll': 1},
    'damage_type': 'slashing',
    'weight': 3,
    'properties': ['versatile'],
    'two_handed':{'dice': 'd10', 'num_to_roll': 1}}
maul = {
    'category': 'martial',
    'type': 'melee',
    'cost':{'currency': 'gp', 'amount': 10},
    'damage':{'dice': 'd6', 'num_to_roll': 2},
    'damage_type': 'bludgeoning',
    'weight': 10,
    'properties': ['heavy', 'two_handed']}
morningstar = {
    'category': 'martial',
    'type': 'melee',
    'cost':{'currency': 'gp', 'amount': 15},
    'damage':{'dice': 'd8', 'num_to_roll': 1},
    'damage_type': 'piercing',
    'weight': 4,
    'properties': [False]}
pike = {
    'category': 'martial',
    'type': 'melee',
    'cost':{'currency': 'gp', 'amount': 5},
    'damage':{'dice': 'd10', 'num_to_roll': 1},
    'damage_type': 'piercing',
    'weight': 18,
    'properties': ['heavy', 'reach', 'two_handed']}
rapier = {
    'category': 'martial',
    'type': 'melee',
    'cost':{'currency': 'gp', 'amount': 25},
    'damage':{'dice': 'd8', 'num_to_roll': 1},
    'damage_type': 'piercing',
    'weight': 2,
    'properties': ['finesse']}
scimitar = {
    'category': 'martial',
    'type': 'melee',
    'cost':{'currency': 'gp', 'amount': 25},
    'damage':{'dice': 'd6', 'num_to_roll': 1},
    'damage_type': 'slashing',
    'weight': 3,
    'properties': ['finesse', 'light']}
shortsword = {
    'category': 'martial',
    'type': 'melee',
    'cost':{'currency': 'gp', 'amount': 10},
    'damage':{'dice': 'd6', 'num_to_roll': 1},
    'damage_type': 'piercing',
    'weight': 2,
    'properties': ['finesse', 'light']}
trident = {
    'category': 'martial',
    'type': 'melee',
    'cost':{'currency': 'gp', 'amount': 5},
    'damage':{'dice': 'd6', 'num_to_roll': 1},
    'damage_type': 'piercing',
    'weight': 4,
    'properties': ['thrown', 'versatile'],
    'two_handed':{'dice': 'd8', 'num_to_roll': 1},
    'range':{'short': 20, 'long': 60}}
war_pick = {
    'category': 'martial',
    'type': 'melee',
    'cost':{'currency': 'gp', 'amount': 5},
    'damage':{'dice': 'd8', 'num_to_roll': 1},
    'damage_type': 'piercing',
    'weight': 2,
    'properties': [False]}
warhammer = {
    'category': 'martial',
    'type': 'melee',
    'cost':{'currency': 'gp', 'amount': 15},
    'damage':{'dice': 'd8', 'num_to_roll': 1},
    'damage_type': 'bludgeoning',
    'weight': 2,
    'properties': ['versatile'],
    'two_handed':{'dice': 'd10', 'num_to_roll': 1}}
whip = {
    'category': 'martial',
    'type': 'melee',
    'cost':{'currency': 'gp', 'amount': 2},
    'damage':{'dice': 'd4', 'num_to_roll': 1},
    'damage_type': 'slashing',
    'weight': 3,
    'properties': ['finesse', 'reach']}
#### martial ranged weapons
blowgun = {
    'category': 'martial',
    'type': 'ranged',
    'cost':{'currency': 'gp', 'amount': 10},
    'damage':{'dice': 'd1', 'num_to_roll': 1},
    'damage_type': 'piercing',
    'weight': 1,
    'properties': ['ammunition', 'loading'],
    'range':{'short': 25, 'long': 100}}
crossbow_hand = {
    'category': 'martial',
    'type': 'ranged',
    'cost':{'currency': 'gp', 'amount': 75},
    'damage':{'dice': 'd6', 'num_to_roll': 1},
    'damage_type': 'piercing',
    'weight': 3,
    'properties': ['ammunition', 'light', 'loading'],
    'range':{'short': 30, 'long': 100}}
crossbow_heavy = {
    'category': 'martial',
    'type': 'ranged',
    'cost':{'currency': 'gp', 'amount': 50},
    'damage':{'dice': 'd10', 'num_to_roll': 1},
    'damage_type': 'piercing',
    'weight': 'weight',
    'properties': ['ammunition', 'heavy', 'loading', 'two_handed'],
    'range':{'short': 100, 'long': 400}}
longbow = {
    'category': 'martial',
    'type': 'ranged',
    'cost':{'currency': 'gp', 'amount': 50},
    'damage':{'dice': 'd8', 'num_to_roll': 1},
    'damage_type': 'piercing',
    'weight': 2,
    'properties': ['ammunition', 'heavy', 'two_handed']}
net = {
    'category': 'martial',
    'type': 'ranged',
    'cost':{'currency': 'gp', 'amount': 1},
    'damage':{'dice': False, 'num_to_roll': False},
    'damage_type': False,
    'weight': 3,
    'properties': ['special', 'thrown'],
    'range':{'short': 5, 'long': 15}}