x = 0
while x == 0:
    try:
        x = int(input("Vedite chslo: "))
        x += 5
        print(x)
    except ValueError:
        print("Vedite luchshe chiso!")
