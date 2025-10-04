temperature = float(input("Enter the temperature in Celsius: "))

# Determine the category
if temperature < 20:
    print("It's Cold ❄️")
elif 20 <= temperature <= 30:
    print("It's Normal 🌤️")
else:
    print("It's Hot 🔥")
fahrenheit = (temperature * 9/5) + 32

# Display the result
print(f"{temperature}°C is equal to {fahrenheit}°F")

