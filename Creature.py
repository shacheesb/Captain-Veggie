# Author: Shachee SB, Pranav Parekh
# Date: 5th December 2023
# Description: Subclass of field inhabitant

from FieldInhabitant import FieldInhabitant

# A constructor that takes in two parameters representing x and y coordinates and one representing the symbol for that creature 
class Creature(FieldInhabitant):
    def __init__(self, x, y, symbol):
        super().__init__(symbol)
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, x):
        self._x = x

    def get_y(self):
        return self._y

    def set_y(self, y):
        self._y = y
