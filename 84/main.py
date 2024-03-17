# main.py
import my_module

# Использование функций из модуля
result_greet = my_module.greet("Иван")
print(result_greet)

side_length = 4
result_area = my_module.calculate_square_area(side_length)
print(f"Площадь квадрата со стороной {side_length}: {result_area}")
