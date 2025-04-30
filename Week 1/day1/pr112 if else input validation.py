# Ask for age
age_input = input("Enter your age: ")

# Add input validation
try:
    # Convert to Integer
    age = int(age_input)

    # Test input validation
except ValueError:
    print("Please input as number. Run the program again and enter a number.")
    exit()

# Result using conditionals

if age >=18:
    print("You are a Adult.")
else:
    print("You are a Minor.")