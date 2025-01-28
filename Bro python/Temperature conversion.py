unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature:"))
if unit.lower() == 'c':
    temp = (temp*9/5+32)
    print(temp)
elif unit.upper() == 'F':
    temp = (temp-32)*5/9
    print(temp)
