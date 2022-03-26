"""
Scenario: You're building an applicaiton for a Tire Center to model the different vehicles that are serviced.
The types of Vehicles the Tire Center services include Cars, Trucks, and Cycles. 
The types of Cycles the mechanic services include Bicycles and Motorcycles.
The mechanic cares about the the number of tires on each vehicle, 
who owns it, and whether or not the vehicle has an engine.

Create a python file that contains classes that model this.
Each class should contain a constructor and a way to print the objects specifications.
No need for getters and setters (but feel free to include them).
Repeat as little code as possible.
Example for printing a Bicycle: "Type: Bicycle; Owner: Josh; Engine: False; Tires: 2"

Be prepared to share.
"""

class Vehicle:
    

    def __init__(self, name):
        self.owner = name
        self.engine = None
        self.tires = None

    def __str__(self):
        return f"Owner: {self.owner}; Engine: {self.engine}; Tires: {self.tires}"


class Car(Vehicle):
    
    def __init__(self, name):
        Vehicle.__init__(self, name)
        self.engine = True
        self.tires = 4

    def __str__(self):
        return f"Type: Car; {super().__str__()}"

class Truck(Vehicle):
    
    def __init__(self, name):
        Vehicle.__init__(self, name)
        self.engine = True
        self.tires = 4

    def __str__(self):
        return f"Type: Truck; {super().__str__()}"


class Cycle(Vehicle):
    
    def __init__(self, name):
        Vehicle.__init__(self, name)
        self.tires = 2

    def __str__(self):
        return f"{super().__str__()}"


class Bicycle(Cycle):
    
    def __init__(self, name):
        Cycle.__init__(self, name)
        self.engine = False

    def __str__(self):
        return f"Type: Bicycle; {super().__str__()}"


class MotorCycle(Cycle):
    
    def __init__(self, name):
        Cycle.__init__(self, name)
        self.engine = True

    def __str__(self):
        return f"Type: Motorcycle; {super().__str__()}"


b1 = Bicycle("Josh")
print(b1)
