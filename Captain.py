# Author: Shachee SB, Pranav Parekh
# Date: 5th December 2023
# Description: Sub class of Creature.

from Creature import Creature

class Captain(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "V")
        self._collected_veggies = []

    def add_veggie(self, veggie):
        self._collected_veggies.append(veggie)

    def get_collected_veggies(self):
        return self._collected_veggies
