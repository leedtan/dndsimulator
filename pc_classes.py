pc_classes = {
'barbarian':{
    'hit_die':'d12',
    'primary_ability': 'str',
    'saving_throw_prof':['str', 'con'],
    'arm_&_wep_prof':['light armor', 'medium armor', 'shields', 'simple weapons', 'martial weapons'],
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
            'cha':12}}}, 
'bard':{
    'hit_die':'d8',
    'primary_ability': 'cha',
    'saving_throw_prof':['dex', 'cha'],
    'arm_&_wep_prof':['light armor', 'simple weapons', 'hand crossbows', 'long swords', 'rapiers', 'short swords'],
    'ability_x_method':{
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
            'cha': 15}}},
'cleric':{
    'hit_die':'d8',
    'primary_ability': 'wis',
    'saving_throw_prof':['wis', 'cha'],
    #'arm_&_wep_prof':['light armor', 'medium armor', 'shields', 'simple weapons', 'martial weapons'],
    'ability_x_method':{
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
                'cha': 10}}}},                     
'druid':{
    'hit_die':'d8',
    'primary_ability': 'wis',
    'saving_throw_prof':['int', 'wis'],
    #'arm_&_wep_prof':['light armor', 'medium armor', 'shields', 'simple weapons', 'martial weapons'],
    'ability_x_method':{
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
            'cha':  8}}},
'fighter':{
    'hit_die':'d10',
    'primary_ability': ['str','dex'],
    'saving_throw_prof':['str', 'con'],
    #'arm_&_wep_prof':['light armor', 'medium armor', 'shields', 'simple weapons', 'martial weapons'],
    'ability_x_method':{
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
                'cha': 12}}}},                                   
'monk':{
    'hit_die':'d8',
    'primary_ability': ('dex', 'wis'),
    'saving_throw_prof':['str', 'dex'],
    #'arm_&_wep_prof':['light armor', 'medium armor', 'shields', 'simple weapons', 'martial weapons'],
    'ability_x_method':{
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
            'cha':  8}}},
'paladin':{
    'hit_die':'d10',
    'primary_ability': ('str', 'cha'),
    'saving_throw_prof':['wis', 'cha'],
    #'arm_&_wep_prof':['light armor', 'medium armor', 'shields', 'simple weapons', 'martial weapons'],
    'ability_x_method':{
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
                'cha': 15}}}},                                          
'ranger':{
    'hit_die':'d10',
    'primary_ability': ('dex', 'wisd'),
    'saving_throw_prof':['str', 'dex'],
    #'arm_&_wep_prof':['light armor', 'medium armor', 'shields', 'simple weapons', 'martial weapons'],
    'ability_x_method':{
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
                'cha': 15}}}},                                  
'rogue':{
    'hit_die':'d8',
    'primary_ability': 'dex',
    'saving_throw_prof':['dex', 'int'],
    #'arm_&_wep_prof':['light armor', 'medium armor', 'shields', 'simple weapons', 'martial weapons'],
    'ability_x_method':{
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
                'cha': 10}}}}},                                  
'sorcerer':{
    'hit_die':'d6',
    'primary_ability': 'cha',
    'saving_throw_prof':['con', 'cha'],
    #'arm_&_wep_prof':['light armor', 'medium armor', 'shields', 'simple weapons', 'martial weapons'],
    'ability_x_method':{
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
             'cha': 15}}},
'warlock':{
    'hit_die':'d8',
    'primary_ability': 'cha',
    'saving_throw_prof':['wis', 'cha'],
    #'arm_&_wep_prof':['light armor', 'medium armor', 'shields', 'simple weapons', 'martial weapons'],
    'ability_x_method':{
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
                'cha': 15}}}}},                        
'wizard':{
    'hit_die':'d6',
    'primary_ability': 'int',
    'saving_throw_prof':['int', 'wis'],
    #'arm_&_wep_prof':['light armor', 'medium armor', 'shields', 'simple weapons', 'martial weapons'],
    'ability_x_method':{
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
            'cha': 10}}}}