# Mini Exercise 1

# Ask for number input
number_input = input("Enter a number between (100–200): ")

# Add input validation
try:
    # Convert to Integer
    number = int(number_input)

    # Test input validation
except ValueError:
    print("Please input a valid number. Run the program again and enter a number.")
    exit()

# Result using multi-branch logic

if 100 <= number <= 200:
    print("In range")

else:
    print("Out of range")