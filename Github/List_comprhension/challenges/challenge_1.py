#1 filter only negative and zero in the list using list comprehension

# numbers = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
# negative_numbers = [i for i in numbers if i <= 0]
# print(negative_numbers)

# #2 flatten the following list of lists of lists to a one dimensional list.
# list_of_lists = [[[1,2,3]],[[4,5,6]],[[7, 8, 9]]]

# dimensional_list = [number for row in list_of_lists for inner_list in row for number in inner_list]

# print(dimensional_list)

#3-Using list comprehension create the following list of tuples

# numbers = [
#     (i,1,i**2,i**3,i**4,i**5) 
#     for i in range(11)
#     ]
# print(numbers)

#Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_list = [(country.upper(), capital.upper()) for sublist in countries for country, capital in sublist]
print(new_list)

