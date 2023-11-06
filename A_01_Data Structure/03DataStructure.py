"""
Create a Series with the temperatures in degrees Celsius for a week. 
Convert the temperatures to degrees Fahrenheit (Fahrenheit = Celsius * 9/5 + 32
"""
import pandas as pd
tempretur = [33,35,28,36]

celcius = pd.Series(tempretur)

print(celcius)

# Convert Celsius temperatures to Fahrenheit
fahrenheit_temperatures = celcius * 9/5 + 32
print(fahrenheit_temperatures)

#or

for temp in celcius:
    Fahrenheit = temp * 9/5 + 32
    print(f"Fahrenheit {Fahrenheit} for Celcius Tempreture {temp}")