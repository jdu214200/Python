import math

def classifyAPoint(points, p, k=3):
    distance = []
    for group in points:
        for feature in points[group]:
            euclidean_distance = math.sqrt((feature[0] - p[0]) ** 2 + (feature[1] - p[1]) ** 2)

            distance.append((euclidean_distance, group))

    distance = sorted(distance)[:k]

    freq1 = 0  # frequency of group 0
    freq2 = 0  # frequency og group 1
    freq3 = 0  # frequency og group 2

    for d in distance:
        if d[1] == 0:
            freq1 += 1
        elif d[1] == 1:
            freq2 += 1
        elif d[1] == 2:
            freq3 += 1

    if freq1 > freq2 and freq1 > freq3:
        return 0
    elif freq2 > freq1 and freq2 > freq3:
        return 1
    elif freq3 > freq1 and freq3 > freq2:
        return 2


# driver function
def main():

    points = {0: [(1, 12), (2, 5), (3, 6), (3, 10), (3.5, 8), (2, 11), (2, 9), (1, 7)],
              1: [(5, 3), (3, 2), (1.5, 9), (7, 2), (6, 1), (3.8, 1), (5.6, 4), (4, 2), (2, 5)],
              2: [(2, 6), (2.3, 4), (7, 3), (6, 8), (3, 3), (4, 5), (2.9, 7.1), (4, 6.4), (4.6, 5.3)]
              }

    # testing point p(x,y)
    p = (4, 4)

    # Number of neighbours
    k = 3

    print("The value classified to unknown point is: {}". \
          format(classifyAPoint(points, p, k)))


if __name__ == '__main__':
    main()

# This code is contributed by Atul Kumar (www.fb.com/atul.kr.007)