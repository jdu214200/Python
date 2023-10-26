x = 10


def add_to_x(y):
    x = 5
    x = x + y
    print(f'x внутри функции: {x}')


add_to_x(3)

print(f'x пределами функции {x}')