class Person():
    def __init__(self,fname,lname):
        self.firstName = fname
        self.lastName = lname
        print("person created")
    
class Student(Person):
    def __init__(self,fname,lname,number):
        Person.__init__(self,fname,lname)
        self.stundentNumber = number
        print("Student Created")

class Teacher(Person):
    def __init__(self,fname,lname,branch):
        super().__init__(fname,lname)
        self.branch = branch
    

person = Person("Cengiz Han","Uyar")
student = Student("Zeynep","Uyar",323)
teacher = Teacher("Pervin","Oflaz","Matematik")

print(f'person: {person.firstName}')
print(f'student name: {student.firstName}, student last name: {student.lastName}, student number: {student.stundentNumber}') 
print(f'teacher name: {teacher.firstName}, last name: {teacher.lastName}, branch: {teacher.branch}')
       