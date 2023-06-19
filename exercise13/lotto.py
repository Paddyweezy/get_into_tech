# write a script that will generate and display 6 random lottery numbers between 1 and 50. Think about which python
# # data structure is best to store the numbers. Use the python help() function to find out which function to use
# usefrom the python standard library called random

import random

# lotto_numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18',
#                  '19', '20', '21', '22', '23', '24', '25', '26', '27', '29', '30', '31', '32', '33', '34', '35', '36',
#                  '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50')

random_six = random.sample(range(1, 51), 6)
print(random_six)

# this is all you need

# quicker way to achieve the same thing - work smarter not harder.

# lotto_numbers2 = list(range(1, 51)) #this create a data range from 1 to 50
# random_six2 = random.sample(lotto_numbers2, 6) #
# print(random_six2)