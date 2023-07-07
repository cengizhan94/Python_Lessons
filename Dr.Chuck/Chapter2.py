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
"""ph = int(input("Enter a number between 0-14: "))
if ph >= 7:
    print("Basic!")
elif ph <= 7:
    print("Acidic!")
else:
    print("Natural.")"""

#The Cyclone 
"""height = int(input("What is your height?"))
credit = int(input("What is your credit?"))

if height >= 137 and credit >= 10:
    print("Enjoy the ride!")
elif height < 137:
    print("You are not tall enaugh to ride.")
elif credit < 10:
    print("You don't have enough credits.")
else:
    print("Invalid data.")"""

#Sorting Hat
houses = {
    "Gryffindor" : 0,
    "Ravenclaw" : 0,
    "Hufflepuff" : 0,
    "Slytherin" : 0
}

question1 = int(input("Do you like Dawn or Dusk?\n 1) Dawn \n 2)Dusk "))
if question1 == 1:
    houses["Gryffindor"] += 1
    houses["Ravenclaw"] += 1
elif question1 == 2:
    houses["Hufflepuff"] += 1
    houses["Slytherin"]+= 1
else:
    print("Wrong answer. Please type 1 or 2.")

question2 = int(input("When I'm dead, I want people to remember me as: \n 1) The Good. \n 2) The Great \n 3) The Wise \n 4) The Bold"))

if question2 == 1:
    houses["Hufflepuff"] += 2
elif question2 == 2:
    houses["Slytherin"] += 2
elif question2 == 3:
    houses["Ravenclaw"] += 2
elif question2 == 4:
    houses["Gryffindor"] += 2
else:
    print("Wrong answer. Please type 1,2,3,4")

question3 = int(input("Wich kind of instrument most pleases your ear? \n 1) The violin \n 2) The trumpet \n 3) The piano \n 4) The drum"))

if question3 == 1:
    houses["Slytherin"] += 4
elif question3 == 2:
    houses["Hufflepuff"] += 4
elif question3 == 3:
    houses["Ravenclaw"] += 4
elif question3 == 4:
    houses["Gryffindor"] += 4
else:
    print("Wrong answer. Please type 1,2,3,4")

max_points = max(houses.values())
winning_house = [house for house, points in houses.items() if points == max_points]
print("Winning house: ". join(winning_house))


    