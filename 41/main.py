
file = open('data/text.txt', 'r')

# print(file.read())

for line in file:
    print(line, end="")

file.close()