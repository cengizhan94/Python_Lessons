import math
#1- Declare a function named evens_and_odds. It takes a positive integer as parameter and it counts number of evens and odds in the number

# def evens_and_odds(start,end):
#     odd_numbers = []
#     even_numbers = []
#     odd_count = 0
#     even_count = 0
    
#     for num in range(start,end +1):
#         if num %2 == 0:
#             even_numbers.append(num)
#             even_count += 1
#         else:
#             odd_numbers.append(num)
#             odd_count += 1
#     return even_numbers, odd_numbers,even_count,odd_count

# start_num = int(input("Enter the start num: "))
# end_num = int(input("Enter the end num:"))

# even_numbers, odd_numbers,even_counts,odd_counts = evens_and_odds(start_num, end_num)

# print("Even Nums: ", even_numbers)
# print("Even Counts: ",even_counts)
# print("Odd Nums: ", odd_numbers)
# print("Odd Count: ",odd_counts)


#1/1 Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

# def factorial(number):
#     return math.factorial(number)
# number = int(input("Enter your number:"))

# factorialnum = factorial(number)
# print(factorialnum)

#1/2 Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(a):
    if not a:
        return True
    else:
        return False


user_input = input("write somethig")
isEmpty = is_empty(user_input)
if isEmpty:
    print("Data is empty")
else:
    print("Data is not empty")