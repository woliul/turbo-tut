# Ask for hour input
time_input = input("Enter the current hour (0–23): ")

# Add input validation
try:
    # Convert to Integer
    time = int(time_input)

    # Test input validation
except ValueError:
    print("Please input a valid hour in number. Run the program again and enter a number.")
    exit()

# Result using multi-branch logic

if 0 <= time <= 5:
    print("You should probably sleep.")

elif 6 <= time <= 10:
        print("Time for breakfast!")

elif 11 <= time <= 14:
        print("It's lunchtime.")

elif 15 <= time <= 17:
        print("Maybe a light snack?")

elif 18 <= time <= 21:
        print("Dinner time!")

elif 22 <= time <= 23:
        print("Late night cravings?")

else:
    print("Invalid time. Please enter a valid hour (0–23)")