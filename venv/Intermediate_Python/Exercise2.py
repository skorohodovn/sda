class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return f"My name is {self._name} and my age is {self._age}"

    def make_a_sound(self):
        print("")

class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    @property
    def name(self):
        return f"My name is {self._name}, the dog. Im {self._age} years old"

    def make_a_sound(self):
        print("woof!")

class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    @property
    def name(self):
        return f"My name is {self._name}, the cat. Im {self._age} years old"

    def make_a_sound(self):
        print("mjau!")

d = Dog("Basar", 5)
d.make_a_sound()
print(d.name)
c = Cat("Nikolai", 4)
c.make_a_sound()
print(c.name)
