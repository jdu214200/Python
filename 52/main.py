class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self, name=None, age=None, isHappy=None):
        self.set_data(name, age, isHappy)
        self.get_data()

    def set_data(self, name = None, age = None, isHappy = None):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):


cat1 = Cat


cat2 = Cat("Jopen", 2, False)