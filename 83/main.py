# main.py
import my_module

result = my_module.greet("Иван")
print(result)

area = my_module.calculate_square_area(5)
print("Площадь квадрата:", area)

# main.py
import my_module as mm

result = mm.greet("Иван")
print(result)

area = mm.calculate_square_area(5)
print("Площадь квадрата:", area)

# main.py
from my_module import greet, calculate_square_area

result = greet("Иван")
print(result)

area = calculate_square_area(5)
print("Площадь квадрата:", area)
