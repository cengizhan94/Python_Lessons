languege = "Python"
lst = list(languege)
print(type(lst))
print(lst)

numbers = [i for i in range(11)]
print(numbers)

squares = [i * i for i in range(11)]
print(squares)

numbers2 = [(i,i * i)for i in range(11)]
print(numbers2)

even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)

odd_numbers = [i for i in range(21) if i %2 != 0]
print(odd_numbers)

numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in range(21)if i %2 == 0 and i > 0]
print(positive_even_numbers)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)