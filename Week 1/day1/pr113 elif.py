# Ask for age
age_input = input("Enter your age: ")

# Add input validation
try:
    # Convert to Integer
    age = int(age_input)

    # Test input validation
except ValueError:
    print("Please input valid number. Run the program again and enter a number.")
    exit()

# Result using multi-branch logic

if age < 1:
    print("Aww! You're just a baby!")

elif 1 <= age <= 12:
        print("You're a child.")

elif 13 <= age <= 17:
        print("You're a teenager.")

elif 18 <= age <= 59:
        print("You're an adult.")

else:
    print("You're a senior citizen.")