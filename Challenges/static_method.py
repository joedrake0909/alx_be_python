# Static Method for Utility Calculations

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b
    

    @staticmethod
    def multiply(a , b):
        return a * b
    
# Example usage
result_add = Calculator.add(5 , 3)
result_multiply = Calculator.multiply(5 , 3)

print(f"Addition: {result_add}")
print(f"Multiplication: {result_multiply}")
