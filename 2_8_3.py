###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# get temperatre in celsius from user input
Celsius=float(input("Enter temperature in Celsius: "))

# convert temperature to Kelvin, and to Fahrenheit
Kelvin=Celsius+273
Fahrenheit=Celsius*1.8+32

# printing the values to the console window
print(f"""
Temperature in Kelvin     :{Kelvin}
Temperature in Fahrenheit :{Fahrenheit}
""")