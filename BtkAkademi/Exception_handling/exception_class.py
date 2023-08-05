class Person:
    def __init__(self,name,year):
        if len(name) > 10:
            raise Exception("name alanı 10 karakterden buyuk")
        else:
            self.name = name
        
p = Person("Cengiz Han Uyar",1994)  