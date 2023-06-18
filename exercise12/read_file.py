output = open("pelican.txt", "r")
with open("pelican.txt", "r") as infile:
    for line in infile:
        print(line, end="")

# The line with open("pelican.txt", "r") as infile: is a common way to open a file named "pelican.txt" in read mode ("r") using a with statement. The with statement ensures that the file is properly closed after it's no longer needed, even if an exception occurs during the execution.

with open("pelican.txt", "r") as infile:
    file_contents = infile.readlines()

num_items = len(file_contents)
print("Number of items in the list:", num_items)
