#function as a parameter:
# def sum_numbers(nums):
#     return sum(nums)

# def higher_order_function(f,lst):
#     summation = f(lst)
#     return summation

# result = higher_order_function(sum_numbers, [1,2,3,4,5])
# print(result)

#Function as a return value

# def square(x):
#     return x ** 2

# def cube(x):
#     return x**3

# def absolute(x):
#     if x >= 0:
#         return x
#     else:
#         return -(x)

# def higher_order_function(type):
#     if type == "square":
#         return square
#     elif type == "cube":
#         return cube
#     elif type == "absolute":
#         return absolute
    
# result = higher_order_function("square")
# print(result(3))
# result = higher_order_function("cube")
# print(result(3))
# result = higher_order_function("absolute")
# print(result(-3))

def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))
print(closure_result(10))
