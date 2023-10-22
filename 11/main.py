# youtube.com/@sudoteach
# Locals and Global variables
from time import time

start_time = time()

print("Global test...")

i = 0
while i < 50_000_000:
    i += 1

print("Done!")

end_time = time()

print(round(end_time - start_time, 3), 'seconds')
print()

def main():
    start_time2 = time()

    print("Local test...")

    i2 = 0
    while i2 < 50_000_000:
        i2 += 1

    print("Done!")

    end_time2 = time()

    print(round(end_time2 - start_time2, 3), 'seconds')
    print()


if __name__ == '__main__':
    main()