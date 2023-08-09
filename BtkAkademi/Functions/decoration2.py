import math
import time

def calculate_time(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print("fonksiyon "+func.__name__+" "+ str(finish - start)+" saniye sürdü")
    return wrapper
        
@calculate_time
def usalma(a,b):
    print(math.pow(a,b))
    
@calculate_time
def faktoriyel(num):
    print(math.factorial(num))


usalma(2,3)
faktoriyel(5)