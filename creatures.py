creature_keys = ['race', 'size', 'abilities', 'hp', 'alt_hp', 'ac', 'actions', 'bonus_actions', 'skills', 'traits',
                'features', 'initiative_bonus', 'initiative', 'inventory', 'vision', 'movement', 'main_hand', 'off_hand',
                'armor', 'disposition', 'suprise', 'advantage', 'disadvantage']



aarakocra = {'race':'aarakocra', 'abilities':{'str':10, 'dex':14, 'con':10, 'int':11, 'wis': 12, 'cha':11},'hp':13, 'alt_hp':[8, 3], 'ac': 12, 
        'actions':['attack', 'cast', 'dash', 'disengage', 'dodge', 'help', 'hide','ready', 'search', 'use an object', 
                   'improvise'],
        'bonus_actions': {}, 'skills': False, 'action_count': 0, 'b_action_count': 0, 'reaction_count': 0, 'feats':{},
        'traits':{}, 'initiative': 2, 
        'inventory':{}, 'vision': False, 'movement':{'walking': 20, 'flight': 50, 'swimming': False,'climbing': False}, 
        'main_hand': False, 'off_hand': False, 'armor': False,'disposition':'indifferent'}