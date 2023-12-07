# Author: Shachee SB, Pranav Parekh
# Date: 5th December 2023
# Description: Defines the field inhabitant i.e rabbit, veggie, captain

#A constructor that takes in a parameter representing a text symbol for the field inhabitant (vegetable, rabbit, captain, etc) and which assigns that value to a new member variable 
class FieldInhabitant:
    def __init__(self, symbol):
        self._symbol = symbol

    def get_symbol(self):
        return self._symbol

    def set_symbol(self, symbol):
        self._symbol = symbol


