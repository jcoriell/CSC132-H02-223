
# Polymorphism: The idea of having multiple methods with the same name in 
# ## multiple classes (multiple interfaces).

# Method Lookup: Used to find the right method to call in a class hierarchy.


class Shape:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def draw(self):
        for _ in range(self.length):
            print('* ' * self.width)


class Rectangle(Shape):
    
    def __init__(self, length, width):
        Shape.__init__(self, length, width)


class Square(Shape):
    
    def __init__(self, length):
        Shape.__init__(self, length, length)


class Triangle(Shape):
    
    def __init__(self, length):
        Shape.__init__(self, length, length)

    def draw(self, space=False):
        for i in range(self.length):
            print('* ' * (self.width - i))
        
        if space:
            print()

r = Rectangle(3, 5)
r.draw()
t = Triangle(5)
t.draw(space=True)
t.draw()
