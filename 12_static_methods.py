"""
Question: 12 {Static Methods}
Assignment:
Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c)
that returns the Fahrenheit value.
"""


class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

f = TemperatureConverter() #  with object
print(f.celsius_to_fahrenheit(10))  

print(TemperatureConverter.celsius_to_fahrenheit(0)) # without object
