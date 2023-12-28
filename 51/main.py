class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self, name, age, isHappy):
        self.set_data(name, age, isHappy)
        self.get_data()

    def set_data(self, name, age, isHappy):...

    def get_data(self):...


cat1 = Cat("Barsik", 3, True)
cat2 = Cat("Jopen", 2, False)
