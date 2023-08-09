#1- Declare a function add_two_numbers. It takes two parameters and it returns a sum
""" 
def add_two_numbers(num1,num2):
    return num1 + num2
print(add_two_numbers(20,30)) """


#2- Area of circle is calculaed as follows: area = pi*r*r. Write a function that calculates area_of_circle.
""" 
def area_of_circle(r):
    import math
    pi = math.pi
    area = pi * r * r
    return area
print(area_of_circle(5)) """
    

#3-Write a function called add_all_nums which takes arbitary  number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
""" 
def add_all_nums(*args):
    total = 0
    for num in args:
        if isinstance(num,(int,float)):
            total += num
        else:
            return "Error: Invalid args type."
    return total
print(add_all_nums(1,2,3,4,5,6,7,8,9,10)) """



#4- Temperature in celsius can be converted to fahrenheit using this formula: fahrenheit = (celcius * 9/5)+32. Write a function which converts celcius to fahrenheit, convert_celcius_to_fahrenheit
""" 
def convert_celcius_to_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5)+32
    return fahrenheit
print(convert_celcius_to_fahrenheit(39)) """

#5-Write a function called check_season, it takes a month parameter and returns the season: Autumn,Winter,Spring or Summer.
""" 
def check_season(month):
    months=[
    "JANUARY",
    "FEBRUARY",
    "MARCH",
    "APRİL",
    "MAY",
    "JUNE",
    "JULY",
    "AUGUST",
    "SEPTEMBER",
    "OCTOBER",
    "NOVEMBER",
    "DECEMBER"
    ]
    upMonth = month.upper()
    if upMonth in months:
        monthIndex = months.index(upMonth)       
        if monthIndex >= 2 and monthIndex <= 4:
            return "SPRİNG"
        elif monthIndex >= 5 and monthIndex <= 7:
            return "SUMMER"
        elif monthIndex >= 8 and monthIndex <= 10:
            return "AUTMN"
        else:
            return "WİNTER"
    else:
        return "Invalid month"
    
month = input("Which month are we in? ")
season = check_season(month)
print(f"The season is {season}") """

#6-
""" 
def calculate_slope(x1,y1,x2,y2):
    slope=(y2-y1)/(x2 - x1)
    return slope

slope = calculate_slope(1,2,3,4)
print("Slope",slope) """
#7
""" import math
def solve_quadratic_eqn(a,b,c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant))/(2*a)
        x2 = (-b - math.sqrt(discriminant))/(2*a)
        return x1,x2
    elif discriminant == 0:
        x1 = -b / (2*a)
        return x1,
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        x1_real = complex(real_part, imaginary_part)
        x2_real = complex(real_part, -imaginary_part)
        return x1_real, x2_real
    
solutions1 = solve_quadratic_eqn(1, -3, 2)
solutions2 = solve_quadratic_eqn(1, 2, 5)
solutions3 = solve_quadratic_eqn(1, -4, 4)

print("Solutions 1:", solutions1)
print("Solutions 2:", solutions2)
print("Solutions 3:", solutions3) """
#8
# nums = [1,2,3,4,5,6]

# def print_list(list):
#     for item in list:
#         print(item)
# print_list(nums)

#9-
# reverseNum = []
# def reverse_list(array):
#     for i in range(len(array)-1,-1,-1):
#         reverseNum.append(array[i])
#     return reverseNum      

# reversedResult = reverse_list(nums)
# print("Original:",nums)
# print("Reversed Array: ", reversedResult)

#10-Declare a functaion named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items.

items = ["a","b","c"]

def capitalized_items(liste):
    capitalized = []
    for item in liste:
            capitalized.append(item.upper())
    return capitalized

capitalized_list= capitalized_items(items)
print(capitalized_list)

#11- Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(input_list,new_item):
    updated_list = input_list.copy()#original list protected
    updated_list.append(new_item)
    return updated_list

original_list = [1,2,3]
new_item = 4
new_list = add_item(original_list,new_item)
print(add_item(original_list,"Cengo"))


# print("Original list: ", original_list)
# print("New List : ", new_list)
        
#-12 Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

def remove_item(input_list,item_to_remove):
    updated_list = []
    for item in input_list:
        if item != item_to_remove:
            updated_list.append(item)
    return updated_list

my_list = [1,2,3,4,5,6]
my_list2 = ["Cengo","Zeyno","Pervo","Zorro"]

item_to_remove = "Pervo"
updated_list = remove_item(my_list2,item_to_remove)

print("Liste: ",my_list2)
print("Updated List: ", updated_list)

#13-Declare a function named sum_of_numbers. It takes a number paramerter and it adds all the numbers in the range.
# def sum_of_numbers(number):
#     return number * (number + 1)//2

# result = sum_of_numbers(5)
# print(result)

# def sum_of_numbers(n):
#     return sum(range(1,n+1))

# result = sum_of_numbers(5)
# print("Sum of numbers from 1 to 5:", result) 

def sumnum(n):
    return sum(range(1, n + 1))

result = sumnum(100)
print(result)

#14-declare a function named sum_of_odds. It takes a number parameter and it adds all odd numbers in that range

def sum_of_odds (n):
    total_sum = 0
    for num in range(1, n+1):
        if num %2 != 0:
            total_sum += num
    return total_sum
    
result1 = sum_of_odds(100)
print(result1)

#15
def sum_of_evens (n):
    total_sum = 0
    for num in range(1, n+1):
        if num %2 == 0:
            total_sum += num
    return total_sum
    
result = sum_of_evens(100)
print(result)
    
    


    