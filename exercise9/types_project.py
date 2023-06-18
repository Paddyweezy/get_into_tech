first_name = 'Paddy'
last_name = 'Whelan'
print(first_name, last_name)
# two different ways create the same outcome
fullname = first_name + last_name
fullname_with_space = first_name + ' ' + last_name
print(fullname_with_space)


my_list = list(first_name + last_name)
print(my_list)

names_dictionary = {'Paddy': 'First', 'Whelan': 'Last'}
print(names_dictionary)
