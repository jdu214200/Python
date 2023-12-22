try:
    file = open('text.txt', 'r')
    file.tead()
except FileNotFoundError:
    print("Fayl ne nayden")
