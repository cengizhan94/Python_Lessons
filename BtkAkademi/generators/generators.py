# def cube():
#     for i in range(5):
#         yield i**3
#         # result.append(i ** 3)
        
# generator = cube()
# iterator = iter(generator)
# print(next(iterator))

generator = (i ** 3 for i in range(5))
print(generator)
print(next(generator))

for i in generator:
    print(i)