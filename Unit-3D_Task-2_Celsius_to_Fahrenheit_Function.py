def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

celsius =float(input("enter temperture in celsius:"))
fahrenheit = celsius_to_fahrenheit(celsius)
print("Fahrenheit:", fahrenheit)