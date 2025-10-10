# A program to demonstrate multiple inheritance in Python

class Bird:
    def fly(self):
        print("A bird can fly.")

class Mammal:
    def run(self):
        print("A mammal can run.")

# A child class inheriting from both Bird and Mammal
class Bat(Bird, Mammal):
    def fly(self):
        print("A bat can fly using its wings.")

    def run(self):
        print("A bat can run on the ground.")

# Creating an instance of Bat and calling the methods
bat = Bat()
bat.fly()
bat.run()
