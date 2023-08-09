def my_decorator(func):
    def wrapper(name):
        print("fonksiyondan onceki islemler")
        func(name)
        print("fonksiyondan sonraki işlemler")
    return wrapper

@my_decorator
def hello(name):
    print("Hello World",name)

@my_decorator
def greeting(name):
    print("greeting",name)
    
# hello = my_decorator(hello)
hello("Cengiz")
# greeting = my_decorator(greeting)
greeting("Zeynep")