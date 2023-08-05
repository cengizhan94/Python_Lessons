""" 
try:
    x = int(input('x: '))
    y = int(input('y: '))
    print(x/y)
except (ZeroDivisionError, ValueError)as e:
    print("yanlis bilgi girdiniz")
    print(e) """
while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    except Exception as ex:
        print("yanlis bilgi girdiniz",ex)
    else:
        break
    finally:
        print("try except sonlandı")

    