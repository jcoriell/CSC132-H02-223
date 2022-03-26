# List Comprehension

a_list = [x for x in range(0,10)]
print(a_list)

a_list = [2*x for x in range(0,10)]
print(a_list)


a_list_of_evens = [x for x in range(0,10) if x%2 ==0]
print(a_list_of_evens)

nesting = [(i,j) for i in range(0,2) for j in range(0,5)]
print(nesting)

more = [(i,j) for i in range(0,2) for j in range(0,5) if i%2 ==0 if j%2 != 0]
print(more)

# Could just execute code with it
[print('hello') for i in range(10)]
[print(value) for value in a_list_of_evens]

# Dictionary Comprehension
cubes = {x:x**3 for x in range(0,10)}
print(cubes)