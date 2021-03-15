import random

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