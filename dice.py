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
    
    def __init__(self, num_sides):
        self.num_sides = num_sides


    def roll(self, num_to_roll=1):
##Define the number of times to roll the dice. Defaults to one roll if not specified.
        if num_to_roll<1:
            return('No dice were rolled')
        elif num_to_roll==1:
            return random.randrange(1, self.num_sides + 1, 1)
        else:
            return sum([random.randrange(1, self.num_sides +1, 1) for i in range(num_to_roll)])

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
