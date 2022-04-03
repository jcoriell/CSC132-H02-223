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
        self._exits[exit] = room

    def add_item(self, item, desc):
        self._items[item] = desc

    def add_grabbable(self, item):
        self._grabbables.append(item)

    def del_grabbable(self, item):
        self._grabbables.remove(item)

    def __str__(self):
        result = f"You are in {self.name}\n"

        result += "You see: "
        for item in self.items.keys():
            result += item + " "
        result += "\n"

        result += "Exits: "
        for exit in self.exits.keys():
            result += exit + " "
        result += "\n"
        
        return result


class Game(Frame):

    EXIT_ACTIONS = ["quit", "exit", "bye", "adios"]
    STATUS_DEFAULT ="I don't understand. Try verb noun. Valid verbs are go, look, take."
    STATUS_DEAD = "You are dead."
    STATUS_BAD_EXIT = "Invalid Exit"

    STATUS_ROOM_CHANGE = "Room Changed."
    STATUS_GRABBED = "Item Grabbed."
    STATUS_BAD_GRABBABLE = "I can't grab that."
    STATUS_BAD_ITEM = "I don't see that."

    def __init__(self, parent):
        self.inventory = []
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=1)

    def create_rooms(self):
        # create the rooms
        r1 = Room("Room 1", "room1.gif")
        r2 = Room("Room 2", "room2.gif")
        r3 = Room("Room 3", "room3.gif")
        r4 = Room("Room 4", "room4.gif")

        # handle the exits
        r1.add_exit("east", r2)
        r1.add_exit("south", r3)

        r2.add_exit("west", r1)
        r2.add_exit("south", r4)

        r3.add_exit("east", r4)
        r3.add_exit("north", r1)

        r4.add_exit("north", r2)
        r4.add_exit("west", r3)
        r4.add_exit("south", None)  # None for death

        # handle items
        r1.add_item("chair", "It is made of wicker and no one is sitting on it.")
        r1.add_item("bigger_chair", "It is made of even more wicker and no one is sitting on it. But there is a key on it")

        r2.add_item("fireplace", "It is made of fire and fire is sitting on it. Grab some fire and bring it with you.")
        r2.add_item("chairs", "They are made of more wicker and no one is sitting on all of them. \
                                This might be a fire hazard. Is this a chair factory?")
        
        r3.add_item("desk", "It is made of wicker and no one is sitting on it.")
        r3.add_item("chair", "Yep. Another.")
        r3.add_item("dimsdale_dimmadome", "Owned by Doug Dimmadome, owner of the Dimsdale Dimmadome. That's right!")
        
        r4.add_item("croissant", "It is made of butter and no one is sitting on it. There is an extra stick of butter.")

        # handle grabbables
        r1.add_grabbable("key")
        r2.add_grabbable("fire")
        r3.add_grabbable("Doug")
        r4.add_grabbable("butter")

        # set the current room
        self.current_room = r1

    def setup_gui(self):
        # input element
        self.player_input = Entry(self, bg="white")
        self.player_input.bind("<Return>", self.process)
        self.player_input.pack(side=BOTTOM, fill=X)
        self.player_input.focus()       # sets input field to have cursor inside of it

        # the image element
        img = None
        self.image_container = Label(self, width=WIDTH // 2, image=img)
        self.image_container.image = img 
        self.image_container.pack(side=LEFT, fill=Y)
        self.image_container.pack_propagate(False) # prevents the image from controlling the size of the window

        # the text/status element
        text_container = Frame(self, width=WIDTH // 2)
        self.text = Text(text_container, bg="lightgrey", state=DISABLED)
        self.text.pack(fill=Y, expand=1)
        text_container.pack(side=RIGHT, fill=Y)
        text_container.pack_propagate(False)


    def set_room_image(self):
        if self.current_room == None:
            img = PhotoImage(file="skull.gif")
        else:
            img = PhotoImage(file=self.current_room.image)

        self.image_container.config(image=img)
        self.image_container.image = img


    def set_status(self, status):
        self.text.config(state=NORMAL)  # makes the text editable
        self.text.delete(1.0, END)  # deletes the characters from 1st spot to the end

        if self.current_room == None:
            self.text.insert(END, Game.STATUS_DEAD)
        
        else:
            content = f"{self.current_room}\nYou are carrying: {self.inventory}\n\n{status}"
            self.text.insert(END, content)
        
        self.text.config(state=DISABLED)


    def play(self):
        self.create_rooms()
        self.setup_gui()
        self.set_room_image()
        self.set_status("")

    def process(self, event):
        action = self.player_input.get() 
        action = action.lower()

        if action in Game.EXIT_ACTIONS:
            exit()
        
        if self.current_room == None:
            self.player_input.delete(0, END)
            return
        
        words = action.split()

        if len(words) != 2:
            self.set_status(Game.STATUS_DEFAULT)
            return
        
        self.player_input.delete(0, END)

        verb = words[0]
        noun = words[1]

        if verb == "go":
            status = Game.STATUS_BAD_EXIT

            if noun in self.current_room.exits:
                self.current_room = self.current_room.exits[noun]
                status = Game.STATUS_ROOM_CHANGE

            self.set_status(status)
            self.set_room_image()
            return

        if verb == "look":
            status = Game.STATUS_BAD_ITEM

            if noun in self.current_room.items: # items is a dictionary
                status = self.current_room.items[noun]

            self.set_status(status)
            return 

        if verb == "take":
            status = Game.STATUS_BAD_GRABBABLE

            if noun in self.current_room.grabbables: # grabbables is a list
                self.inventory.append(noun)
                self.current_room.del_grabbable(noun)
                status = Game.STATUS_GRABBED

            self.set_status(status)
            return


# Main Part

window = Tk()
window.title("Room Adventure Revolutions")
game = Game(window)
game.play()
window.mainloop()