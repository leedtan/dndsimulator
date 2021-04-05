light_armor ={
    'padded':{
        'name': 'padded',
        'type': 'light armor',
        'cost': 5,
        'armor_class':{'base': 11, 'dex_mod': True, 'dex_mod_max': False},
        'str_req': False,
        'stealth_penalty': True,
        'weight': 8},
    'leather':{
        'name': 'leather',
        'type': 'light armor',
        'cost': 10,
        'armor_class':{'base': 11, 'dex_mod': True, 'dex_mod_max': False},
        'str_req': False,
        'stealth_penalty': False,
        'weight': 10},
    'studded_leather':{
        'name': 'studded_leather',
        'type': 'light armor',
        'cost': 45,
        'armor_class':{'base': 12, 'dex_mod': True , 'dex_mod_max': False},
        'str_req': False,
        'stealth_penalty': False,
        'weight': 13}}
#### medium armor
hide = {
    'name': 'hide',
    'type': 'medium armor',
    'cost': 10,
    'armor_class':{'base': 12, 'dex_mod': True, 'dex_mod_max': 2},
    'str_req': False,
    'stealth_penalty': False,
    'weight': 12}
chain_shirt = {
    'name': 'chain_shirt',
    'type': 'medium armor',
    'cost': 50,
    'armor_class':{'base': 13, 'dex_mod': True, 'dex_mod_max': 2},
    'str_req': False,
    'stealth_penalty': False,
    'weight': 20}
scale_mail = {
    'name': 'scale_mail',
    'type': 'medium armor',
    'cost': 50,
    'armor_class':{'base': 14, 'dex_mod': True, 'dex_mod_max': 2},
    'str_req': False,
    'stealth_penalty': True,
    'weight': 45}
breast_plate = {
    'name': 'breast_plate',
    'type': 'medium armor',
    'cost': 400,
    'armor_class':{'base': 14, 'dex_mod': True, 'dex_mod_max': 2},
    'str_req': False,
    'stealth_penalty': False,
    'weight': 20}
half_plate = {
    'name': 'half_plate',
    'type': 'medium armor',
    'cost': 750,
    'armor_class':{'base': 15, 'dex_mod': True, 'dex_mod_max': 2},
    'str_req': False,
    'stealth_penalty': True,
    'weight': 40}
    #### heavy armor
ring_mail = {
    'name': 'ring_mail',
    'type': 'heavy armor',
    'cost': 30,
    'armor_class':{'base': 14, 'dex_mod': False, 'dex_mod_max': False},
    'str_req': False,
    'stealth_penalty': True,
    'weight': 40}
chain_mail = {
    'name': 'chain_mail',
    'type': 'heavy armor',
    'cost': 75,
    'armor_class':{'base': 16, 'dex_mod': False, 'dex_mod_max': False},
    'str_req': 13,
    'stealth_penalty': True,
    'weight': 55}
splint = {
    'name': 'splint',
    'type': 'heavy armor',
    'cost': 200,
    'armor_class':{'base': 17, 'dex_mod': False, 'dex_mod_max': False},
    'str_req': 15,
    'stealth_penalty': True,
    'weight': 60}
plate = {
    'name': 'plate',
    'type': 'heavy armor',
    'cost': 1500,
    'armor_class':{'base': 18, 'dex_mod': False, 'dex_mod_max': False},
    'str_req': 15,
    'stealth_penalty': True,
    'weight': 65}
### shield
shield = {
    'name': 'shield',
    'type': 'shield',
    'cost': 10,
    'armor_class':{'base': 10, 'dex_mod': False, 'dex_mod_max': False},
    'str_req': False,
    'stealth_penalty': False,
    'weight': 6}