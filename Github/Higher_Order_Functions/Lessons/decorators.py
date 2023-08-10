def greeting():
    return "Welcome to Python"
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

g = uppercase_decorator(greeting)
print(g())

#<<<<<<<<<<<<--->>>>>>>>>>>>>>>>>>>>

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper


@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())

#Applying multiple decorators to a single function

#first decorator
def uppercse_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

#second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string_decorator
@uppercse_decorator
def greeting():
    return "Welcome Home"
print(greeting())

#Accepting parameters in decorator functions

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(param1,param2,param3):
        function(param1,param2,param3)
        print("I live in {}".format(param3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name,last_name,country):
    print("I am {} {}, I love to learn".format(first_name,last_name,country))

print_full_name("Cengiz Han","Uyar","Turkey")
        

