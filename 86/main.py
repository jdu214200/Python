# Списки
my_list = [1, 3, 5, 7, 9]

# Кортежи
my_tuple = (2, 4, 6, 8, 10)

# Словари
my_dict = {'apple': 3, 'banana': 5, 'orange': 2, 'grape': 7}

# Функция для удвоения чисел в списке
def double_numbers(numbers):
    return [number * 2 for number in numbers]

# Функция для проверки четности чисел в кортеже
def is_even_numbers(numbers):
    return tuple(number % 2 == 0 for number in numbers)

# Функция для увеличения количества фруктов в словаре
def increase_fruit_quantity(fruit_dict):
    return {fruit: quantity + 1 for fruit, quantity in fruit_dict.items()}

# Использование функций
doubled_list = double_numbers(my_list)
even_tuple = is_even_numbers(my_tuple)
increased_dict = increase_fruit_quantity(my_dict)

# Вывод результатов
print("Удвоенные числа в списке:", doubled_list)
print("Проверка четности чисел в кортеже:", even_tuple)
print("Увеличенное количество фруктов в словаре:", increased_dict)
