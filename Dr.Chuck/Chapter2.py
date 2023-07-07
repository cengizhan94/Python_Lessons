import random
#Control Flow

"""num = random.randint(0,1)

if num > 0.5:
    print("Picture")
else:
    print("Tail")"""
    
#Grades Calculation
"""line = 55

study_grade = int(input("Study Grade: "))
if study_grade >= line:
    print("You Passed!")
else:
    print("You Failed!")"""

#pH Levels
ph = int(input("Enter a number between 0-14: "))
if ph >= 7:
    print("Basic!")
elif ph <= 7:
    print("Acidic!")
else:
    print("Natural.")

#The Cyclone 
height = int(input("What is your height?"))
credit = int(input("What is your credit?"))

if height >= 137 and credit >= 10:
    print("Enjoy the ride!")
elif height < 137:
    print("You are not tall enaugh to ride.")
elif credit < 10:
    print("You don't have enough credits.")
else:
    print("Invalid data.")