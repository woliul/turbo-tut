# Multi parameter function example

# define function

def clothing_advice(temp, weather):
    # Multibranch input
    if temp < 10 and weather == "rainy":
        return "Wear a raincoat and warm clothes."

    elif temp < 10 and weather == "cold":
        return "Wear warm clothes."

    elif 10 <= temp <= 20 and weather == "sunny":
        return "Wear sunny clothes."

    elif 10 <= temp <= 20 and weather == "rainy":
        return "Wear a raincoat and light weight clothes."

    elif 21 <= temp <= 30 and weather == "sunny":
        return "Wear light weight clothes."

    elif 21 <= temp <= 30 and weather == "rainy":
        return "Wear a raincoat & light weight clothes."

    elif 21 <= temp <= 30 and weather == "cloudy":
        return "Wear light weight clothes & carry an umbrella or raincoat."

    else:
        return "No advice needed this combination. Dress comfortably!"

# Temperature input
temp_input = input("Enter the temperature (°C): ")

# Check temperature input validation
try:
    temp_in = float(temp_input)
except (
        ValueError):
        print("Invalid temperature input, Please enter a number")
        exit()

# Weather input
weather_input = input("Enter the weather (e.g., sunny, rainy, cold, or cloudy.): ")

# Check weather input validation
try:
    weather_in = weather_input.lower()
except (
        ValueError):
        print("Invalid weather input, Please enter sunny, rainy, cold, or cloudy.")
        exit()

# Call the function
advice = clothing_advice(temp_in, weather_in)

# Show result
print(advice)