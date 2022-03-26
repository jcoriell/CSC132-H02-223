# Name: Josh Coriell
# Date: Today! 
# Description: Room Adventure Revolutions

from tkinter import *

# Constants
WIDTH = 800
HEIGHT = 600


# Classes
class Room:
    
    def __init__(self, name, image):
        self.name = name
        self.image = image
        self.exits = {}
        self.items = {}
        self.grabbables = []

    # getters/setters
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value

    @property
    def exits(self):
        return self._exits

    @exits.setter
    def exits(self, value):
        self._exits = value

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, value):
        self._items = value

    @property
    def grabbables(self):
        return self._grabbables

    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    # additional methods
    def add_exit(self, exit, room):
        pass

    def add_item(self, item, desc):
        pass

    def add_grabbable(self, item):
        pass

    def del_grabbable(self, item):
        pass

    def __str__(self):
        pass


class Game(Frame):
    
    def __init__(self, parent):
        pass

    def create_rooms(self):
        pass

    def setup_gui(self):
        pass

    def set_room_image(self):
        pass

    def play(self):
        self.create_rooms()
        self.setup_gui()
        self.set_room_image()
        self.set_status("")

    def process(self, event):
        pass

# Main Part

window = Tk()
window.title("Room Adventure Revolutions")
game = Game(window)
game.play()
window.mainloop()