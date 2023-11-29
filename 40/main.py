def minimal(l):
    min_number = l[0]
    for el in l:
        if el < min_number:
          min_number = el

    # print(min_number)
    return min_number

nums1 = [4, 5, 2, 6, 9]
min1 = minimal(nums1)

nums2 = [2.4, 4.6, 6.8, 8.2, 3.7]
min2 = minimal(nums2)

if min1 < min2:
    print(min1)
else:
    print(min2)

