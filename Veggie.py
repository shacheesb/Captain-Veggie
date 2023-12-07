# Author: Shachee SB, Pranav Parekh
# Date: 5th December 2023
# Description: Subclass of Field Inhabitant, contains the comma delimited information regarding the initial configuration of the 
game.

from FieldInhabitant import FieldInhabitant

class Veggie(FieldInhabitant):
    #private variables
    def __init__(self, name, symbol, points):
        super().__init__(symbol)
        self._name = name
        self._points = points
        
    def __str__(self): 
        return f"Symbol: {self.get_symbol()}, Name: {self._name}, Points: {self._points}"

    def get_name(self): #Appropriate getter setter functions
        return self._name

    def set_name(self, name):
        self._name = name

    def get_points(self):
        return self._points

    def set_points(self, points):
        self._points = points
