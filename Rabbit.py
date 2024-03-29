# Author: Shachee SB, Pranav Parekh
# Date: 5th December 2023
# Description: This program defines the rabbit class

from Creature import Creature

# A constructor that takes in two values representing x and y coordinates
class Rabbit(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "R")
