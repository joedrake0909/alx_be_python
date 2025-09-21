# Drawing Patterns with Nested Loops

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop for rows
while row < size:
    # Use for loop for columns
    for col in range(size):
        print("*", end="")
    # Move to next line after completing a row
    print()
    # Move to next row
    row += 1