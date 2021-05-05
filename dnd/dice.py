import random

dice_avg = {
    'd4': 3,
    'd6': 4,
    'd8': 5,
    'd10': 6,
    'd12': 7,
    'd20': 11}

##A simple random number generator meant to be used to simulate dice rolls. Call and define the number of sides

class Dice:
    
    def __init__(self, num_sides = False):
        self.num_sides = num_sides
        pass
    
    def __is_int(self, string):
        try:
            if type(int(string)) is int:
                return True
        except:
            return False
        
    def __test_dice_snippets(self, string):
        d = string.find('d')
        if d < 0:
            return False
        elif d == 0:
            if self.__is_int(string[d+1:]):
                return int(string[d+1:])
            else:
                return False
        else:
            if self.__is_int(string[d+1:]):
                sides = int(string[d+1:])
                if self.__is_int(string[:d]):
                    num_to_roll = int(string[:d])
                    return [sides, num_to_roll]
            else:
                return False
    
    def roll(self, num_to_roll=1, num_sides= False):
        if num_sides == False:
            pass
        else:
            self.num_sides = num_sides
    ##Define the number of times to roll the dice. Defaults to one roll if not specified.
        if num_to_roll<1:
            return('No dice were rolled')
        elif num_to_roll==1:
            return random.randrange(1, self.num_sides + 1, 1)
        else:
            return sum([random.randrange(1, self.num_sides +1, 1) for i in range(num_to_roll)])
        
    def roll_from_string(self, string):
        value = self.__test_dice_snippets(string)
        if type(value) == list:
            dice = Dice(value[0])
            num_to_roll = value[1]
            return dice.roll(num_to_roll)
        elif type(value) == int:
            dice = Dice(value)
            return dice.roll()
        else:
            return False
            
class DiceBag(Dice):
    def __init__(self):
        self.d4 = Dice(4)
        self.d6 = Dice(6)
        self.d8 = Dice(8)
        self.d10 = Dice(10)
        self.d12 = Dice(12)
        self.d20 = Dice(20)
    def roll_advantage(self):
        return max([self.d20.roll() for i in range(2)])
    def roll_disadvantage(self):
        return min([self.d20.roll() for i in range(2)])
