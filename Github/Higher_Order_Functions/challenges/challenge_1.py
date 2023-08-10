import module as m

#1
def list_country(country):
    return country
  
country_list = [list_country(country) for country in m.countries]
print(country_list)

#2
def name_list(name):
    return name

names_list = [name_list(name) for name in m.names]
print(names_list)

#3

def num_list(num):
    return num

number_list = [num_list(num) for num in m.numbers]
print(number_list)
