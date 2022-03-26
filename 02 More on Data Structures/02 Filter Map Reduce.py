# Filter
# Define a function that returns a Boolean based on an input
# Pass the function through filter(func, list) to filter the items based
#### on the function

def is_even(x):
    if x % 2 == 0:
        return True
    else: 
        return False

a_list = [1, 2, 44, 6, 7, 3, 768]
items = filter(is_even, a_list)
filtered_list = list(items)
print(filtered_list)
print(a_list)

students = [
    {
        "first": "Josh",
        "age": 546789,
        "last" :"Coriell",
        "major": "CAM PhD",
        "hobbies": ["Games", "Piano", "Eating"],
        "has_face": True,
    },
    {
        "first": "Mona-Lisa",
        "age": 5,
        "last" :"Saperstein",
        "major": "Being the Worst",
        "hobbies": ["Asking for money"],
        "has_face": True,
    },
]

def is_old(student:dict):
    return student["age"] > 100

old_students = list(filter(is_old, students))
print(old_students)


# Map
# Define a function that manipulates an input. 
# Map returns the manipulated data

def double_it(x):
    return x * 2

data = [1,2,3,4,5,6,7,8]
doubled_values = list(map(double_it, data))
print(doubled_values)

def letter_writer(student:dict):
    result = f"Hi {student['first']},\n"
    result += f"I hear you are {student['age']} years old.\n"
    result += f"Congrats on graduating in {student['major']}\n"

    return result 

letters = list(map(letter_writer, students))
#print(letters)

for index, letter in enumerate(letters):
    file = open(f'{students[index]["last"]}.txt', 'w')
    file.write(letter)
    file.close()



# Reduce

from functools import reduce

def concatenate(x, y):
    return x + ' ' + y


a_list = ['hi', 'how', 'are', 'you']
reduced_thing = reduce(concatenate, a_list)
print(reduced_thing)






# git --version

# 1. Install git (google git for windows)
# 2. Create a github account
# 3. Some helpful vocab
    # Repos can be *cloned* from github to your local filesystem
    # A *commit* is a snapshot of your project at a specific time.
    # Commits must be *staged* first, then made
    # When your return you must *pull* changes


# 4. Problem solving and teamwork time
    # Form groups of 3ish.
    # Deliverables:
    # - have a repository on github, with each person as a collaborator
    # - each person should have a commit to the repository
