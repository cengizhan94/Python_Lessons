#Functions with default parameters

def greetings (name = "Cengiz"):
    message = name + ", Welcome to Python for everyone!"
    return message
print(greetings())
print(greetings("Zeynep"))

def calculate_age(birth_year,current_year = 2023):
    age = current_year - birth_year
    return age
print("Age: ",calculate_age(1823))

def weight_of_object(mass,gravity=9.81):
    weight = str(mass * gravity)+"N"
    return weight
print("Weight of an object in Newtons: ", weight_of_object(100))
print("Weight of an object in Newtons: ", weight_of_object(100,1.62)) #gravity on the surface of the moon

    