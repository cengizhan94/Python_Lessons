from collections import Counter
import module as m
import countries as c
from functools import reduce

#1-
# def change_upper(country):
#     return country.upper()

# country_to_upper = map(change_upper,m.countries)
# print(list(country_to_upper))

#2-map
# def square(num):
#     return num ** 2

# squared_num = map(square,m.numbers)
# print(list(squared_num))
#3-map

# def upper_name(name):
#     return name.upper()

# uppered_name = map(upper_name,m.names)
# print(list(uppered_name))

#4-filter
# def contain_land(country):
#     return "land" in country

# land_countries = list(filter(contain_land,m.countries))
# print(land_countries)
#5-filter
# def six_char_countries(country):
#     return len(country) == 6

# six_char_country=list(filter(six_char_countries,m.countries))
# print(six_char_country)
#6-filter
# def sixmore_char_countries(country):
#     return len(country) >= 6

# six_morechar_country=list(filter(sixmore_char_countries,m.countries))
# print(six_morechar_country)

#7-filter
# def starts_with_e(country):
#     return country.startswith('E')

# starts_e = list(filter(starts_with_e,m.countries))
# print(starts_e)

#8-reduce
# doubled_numbers = map(lambda x: x * 2, m.numbers)

# even_numbers = filter(lambda x: x % 2 == 0,doubled_numbers)

# sum_of_even_numbers = reduce(lambda x,y: x+y,even_numbers)

# print(sum_of_even_numbers)

#9-
# def get_string(input_list):
#     #isinstance(item,str)<look for only strings
#     string_list = filter(lambda item: isinstance(item,str), input_list)
#     return list(string_list)

# mixed_list=[1,"Cengiz",2.5,"Zeynep","Pervin",5]

# string_list = get_string(mixed_list)
# print(string_list)    

#10-
# def sum_all_numbers(x,y):
#     return int(x)+ int(y)

# total = reduce(sum_all_numbers,m.numbers)
# print(total)

#11-
# def concatenate_countries(sentence,country):
#     if sentence:
#         sentence += ", " + country
#     else:
#         sentence += country
#     return sentence

# result_sentence = reduce(concatenate_countries, m.countries, "")+ " are north European countries"
# print(result_sentence)

#12-
# def categorize_countries(pattern, country_list):
#     categorized_countries = [country for country in country_list if pattern in country]
#     return categorized_countries

# land_countries = categorize_countries("land",c.countries)
# print(land_countries)

#13-

def count_countries_by_starting_letter(country_list):
    starting_letters = [country[0].upper() for country in country_list]
    letter_count = Counter(starting_letters)
    return letter_count

starting_letter_count = count_countries_by_starting_letter(c.countries)

print(starting_letter_count)

#14-
def get_first_ten_countries():
    return c.countries[:10]

first_ten_countries = get_first_ten_countries()
print(first_ten_countries)
    
#15-
def get_last_ten_countries():
    return c.countries[-10:]

last_ten_countries = get_last_ten_countries()
print(last_ten_countries)

        
    



