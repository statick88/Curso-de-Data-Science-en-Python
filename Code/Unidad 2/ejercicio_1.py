def celsius_to_fahrenheit(temp_celsius):
    temp_fahrenheit = (temp_celsius * 1.8) + 32
    return temp_fahrenheit

temp_celsius = float(input("Introduce una temperatura en grados Celsius: "))
temp_fahrenheit = celsius_to_fahrenheit(temp_celsius)
print(f"{temp_celsius} grados Celsius son {temp_fahrenheit} grados Fahrenheit.")
