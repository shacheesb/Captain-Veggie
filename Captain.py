# Author: Shachee SB, Pranav Parekh
# Date: 5th December 2023
# Description: Sub class of Creature.

from Creature import Creature
# A constructor that takes in two integer values representing x and y coordinates 
class Captain(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "V")
        self._collected_veggies = []
# A function that takes in a Veggie object as a parameter, returns nothing, and adds the object to the List of Veggie objects 
    def add_veggie(self, veggie):
        self._collected_veggies.append(veggie)

    def get_collected_veggies(self):
        return self._collected_veggies
