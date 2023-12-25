class Cat:
    name = None
    age = None
    isHappy = None

    def set_data(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy


cat1 = Cat()
cat1.set_data("Barsik", 3, True)

cat2 = Cat()
cat2.set_data("Joper", 3, True)

print(cat1.name)
print(cat2.name)