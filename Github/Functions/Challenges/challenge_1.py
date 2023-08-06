#1- Declare a function add_two_numbers. It takes two parameters and it returns a sum

def add_two_numbers(num1,num2):
    return num1 + num2
print(add_two_numbers(20,30))


#2- Area of circle is calculaed as follows: area = pi*r*r. Write a function that calculates area_of_circle.

def area_of_circle(r):
    import math
    pi = math.pi
    area = pi * r * r
    return area
print(area_of_circle(5))
    

#3-Write a function called add_all_nums which takes arbitary  number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*args):
    total = 0
    for num in args:
        if isinstance(num,(int,float)):
            total += num
        else:
            return "Error: Invalid args type."
    return total
print(add_all_nums(1,2,3,4,5,6,7,8,9,10))



#4- Temperature in celsius can be converted to fahrenheit using this formula: fahrenheit = (celcius * 9/5)+32. Write a function which converts celcius to fahrenheit, convert_celcius_to_fahrenheit

def convert_celcius_to_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5)+32
    return fahrenheit
print(convert_celcius_to_fahrenheit(39))

#5-Write a function called check_season, it takes a month parameter and returns the season: Autumn,Winter,Spring or Summer.

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
print(f"The season is {season}")
    


    