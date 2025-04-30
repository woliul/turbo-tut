# Mini Exercise 2

# Ask for temperature input
temp_input = input("Enter a temperature: ")

# Add input validation
try:
    # Convert to Integer
    temperature = float(temp_input)

    # Test input validation
except ValueError:
    print("Please input a valid temperature in number. Run the program again and enter a temperature.")
    exit()

# Input Validation for below absolute zero (-273.15°C)
if temperature < -273.15:
    print("Invalid Temperature")
    exit()

# Result using multi-branch logic

if temperature < 0:
    print("Freezing cold!")

elif 0 <= temperature <= 20:
        print("Cold")

elif 21 <= temperature <= 30:
        print("Warm")

else:
    print("Hot!")
