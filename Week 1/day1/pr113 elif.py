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

elif age <= 1 or age<= 12:
        print("You're a child.")

elif age <= 13 or age<= 17:
        print("You're a teenager.")

elif age <= 18 or age<= 59:
        print("You're an adult.")

else:
    print("You're a senior citizen.")