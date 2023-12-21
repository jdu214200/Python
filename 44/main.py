try:
    x = 5 / 0
    x = int(input())
except ZeroDivisionError:
    print("Deleniya na noll")
except ValueError:
    print("Vi veli chto to ne tak")
else:
    print("else")
finally:
    print("Finally")