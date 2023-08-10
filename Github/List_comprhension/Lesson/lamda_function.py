# def add_two_numbers(a,b):
#     return a+b
# print(add_two_numbers(1,2))

# add_two_numbers = lambda a,b: a+b
# print(add_two_numbers(5,8))

# print((lambda a,b:a+b)(2,3))

# square = lambda x : x **2
# print(square(3))

# cube = lambda x : x **3
# print(cube(3))

#Lambda function inside another function

def power(x):
    return lambda n: x**n

cube = power(9)(2)
print(cube)