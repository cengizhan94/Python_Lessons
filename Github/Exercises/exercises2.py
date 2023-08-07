class Person():
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        
class Student(Person):
    def __init__(self, firstName, lastName,studentNumber,classRoom,grade):
        super().__init__(firstName, lastName)
        self.studentNumber = studentNumber
        self.grade = grade
        self.classRoom = classRoom
    
    def welcome(self):
        print(f"Welcome {self.firstName} {self.lastName}. Your class is {self.classRoom} and your student number is {self.studentNumber}. Your grade is {self.grade}")
        

class Teacher(Person):
    def __init__(self, firstName, lastName,branch,salary):
        super().__init__(firstName, lastName)
        self.branch = branch
        self.salary = salary
    
    def welcome(self):
        print(f"welcome {self.firstName} {self.lastName} your branch is {self.branch} and your salary is {self.salary}")
    
class Worker(Person):
    def __init__(self, firstName, lastName,age,workSpace,year,salary):
        super().__init__(firstName, lastName)
        self.age = age
        self.workSpace = workSpace
        self.year = year
        self.salary = salary
        
    def welcome(self):
        print(f"Welcome {self.firstName} {self.lastName}. You are {self.age} years old and you working with us {self.year} year(s) as {self.workSpace}. Your salary is {self.salary}.")
        
 
 
 
teacher = Teacher("Cengiz Han","Uyar","Yazılım","25000")
student = Student("Zeynep","Uyar",63,"Müzik",100)
worker = Worker("Pervin","Oflaz",50,"Temizlik",10,11500)
   
print(teacher.welcome())
print(student.welcome())
print(worker.welcome())