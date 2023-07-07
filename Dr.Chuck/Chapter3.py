#Loops
#Enter Pin
"""print("Welcome to Bank Of Technology")

pin = int(input('Enter your PIN: '))
while pin != 1234:
  pin = int(input('Incorrect PIN. Enter your PIN again: '))

if pin == 1234:
  print('PIN accepted!')"""
  
#Fizz Buzz
for i in range(1,101):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)