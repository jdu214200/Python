 # n = int(input())
 #
 # for i in range(n, 0, -1):
 #     print(i)


string = "I just recently started learning programing, ""and I'm already going through the topic of cyc""Thanks to the YouTube channel sudo teach thank"

counter = 1
for i in string:
    if i == ' ':
        counter += 1
print(counter)