# Faça um program o qual converta uma temperatura (F) Farenheit para (C) Celsius.

f = float(input('Temperatura (F): '))
conversion = 5 * ((f - 32) / 9)

print(f'{conversion:.2f}°C')

