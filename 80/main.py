x = 5
y = 2
result = x + y * 3
print(result)


age = 18
if age >= 18:
    print("Вы совершеннолетний")
else:
    print("Вы несовершеннолетний")


score = 85
if score >= 90:
    print("Отлично!")
elif 80 <= score < 90:
    print("Хорошо")
else:
    print("Удовлетворительно")


fruits = ["яблоко", "груша", "апельсин"]
for fruit in fruits:
    print(fruit)


count = 0
while count < 5:
    print("Текущее значение:", count)
    count += 1
