import math
"""
#calculate triangle area basic
base = float(input("Enter triangle base: "))
height = float(input("Enter triangle height: "))
triangleArea = 0.5 * base * height
print(triangleArea)

#perimeter of triangle basic
a = float(input("Enter triangle sight a :"))
b = float(input("Enter triangle sight b: "))
c = float(input("Enter triangle sight b: "))
perimter = a + b + c
print(perimter)

#rectangle
length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))
rectangleArea = length * width
perimeter = 2 * length + width

print(f"Rectangle area {rectangleArea} and  rectangle perimeter is {perimeter}")

#radius
radius = float(input("Enter circle radius: "))
circleArea = math.pi * radius * radius
circumference = 2 * math.pi * radius
print(f"Circle Area {circleArea} and circum ference {circumference}")

#slope
def calculate_slope(x1,y1,x2,y2):
    slope = (y2 - y1) / (x2 - x1)
    return slope

def calculate_distance(x1,y1,x2,y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

x1 = float(input("Enter points (x1):"))
y1 = float(input("Enter points (y1):"))
x2 = float(input("Enter points (x2):"))
y2 = float(input("Enter points (y2):"))

slope = calculate_slope(x1,y1,x2,y2)
print("Slope: ", slope)

distance = calculate_distance(x1,y1,x2,y2)
print("Euclidean Distance: ", distance)
"""
#11
def calculate_y(x):
    y = x ** 2 + 6 * x + 9
    return y

def find_zero_points():
    zero_points = []
    for x in range(-10,11):
        y = calculate_y(x)
        if y == 0:
            zero_points.append(x)
    return zero_points

zero_points = find_zero_points()
if zero_points:
    print("Values of x where y is 0: ",zero_points)
else:
    print("No values of x where y is 0 in the given range")
 