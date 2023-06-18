# What is wrong with this?
cheese = ["Cheddar", "Stilton", "Cornish Yarg"]
cheese += "Oke"
print(cheese)
# ['Cheddar', 'Stilton', 'Cornish Yarg', 'O', 'k', 'e'] - += adds the letters separately not as a complete string.

# This is how is should be done
cheese = ["Cheddar", "Stilton", "Cornish Yarg"]
cheese += ["Oke"]
print(cheese)
# [] required to wrap around string to make it valid. they are used to access data within a string, list or tuple.

# How to add teo new cheeses to the list with a single command?
cheese = ["Cheddar", "Stilton", "Cornish Yarg"]
cheese += ["Oke", "Red Leicester"]
print(cheese)