# data = set('Hello')
data = {5, 7, 4, 3, 5}

data.add(32)
data.update(['32', True, 4, 5])
data.remove(True)
data.pop()
# data.clear()

nums = [5, 7, 3, 5, 5]
new_nums = set(nums)

new_data = frozenset([5, 7, 4, '32', True, 4, 6, 5, 7, 4, 3, 5])
# print(data)
print(new_data)
