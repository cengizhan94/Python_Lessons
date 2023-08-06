#Arbitary number of arguments
#If we do not know the number of arguments we pass to our function, we can create a function which can take arbitary number of arguments by adding * before the parameter name

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(sum_all_nums(2,3,5))

#Default and arbitary number of parameters in functions
def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)
print(generate_groups("Team-1","Cengizhan","Zeynep","Pervin","Fatma"))

#Function as a parameter of another Function

def square_number(n):
    return n*n
def do_something(f,x):
    return f(x)
print(do_something(square_number,3))