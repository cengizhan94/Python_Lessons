def announce(f):
    def wrapper():
        print("Hello World!")
        f()
        print("Hello Turkey!")
@announce
def hello(f):
    print("Hello Python!")

hello()