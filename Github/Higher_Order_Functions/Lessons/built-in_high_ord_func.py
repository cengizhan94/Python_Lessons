#Map function

numbers = [1,2,3,4,5]
# def square(x):
#     return x**2

# numbers_squared = map(square,numbers)
# print(list(numbers_squared))

# numbers_squared2 = map(lambda x : x **2,numbers)
# print(list(numbers_squared2))

# numbers_str = ["1","2","3","4","5"]
# numbers_int = map(int,numbers_str)
# print(list(numbers_int))

names = ["Cengiz Han","Zeynep","Pervin"]

# def change_to_upper(name):
#     return name.upper()

# names_upper_cased=map(change_to_upper,names)
# print(list(names_upper_cased))

# names_upper_cased2 = map(lambda name: name.upper(),names)
# print(list(names_upper_cased2))

#filter function

def is_even (num):
    if num %2==0:
        return True
    return False

even_numbers = filter(is_even,numbers)
print(list(even_numbers))

def is_odd(num):
    if num %2 != 0:
        return True
    return False

odd_numbers = filter(is_odd,numbers)
print(list(odd_numbers))

def is_name_long(name):
    if len(name)>7:
        return True
    return False

long_names = filter(is_name_long,names)
print(list(long_names))



