class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f"{self.name} eats {food}.")

    def sleep(self, hours):
        print(f"{self.name} sleeps for {hours} hours.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} says: Woof!")

if __name__ == "__main__":
    a = Animal("Generic")
    a.eat("hay")
    a.sleep(4)

    d = Dog("Rex", "Labrador")
    d.eat("kibble")    # inherited
    d.sleep(6)         # inherited
    d.bark()           # Dog-specific
