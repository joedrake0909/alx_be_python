class Person:
    def __init__ (self, name, age):
        self.name =name
        self.age = age 

    @classmethod
    def create_class(cls, name):
        return cls(name, 0)
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Example usage
person1 = Person("Alice", 30)
person2 = Person.create_class("Bob")
person1.display_info()
person2.display_info()