dragonborn_black ={
    'race': 'dragonborn',
    'subrace': 'black',
    'ability_score_increase':{'str': 2, 'cha': 1},    
    'size': 'medium',
    'movement': 30,
    'vision': False,
    'languages':[('common', 'r_trait'), ('draconic', 'r_trait')],
    'black':{'damage type': 'acid', 'breath weapon':[5, 30], 'shape':'line', 'save': 'dex'}}

dragonborn_blue ={
    'race': 'dragonborn',
    'subrac': 'blue',
    'ability_score_increase':{'str': 2, 'cha': 1},    
    'size': 'medium',
    'movement': 30,
    'vision': False,
    'languages':[('common', 'r_trait'), ('draconic', 'r_trait')],
    'blue':{'damage type': 'lightning', 'breath weapon':[5, 30], 'shape': 'line', 'save': 'dex'}}

dragonborn_brass ={
    'race': 'dragonborn',
    'subrace': 'brass',
    'ability_score_increase':{'str': 2, 'cha': 1},    
    'size': 'medium',
    'movement': 30,
    'vision': False,
    'languages':[('common', 'r_trait'), ('draconic', 'r_trait')],
    'brass':{'damage type': 'fire', 'breath weapon': [5, 30], 'shape': 'line', 'save': 'dex'}}

dragonborn_bronze ={
    'race': 'dragonborn',
    'subrace': 'bronze',
    'ability_score_increase':{'str': 2, 'cha': 1},    
    'size': 'medium',
    'movement': 30,
    'vision': False,
    'languages':[('common', 'r_trait'), ('draconic', 'r_trait')],
    'bronze':{'damage type': 'lightning', 'breath weapon':[5, 30], 'shape': 'line', 'save': 'dex'}}

dragonborn_copper ={
    'race': 'dragonborn',
    'subrace': 'copper',
    'ability_score_increase':{'str': 2, 'cha': 1},    
    'size': 'medium',
    'movement': 30,
    'vision': False,
    'languages':[('common', 'r_trait'), ('draconic', 'r_trait')],
    'copper':{'damage type': 'acid', 'breath weapon':[5, 30], 'shape':'line', 'save': 'dex'}}

dragonborn_gold ={
    'race': 'dragonborn',
    'subrace': 'gold',
    'ability_score_increase':{'str': 2, 'cha': 1},    
    'size': 'medium',
    'movement': 30,
    'vision': False,
    'languages':[('common', 'r_trait'), ('draconic', 'r_trait')],
    'gold':{'damage type': 'fire', 'breath weapon':15, 'shape':'cone', 'save': 'dex'}}

dragonborn_green ={
    'race': 'dragonborn',
    'subrace': 'green',
    'ability_score_increase':{'str': 2, 'cha': 1},    
    'size': 'medium',
    'movement': 30,
    'vision': False,
    'languages':[('common', 'r_trait'), ('draconic', 'r_trait')],
    'green':{'damage type': 'poisin', 'breath weapon':15, 'shape':'cone', 'save': 'con'}}

dragonborn_red ={
    'race': 'dragonborn',
    'subrace': 'red',
    'ability_score_increase':{'str': 2, 'cha': 1},    
    'size': 'medium',
    'movement': 30,
    'vision': False,
    'languages':[('common', 'r_trait'), ('draconic', 'r_trait')],
    'red':{'damage type': 'fire', 'breath weapon':15, 'shape':'cone', 'save': 'dex'}}

dragonborn_silver ={
    'race': 'dragonborn',
    'subrace': 'silver',
    'ability_score_increase':{'str': 2, 'cha': 1},    
    'size': 'medium',
    'movement': 30,
    'vision': False,
    'languages':[('common', 'r_trait'), ('draconic', 'r_trait')],
    'silver':{'damage type': 'cold', 'breath weapon':15, 'shape':'cone', 'save': 'dex'}}

dragonborn_silver ={
    'race': 'dragonborn',
    'subrace': 'silver',
    'ability_score_increase':{'str': 2, 'cha': 1},    
    'size': 'medium',
    'movement': 30,
    'vision': False,
    'languages':[('common', 'r_trait'), ('draconic', 'r_trait')],
    'white':{'damage type': 'cold', 'breath weapon':15, 'shape':'cone', 'save': 'dex'}}

dwarf_hill ={
    'race': 'dwarf',
    'subrace': 'hill',
    'ability_score_increase':{'con': 2, 'wis':1},
    'size': 'medium',
    'movement': 25,
    'vision':{'darkvision': 60},
    'languages':[('common', 'r_trait'), ('dwarvish', 'r_trait')],
    'resistance':[('poisin', 'r_trait')],
    'proficiencies':[('battleaxe', 'r_trait'), ('handaxe', 'r_trait'), ('light hammer', 'r_trait'), ('warhammer', 'r_trait')],
    'proficiencies_optional': [('smiths tools', 'r_trait'), ('brewers supplies', 'r_trait'),  ('masons tools', 'r_trait')],
    'traits':{
        'ignore heavy armor speed reduction': True,
        'special notes': 'Stonecunning. Whenever you make an Intelligence (History) check related to the origin\
        of stonework, you are considered proficient in the History skill and add double your proficiency bonus\
        to the check, instead of your normal proficiency bonus.'},
    'special notes':{'hp':1* 'c_lvl'}}

dwarf_mountain ={
    'race': 'dwarf',
    'subrace': 'mountain',
    'ability_score_increase':{'con': 2, 'str': 2},
    'size': 'medium',
    'movement': 25,
    'vision':{'darkvision': 60},
    'languages':[('common', 'r_trait'), ('dwarvish', 'r_trait')],
    'resistance':[('poisin', 'r_trait')],
    'proficiencies':[('battleaxe', 'r_trait'), ('handaxe', 'r_trait'), ('light hammer', 'r_trait'), ('warhammer', 'r_trait'),
                    ('light armor', 'r_trait'),('medium armor', 'r_trait')],
    'proficiencies_optional': [('smiths tools', 'r_trait'), ('brewers supplies', 'r_trait'),  ('masons tools', 'r_trait')],
    'traits':{
        'ignore heavy armor speed reduction': True,
        'special notes': 'Stonecunning. Whenever you make an Intelligence (History) check related to the origin\
        of stonework, you are considered proficient in the History skill and add double your proficiency bonus\
        to the check, instead of your normal proficiency bonus.'}}

elf_dark ={
    'race': 'elf',
    'subrace': 'dark',
    'ability_score_increase':{'dex':2, 'cha': 1},
    'size': 'medium',
    'movement': 30,
    'vision':{'superior darkvision':120},
    'languages': [('common', 'r_trait'), ('elven', 'r_trait')],
    'advantage':[('charm', 'r_trait')],
    'immune':[('sleep', 'r_trait')],
    'proficiencies':[('perception', 'r_trait'),('rapiers', 'r_trait'), ('short swords', 'r_trait'),
                     ('hand crossbows', 'r_trait')],
    'spells':{
        'cantrip':[('dancing lights', 'r_trait')],
        'lvl 3':[({'spell':'faeire ', 'uses':1}, 'r_trait')],
        'lvl 5':[({'spell': 'darkness', 'uses':1}, 'r_trait')]},
    'traits':{
        'rest': 4},
    'special notes':{
        'Sunlight Sensitivity': 'You have disadvantage on attack rolls and Wisdom (Perception)\
            checks that rely on sight when you, the target of the attack, or whatever you are trying to perceive\
                is in direct sunlight.'}}

elf_high ={
    'race': 'elf',
    'subrace': 'high',
    'ability_score_increase':{'dex':2, 'int': 1},
    'size': 'medium',
    'movement': 30,
    'vision':{'darkvision': 60},
    'languages': [('common', 'r_trait'), ('elven', 'r_trait'),('single language of choice', 'r_trait')],
    'advantage':[('charm', 'r_trait')],
    'immune':[('sleep', 'r_trait')],
    'proficiencies':[('perception', 'r_trait'), ('longsword', 'r_trait'), ('shortsword', 'r_trait'), 
                    ('shortbow', 'r_trait'), ('longbow', 'r_trait')],
    'spells':{
        'spells':'1 wizard cantrip'},
    'traits':{
        'rest': 4}}

elf_wood ={
    'race': 'elf',
    'ability_score_increase':{'dex':2, 'wis':1},
    'size': 'medium',
    'movement': 35,
    'vision':{'darkvision': 60},
    'languages': [('common', 'r_trait'), ('elven', 'r_trait')],
    'advantage':[('charm', 'r_trait')],
    'immune':[('sleep', 'r_trait')],
    'proficiencies':[('perception', 'r_trait'), ('longsword', 'r_trait'), ('shortsword', 'r_trait'), 
                    ('shortbow', 'r_trait'), ('longbow', 'r_trait')],
    'traits':{
        'rest': 4},
    'speial_notes':{
        'hide': 'natural light coverage'}}
        
gnome_forrest ={
    'race': 'gnome',
    'subrace': 'forrest',
    'ability_score_increase':{'int':2, 'dex': 1},
    'size': 'small',
    'movement': 25,
    'vision':{'darkvision': 60},
    'languages':[('common', 'r_trait'), ('gnomish', 'r_trait')],
    'advantage':{'saves':[('magic','int'),('magic','wis'),('magic','cha')]},
    'spells':{'cantrip':'minor illusion'},
    'special notes':{
        'communicate with small beasts': 'Through sound and gestures, you may communicate\
            simple ideas with Small or smaller beasts.'}}

gnome_rock ={
    'race': 'gnome',
    'subrace': 'rock',
    'ability_score_increase':{'int':2, 'con':1},
    'size': 'small',
    'movement': 25,
    'vision':{'darkvision': 60},
    'languages':[('common', 'r_trait'), ('gnomish', 'r_trait')],
    'advantage':{'saves':[('magic','int'),('magic','wis'),('magic','cha')]},
    'spedial notes':{
        'artificers lore': 'Whenever you make an Intelligence (History) check related to magical, alchemical,\
            or technological items, you can add twice your proficiency bonus instead of any other proficiency bonus\
                that may apply.',
        'tinker': 'flavor to be added to engine later'}}

half_elf ={
    'race': 'half-elf',
    'size': 'medium',
    'movement': 30,
    'vision': {'darkvision':60},
    'ability_score_increase':{'cha':2, 'choice 1':1, 'choice 2': 1}}
