word = 'Futboll, Basketbol, Volleboll'
# print(word.count('!'))
# print(word.upper())
# print(word.lower())
# print(word.capitalize())
# print(word.find('pr'))
hobby = word.split(', ')

for i in range(len(hobby)):
    hobby[i] = hobby[i].capitalize()

# print(hobby)
result = ", ".join(hobby)
print(result)