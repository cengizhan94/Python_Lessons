
"""
from module import generate_full_name, sum_two_nums,person gravity

 print(generate_full_name("Cengiz Han", "Uyar"))
print(sum_two_nums(3,9)) 
 mass = 120
weight = mass * gravity
print(weight)
print(person["fname","lname"]) """


#Import Functions from a module and renaming:
from module import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g

print(fullname("Cengiz Han","Uyar"))
print(total(5,5))
mass = 100
weight = mass * g
print(weight)
print(p)
print(p['firstName'])

