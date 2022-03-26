# Sets
# An unordered grouping of things. Duplicates can't exist.

a_set = {5, 10, 15, 15, 15, 15, 30, 15, 20}
print(a_set)

a_list = [1,2,3,4,5,6,7,6,6,6,6,6,6,6,8]
a_set = set(a_list)
print(a_set)

# union with |
print({1,2,3} | {3,4,5})

# intersection with &
print({1,2,3} & {3, 4, 5})

# difference with - 
print({1,2,3} - {2,3})


# Dictionaries
# Set of KEY:VALUE pairs

prof = {
    "first_name" : "Josh", 
    "last_name" : "Coriell",
    "stats": {
        "age": 75643567
    }
}

print(prof["first_name"])
his_first_name = prof["first_name"]
print(his_first_name)


# iterate over dictionaries
for key in prof:
    print(key)

for key in prof:
    print(prof[key])

for k,v in prof.items():
    print(k, v)

print("Josh" in prof)
print("age" in prof.keys())
print("Josh" in prof.values())

prof["stats"]["age"]

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

    },
]


