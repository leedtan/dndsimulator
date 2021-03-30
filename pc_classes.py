### ability_by_method comes from players guides on rpgbot.net

prof_bonus ={1:2, 2:2, 3:2, 4:2, 5:3, 6:3, 7:3, 8:3, 9:4, 10:4, 11:4, 12:4, 
             13:5, 14:5, 15:5, 16:5, 17:6, 18:6, 19:6, 20:6}

barbarian = {
    'pc_class': 'barbarian',
    'hit_die':'d12',
    'primary_ability': 'str',
    'saving_throw_prof':['str', 'con'],
    'arm_weap_prof':['light armor', 'medium armor', 'shields', 'simple weapons', 'martial weapons'],
    'ability_by_method':{
        'pb':{
            'str': 15, 
            'dex': 14,
            'con': 14,
            'int':  8, 
            'wis': 10,
            'cha': 10}, 
        'sa':{
            'str': 15, 
            'dex': 13, 
            'con': 14, 
            'int':  8, 
            'wis': 10, 
            'cha':12}}}
bard ={
    'pc_class': 'bard',
    'hit_die':'d8',
    'primary_ability': 'cha',
    'saving_throw_prof':['dex', 'cha'],
    'arm_weap_prof':['light armor', 'simple weapons', 'hand crossbows', 'long swords', 'rapiers', 'short swords'],
    'ability_by_method':{
        'pb':{
            'str':  8, 
            'dex': 15,
            'con': 13,
            'int': 12 , 
            'wis': 10,
            'cha': 15}, 
        'sa':{
            'str':  8, 
            'dex': 14, 
            'con': 13, 
            'int': 12, 
            'wis': 10, 
            'cha': 15}}}
cleric = {
    'pc_class': 'cleric',
    'hit_die':'d8',
    'primary_ability': 'wis',
    'saving_throw_prof':['wis', 'cha'],
    'arm_weap_prof':['light armor', 'medium armor', 'shields', 'simple weapons'],
    'ability_by_method':{
        'pb':{
            'light armor':{
                'str':  8, 
                'dex': 14,
                'con': 14,
                'int':  8, 
                'wis': 15,
                'cha': 12},
            'medium armor':{
                'str':  8, 
                'dex': 14,
                'con': 14,
                'int':  8, 
                'wis': 15,
                'cha': 12},
            'heavy armor':{
                'str': 14, 
                'dex':  8,
                'con': 14,
                'int':  8, 
                'wis': 15,
                'cha': 12}},                     
        'sa':{
            'light armor':{
                'str':  8, 
                'dex': 14,
                'con': 13,
                'int': 12, 
                'wis': 15,
                'cha': 10},
            'medium armor':{
                'str': 12, 
                'dex': 13,
                'con': 14,
                'int': 10, 
                'wis': 15,
                'cha':  8},
            'heavy armor':{
                'str': 13, 
                'dex':  8,
                'con': 14,
                'int': 12, 
                'wis': 15,
                'cha': 10}}}}                    
druid ={
    'pc_class': 'druid',
    'hit_die':'d8',
    'primary_ability': 'wis',
    'saving_throw_prof':['int', 'wis'],
    'arm_weap_prof':['light armor(non-metal)', 'medium armor(non-metal)', 'shields(non-metal)', 
                     'clubs','daggers', 'darts', 'javelins', 'maces', 'quarterstaffs', 'scimitars', 
                    'sicles', 'slings', 'spears'],
    'ability_by_method':{
        'pb':{
            'str':  8, 
            'dex': 14,
            'con': 14,
            'int': 12 , 
            'wis': 15,
            'cha':  8}, 
        'sa':{
            'str': 10, 
            'dex': 13, 
            'con': 14, 
            'int': 12, 
            'wis': 15, 
            'cha':  8}}}
fighter ={
    'pc_class': 'fighter',
    'hit_die':'d10',
    'primary_ability': ['str','dex'],
    'saving_throw_prof':['str', 'con'],
    'arm_weap_prof':['all'],
    'ability_by_method':{
        'pb':{
            'Strength_based':{
                'str': 15,
                'dex': 10,
                'con': 15,
                'int': 10,
                'wis': 12,
                'cha':  8},
            'E_Knight/Psi_War_based':{
                'str': 15,
                'dex':  8,
                'con': 14,
                'int': 14,
                'wis': 12,
                'cha':  8},
            'Finesse/Archery_based':{
                'str':  8,
                'dex': 15,
                'con': 15,
                'int': 10,
                'wis': 13,
                'cha': 10}},                     
        'sa':{
            'str_based':{
                'str': 15,
                'dex':  8,
                'con': 14,
                'int': 10,
                'wis': 13,
                'cha': 12},
            'E_Knight/Psi_War_based':{
                'str': 15,
                'dex':  8,
                'con': 14,
                'int': 13,
                'wis': 12,
                'cha': 10},
            'Finesse/Archery_based':{
                'str':  8,
                'dex': 15,
                'con': 14,
                'int': 10,
                'wis': 13,
                'cha': 12}}}}                                  
monk ={
    'pc_class': 'monk',
    'hit_die':'d8',
    'primary_ability': ('dex', 'wis'),
    'saving_throw_prof':['str', 'dex'],
    'arm_weap_prof':['simple weapons', 'short swords'],
    'ability_by_method':{
        'pb':{
            'str':  8,
            'dex': 15,
            'don': 14,
            'dnt': 10,
            'wis': 15,
            'cha':  8}, 
        'sa':{
            'str': 12,
            'dex': 15,
            'con': 14,
            'int': 10,
            'wis': 13,
            'cha':  8}}}
paladin ={
    'pc_class': 'paladin',
    'hit_die':'d10',
    'primary_ability': ('str', 'cha'),
    'saving_throw_prof':['wis', 'cha'],
    'arm_weap_prof':['all'],
    'ability_by_method':{
        'pb':{
            'str_based':{
                'str': 15,
                'dex':  8,
                'con': 15,
                'int':  8,
                'wis':  8,
                'cha': 15},
            'dex_based':{
                'str':  8,
                'dex': 15,
                'con': 15,
                'int':  8,
                'wis':  8,
                'cha': 15},
            'cha_based':{
                'str': 15,
                'dex':  8,
                'don': 15,
                'dnt':  8,
                'wis':  8,
                'cha': 15}},                     
        'sa':{
            'str_based':{
                'str': 15,
                'dex':  8,
                'don': 13,
                'int': 10,
                'wis': 12,
                'cha': 14},
            'dex_based':{
                'str':  8,
                'dex': 15,
                'con': 13,
                'int': 10,
                'wis': 12,
                'cha': 14},
            'cha_based':{
                'str': 14,
                'dex':  8,
                'con': 13,
                'int': 10,
                'wis': 12,
                'cha': 15}}}}                                    
ranger ={
    'pc_class': 'ranger',
    'hit_die':'d10',
    'primary_ability': ('dex', 'wisd'),
    'saving_throw_prof':['str', 'dex'],
    'arm_weap_prof':['light armor', 'medium armor', 'shields', 'simple weapons', 'martial weapons'],
    'ability_by_method':{
        'pb':{
            'dex_based':{
                'str':  8,
                'dex': 15,
                'con': 14,
                'int': 10,
                'wis': 15,
                'cha':  8},
            'str_based':{
                'str': 15,
                'dex': 14,
                'con': 14,
                'int':  8,
                'wis': 12,
                'cha':  8},
            'wis_based':{
                'str':  8,
                'dex': 14,
                'con': 14,
                'int':  8,
                'wis': 15,
                'cha': 12}},                     
        'sa':{
            'dex_based':{
                'str': 15,
                'dex':  8,
                'con': 13,
                'int': 10,
                'wis': 12,
                'cha': 14},
            'str_based':{
                'str':  8,
                'dex': 15,
                'con': 13,
                'int': 10,
                'wis': 12,
                'cha': 14},
            'wis_based':{
                'str': 14,
                'dex':  8,
                'con': 13,
                'int': 10,
                'wis': 12,
                'cha': 15}}}}                                
rogue ={
    'pc_class': 'rogue',
    'hit_die':'d8',
    'primary_ability': 'dex',
    'saving_throw_prof':['dex', 'int'],
    'arm_weap_prof':['light armor', 'simple weapons', 'hand crossbows', 'longswords', 'rapiers', 'shortswords'],
    'ability_by_method':{
        'pb':{
            'main':{
                'str':  8,
                'dex': 15,
                'con': 14,
                'int': 11,
                'wis': 12,
                'cha': 12},
            'arcane_trickster':{
                'str': 10,
                'dex': 15,
                'con': 14,
                'int': 14,
                'wis': 10,
                'cha': 10},                    
        'sa':{
            'main':{
                'str':  8,
                'dex': 15,
                'con': 14,
                'int': 10,
                'wis': 13,
                'cha': 12},
            'arcane_trickster':{
                'str':  8,
                'dex': 15,
                'con': 13,
                'int': 14,
                'wis': 12,
                'cha': 10}}}}}                                
sorcerer ={
    'pc_class': 'sorcerer',
    'hit_die':'d6',
    'primary_ability': 'cha',
    'saving_throw_prof':['con', 'cha'],
    'arm_weap_prof':['daggers', 'slings', 'quarterstaffs', 'light crossbows'],
    'ability_by_method':{
        'pb':{
             'str':  8,
             'dex': 14,
             'con': 14,
             'int': 10,
             'wis': 10,
             'cha': 15}, 
        'sa':{
             'str':  8,
             'dex': 13,
             'con': 14,
             'int': 12,
             'wis': 10,
             'cha': 15}}}
warlock ={
    'pc_class': 'warlock',
    'hit_die':'d8',
    'primary_ability': 'cha',
    'saving_throw_prof':['wis', 'cha'],
    'arm_weap_prof':['light armor', 'simple weapons'],
    'ability_by_method':{
        'pb':{
            'chain/talisman/tome':{
                'str':  8,
                'dex': 14,
                'con': 14,
                'int': 10,
                'wis': 10,
                'cha': 15},
            'blade':{
                'str': 10,
                'dex': 15,
                'con': 14,
                'int':  8,
                'wis':  8,
                'cha': 14},                    
        'sa':{
            'chain/talisman/tome':{
                'str':  8,
                'dex': 13,
                'con': 14,
                'int': 12,
                'wis': 10,
                'cha': 15},
            'blade':{
                'str': 10,
                'dex': 14,
                'con': 13,
                'int': 12,
                'wis':  8,
                'cha': 15}}}}}                     
wizard ={
    'pc_class': 'wizard',
    'hit_die':'d6',
    'primary_ability': 'int',
    'saving_throw_prof':['int', 'wis'],
    'arm_weap_prof':['daggers','darts', 'slings', 'quarterstaffs', 'light crossbows'],
    'ability_by_method':{
        'pb':{
            'str':  8,
            'dex': 14,
            'con': 14,
            'int': 15,
            'wis': 12,
            'cha':  8}, 
        'sa':{
            'str':  8,
            'dex': 13,
            'con': 14,
            'int': 15,
            'wis': 12,
            'cha': 10}}}