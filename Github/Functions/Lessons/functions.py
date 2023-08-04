""" def generate_full_name():
    first_name = "Cengiz Han"
    last_name = "Uyar"
    space = " "
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name()

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()

#function returning a value - part 1
#Function can also return values, if a function does not have a return statement, the value of the function is None. Let us rewrite the above functions using return. From now on, we get a value fom a function when we call the function and print it.

def generate_full_name():
    first_name = "Cengiz Han"
    last_name = "Uyar"
    space = " "
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total

print(add_two_numbers())

#Function with parameters
#Single Parameter:
def greetings (name):
    message = name + ", welcome to python for everyone!"
    return message
print(greetings("Cengiz Han"))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle(r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total += i
    print(total)
print(sum_of_numbers(10))
print(sum_of_numbers(100))

#Two Parameter:

def generate_full_name(first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name("Cengiz Han","Uyar"))

def sum_two_numbers(num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1,9))

def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N'
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100,9.81))

#Passing Arguments with Key and Value
#If we pass the arguments with key and value, the order of the arguments does not matter.

def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname + space + lastname
    print(full_name)
print(print_fullname(firstname = 'Cengiz Han', lastname = 'Uyar'))

def add_two_numbers(num1, num2):
    total = num1 + num2
    print(total)
print(add_two_numbers(num2 = 3, num1 = 2)) """

#Function Returning a Value - part 2

""" If we do not return a value with a  function, then our function is returning  None by default. To return a value with a function we use the keyword return followed by the variable we are returning. We can return any kind of data types from a function """

#Returning string
def print_name(firstname):
    return firstname

print_name('Cengiz Han')

def print_full_name(firstName,lastName):
    space = " "
    full_name = firstName + space + lastName
    return full_name

print_full_name(firstName="Cengiz Han", lastName="Uyar") 