# Polymorphism with Duck Typing Instruction 

# In this example, we define three different classes: Dog, Cat, and Bird.

# Defining a Dog class
class Dog:
    def make_sound(self):
        print("Woof Woof!")

# Defining a Cat class
class Cat:
    def make_sound(self):
        print("Meow Meow!")


# Defining a Bird class
class Bird:
   def make_sound(self):
        print("Chirp Chirp!")


# Function demonstrating polymorphism using duck typing
def make_them_speak(animals):
    for animal in animals:
        animal.make_sound()

dog = Dog()
cat = Cat()
bird = Bird()

# List of different animal objects
animals = [dog, cat, bird]

# Calling the function with different animal objects
make_them_speak(animals)
