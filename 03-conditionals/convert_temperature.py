# Eighth program: convert a temperature between Celsius and Fahrenheit.

temperature = float(input('Enter the temperature you want to convert: '))
target_unit = int(input('Choose the unit to convert to ([0] Celsius  [1] Fahrenheit): '))

if target_unit == 0:
    converted_temperature = (temperature - 32) / 1.8
    print(f'{temperature}°F is equal to {converted_temperature:.2f}°C')
elif target_unit == 1:
    converted_temperature = (temperature * 1.8) + 32
    print(f'{temperature}°C is equal to {converted_temperature:.2f}°F')
else:
    print(f'The option {target_unit} is not valid.')
