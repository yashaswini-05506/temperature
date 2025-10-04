temperature = float(input("Enter the temperature in Celsius: "))

# Determine the category
if temperature < 20:
    print("It's Cold ❄️")
elif 20 <= temperature <= 30:
    print("It's Normal 🌤️")
else:
    print("It's Hot 🔥")
