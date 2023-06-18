output = open("pelican.txt", 'w')
output.write("A wonderful bird is the pelican", )
output.write("\n")
output.write("His beak can hold more than his belican. \n")
output.close()

lines = ["He can take in his beak, \n", "Enough food for a week. \n", "But i'm damned if I see how the helican. \n"]

with open("pelican.txt", "a") as file:
    file.writelines(lines)

