numbers = [5, 2, 7]
# numbers[3] = 100
numbers.append(100)
numbers.insert(1, True)

b = [5, 6, 8]
numbers.extend(b)
numbers.sort()

numbers.pop(0) #может удалить люобой цифру
numbers.remove(6) #можно выбрать значения

#number.clear()

#print(number.count(True))
print(len(numbers))