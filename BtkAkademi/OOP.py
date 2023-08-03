class Person:
    pass
    #attribute
    #methods
    def __init__(self,name,year):
        self.name = name
        self.year = year
    
    def intro(self):
        print("Hello World!")
        
    def calculateAge(self):
       return 2023 - self.year

#object (instance)     
person = Person("Cengiz Han",1994)
person2 = Person("Zeynep",2011)
person.intro()

print(f'age: {person.calculateAge()}')
print(f'p1 : name: {person.name} year: {person.year}')
       
