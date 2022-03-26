
try:
    print("Hello")
    1 + "h"
    print("How")
    print("are")
    print(you)
    print("doing")
except NameError:
    print("A name error occurred")
except TypeError:
    print("A type error occurred")
except:
    print("An error occurred")