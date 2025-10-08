import gc  # Garbage collection interface

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print(f"Goodbye, {self.name}. You were {self.age} years old.")
    
if __name__ == "__main__":
    p = Person("Joseph", 20)
    print(f"Created person: {p.name}, {p.age}")

    del p  # Explicitly delete the object
    gc.collect()  # Force garbage collection to ensure __del__ is called
