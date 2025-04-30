# Function Mini Exercise 2

# Define function
def hourly_meal(time):

    # Result using multi-branch logic

    if 0 <= time <= 5:
        return "You should probably sleep."

    elif 6 <= time <= 10:
        return "Time for breakfast!"

    elif 11 <= time <= 14:
        return "It's lunchtime."

    elif 15 <= time <= 17:
        return "Maybe a light snack?"

    elif 18 <= time <= 21:
        return "Dinner time!"

    elif 22 <= time <= 23:
        return "Late night cravings?"

    return "Invalid time!"

# Ask for hour input
hour_input = input("Enter the current hour (0–23): ")

# Add input validation
try:
    # Convert to Integer
    time_in = int(hour_input)

    # Test input validation
except ValueError:
    print("Please input a valid hour in number. Run the program again and enter a number.")
    exit()

# Check input validation
if time_in < 0 or time_in > 23:
    print("Invalid time input. Please enter a valid hour between (0–23)")
    exit()

# Call function

choose_meal = hourly_meal(time_in)

# Print function
print(choose_meal)