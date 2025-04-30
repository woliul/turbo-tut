# Multi parameter function example

# define function

def clothing_advice(temp, weather):
    # Multibranch input
    if temp < 10 and weather == "rainy":
        return "Wear a raincoat and warm clothes."

    elif temp < 20 and weather == "sunny":
        return "Wear a sunny clothes."

    elif temp < 20 and weather == "rainy":
        return "Wear a raincoat and light weight clothes."

    elif temp < 30 and weather == "cloudy":
        return "Wear a light weight clothes."

temp_input = input("Enter the temperature (°C): ")
weather_input = input("Enter the weather (e.g., sunny, rainy, snowy): ")

try:
    temp_in = float(temp_input)
except (
        ValueError):
        print("Invalid temperature input, Please enter a number")

