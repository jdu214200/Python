login = input()

if login == 'admin':
    print('Логин введен верно!')
    password = input()
    if password == '123':
        print('Пароль введен верно!')
    else:
        print('Пароль введен неверно!')
else:
    print('Логин введен неверно!')