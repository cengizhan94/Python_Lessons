# listt = [1,2,3,4,5]

# iterator = iter(listt)
# print(next(iterator))

# for i in listt:
#     print(i)
    
# while True:
#     try:
#         element = next(iterator)
#         print(element)
#     except Exception as e:
#         print(e)
#         break

class MyNumbers:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration
        
liste = MyNumbers(10,20)
# for x in liste:
#     print(x)
myiter = iter(liste)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

    
while True:
    try:
        element = next(myiter)
        print(element)
    except Exception as e:
        print(e)
        break

        