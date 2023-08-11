try:
    name = input("Enter your name: ")
    year_born = int(input("Year you were born: "))
    age = 2023 - year_born
    print(f"You are {name}. And your age is {age}")
except Exception as e:
    print(e)

   
    
    
