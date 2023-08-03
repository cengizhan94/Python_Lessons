class Circle:
    pi = 3.14
    
    def __init__(self, yaricap=1):
        self.yaricap = yaricap
    
    def calculate_circumference(self):
        return 2 * self.pi * self.yaricap
    
    def calculate_area(self):
        return self.pi * (self.yaricap ** 2)
    
circle = Circle()
circle2 = Circle(5)

print(f'c1 : area = {circle.calculate_area()} circumference: {circle.calculate_circumference()}')

print(f'c2 : area ={circle2.calculate_area()} circumference: {circle2.calculate_circumference()}')
    
    