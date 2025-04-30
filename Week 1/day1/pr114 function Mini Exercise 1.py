def check_age_cat(age):
    # Result using multi-branch logic
    if age < 1:
        return "Aww! You're just a baby!"

    elif 1 <= age <= 12:
        return "You're a child."

    elif 13 <= age <= 17:
        return "You're a teenager."

    elif 18 <= age <= 59:
        return "You're an adult."

    else:
        return "You're a senior citizen."


# Ask for age
age_in = input("Enter your age: ")

# Add input validation
try:
    # Convert to Integer
    age_input = int(age_in)

    # Test input validation
except ValueError:
    print("Please input valid number. Run the program again and enter a number.")
    exit()

age_cat = check_age_cat(age_input)
print(age_cat)

