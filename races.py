dragonborn ={
    'race': 'dragonborn',
    'size': 'medium',
    'movement': 30,
    'vision': False,
    'traits':{
        'ability score increase':{'str': 2, 'cha': 1},
        'languages':['common', 'draconic'],
        'sub-race':{
            'black':{'damage type': 'acid', 'breath weapon':[5, 30], 'shape':'line', 'save': 'dex'},
            'blue':{'damage type': 'lightning', 'breath weapon':[5, 30], 'shape': 'line', 'save': 'dex'},
            'brass':{'damage type': 'fire', 'breath weapon': [5, 30], 'shape': 'line', 'save': 'dex'},
            'bronze':{'damage type': 'lightning', 'breath weapon':[5, 30], 'shape': 'line', 'save': 'dex'},
            'copper':{'damage type': 'acid', 'breath weapon':[5, 30], 'shape':'line', 'save': 'dex'},
            'gold':{'damage type': 'fire', 'breath weapon':15, 'shape':'cone', 'save': 'dex'},
            'green':{'damage type': 'poisin', 'breath weapon':15, 'shape':'cone', 'save': 'con'},
            'red':{'damage type': 'fire', 'breath weapon':15, 'shape':'cone', 'save': 'dex'},
            'silver':{'damage type': 'cold', 'breath weapon':15, 'shape':'cone', 'save': 'dex'},
            'white':{'damage type': 'cold', 'breath weapon':15, 'shape':'cone', 'save': 'dex'}}}}
dwarf ={
    'race': 'dwarf',
    'size': 'medium',
    'movement': 25,
    'vision':{'darkvision': 60},
    'traits':{
        'ability score increase':{'con': 2},
        'ignore heavy armor speed reduction': True,
        'resistance':'poisin',
        'proficiencies':['battleaxe', 'handaxe', 'light hammer', 'warhammer',['smiths tools', 'brewers supplies',
                                                                         'masons tools']],
        'special notes': 'Stonecunning. Whenever you make an Intelligence (History) check related to the origin\
        of stonework, you are considered proficient in the History skill and add double your proficiency bonus\
        to the check, instead of your normal proficiency bonus.',
        'languages': ['common', 'dwarvish'],
        'sub-race':{
            'hill dwarf':{
                'ability score increase':{'wis':1},
                'special notes':{'hp':1* 'c_lvl'}},
            'mountain dwarf':{
                'ability score increase':{'str': 2}, 
                'special notes':{'proficiency':['light armor','medium armor']}}}}}
elf ={
    'race': 'elf',
    'size': 'medium',
    'movement': 30,
    'vision':{'darkvision': 60},
    'traits':{
        'ability score increase':{'dex':2},
        'advantage': 'charm',
        'imune': 'sleep',
        'rest': 4,
        'proficiencies': 'perception',
        'languages': ['common', 'elven'],
        'sub-race':{
            'dark elf':{
                'ability score increase':{'cha': 1},
                'vision':{'superior darkvision':120},
                'special notes':{'Sunlight Sensitivity': 'You have disadvantage on attack rolls and Wisdom (Perception)\
                checks that rely on sight when you, the target of the attack, or whatever you are trying to perceive\
                is in direct sunlight.',
                                'spells':{
                                    'cantrip':'dancing lights',
                                    'lvl 3':{'spell':'faeire ', 'uses':1},
                                    'lvl 5':{'spell': 'darkness', 'uses':1}},
                                'proficiencies': ['rapiers', 'short swords', 'hand crossbows']}},
            'high elf':{
                'ability score increase':{'int': 1},
                'special notes':{
                    'spells':'1 wizard cantrip',
                    'proficiencies':['longsword', 'shortsword', 'shortbow', 'longbow'],
                    'extra language':'single language of choice'}},
            'wood elf':{
                'ability score increase':{'wis':1},
                'special notes':{
                    'proficiencies':['longsword', 'shortsword', 'shortbow', 'longbow'],
                    'speed': 35,
                    'hide': 'natural light coverage'}}}}}
gnome ={
    'race': 'gnome',
    'size': 'small',
    'movement': 25,
    'vision':{'darkvision': 60},
    'traits':{
        'ability score increase':{'int':2},
        'advantage':{'saves':[('magic','int'),('magic','wis'),('magic','cha')]},
        'languages':['common', 'gnomish'],
        'sub-race':{
            'forrest gnome':{
                'ability score increase':{'dex': 1},
                'special notes':{
                'spells':{
                    'cantrip':'minor illusion'},
                'communicate with small beasts': 'Through sound and gestures, you may communicate\
                simple ideas with Small or smaller beasts.'}},
            'rock gnome':{
                'ability score increase': {'con':1},
                'spedial notes':{
                    'artificers lore': 'Whenever you make an Intelligence (History) check related to magical, alchemical,\
                    or technological items, you can add twice your proficiency bonus instead of any other proficiency bonus\
                    that may apply.',
                    'tinker': 'flavor to be added to engine later'}}}}}
half_elf ={
    'race': 'half-elf',
    'size': 'medium',
    'movement': 30,
    'vision': {'darkvision':60},
    'traits':{
        'ability score increase':{'cha':2, 'choice 1':1, 'choice 2': 1}
    }
}
