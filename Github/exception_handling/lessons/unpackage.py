#packing and unpacking arguments in python
#unpacking
def sum_of_five_nums(a,b,c,d,e):
    return a+b+c+d+e

lst=[1,2,3,4,5]
# print(sum_of_five_nums(lst))
print(sum_of_five_nums(*lst)) #unpackage

numbers = range(2,7)
print(list(numbers))
args=[2,7]
numbers= range(*args)
print(numbers)

countries = ['Turkey', 'Sweden', 'Norway', 'Denmark', 'Iceland']

tr,sw,nor,*rest = countries
print(tr,sw,nor,rest)

numbers2=[1,2,3,4,5,6]
one,*middle,last = numbers2
print(one,middle,last)

#unpacking dictionaries

def unpacking_person_info(name,country,city,age):
    return f"{name} lives in {country},{city}. He/She {age} years old."
dct = {"name":"Cengiz Han","coundstry":"Turkey","city":"Tokat","age":29}
print(unpacking_person_info(**dct))
