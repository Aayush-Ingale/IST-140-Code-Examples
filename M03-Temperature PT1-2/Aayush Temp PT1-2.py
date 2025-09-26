#Use these rules for Celsius:
#gas state: temp >100
#liquid state: temp >0

#Use these rules for Fahrenheit:
#gas state: temp > 212
#liquid state: temp > 32

#F to C conversion:
#C = (F-32) * 5/9

tempValue = float(input("Enter a temperature value: "))
Degrees = input("Is the Temp in F or C? ")

if Degrees == "F":
    tempValue = (tempValue - 32) * (5/9)

if tempValue > 100:
    print("Gas")
elif tempValue > 0:
    print("Liquid")
else:
    print("Solid")

# based on tempValue, print the appropriate state of water (gas, liquid, solid)

Altitude = int(input("Enter a altitude: "))
altitudeUnit = input("Is the Altitude measured in meters or Feet? ")

boilingPoint = 100 #Degrees Celsius

# for every 300 meters ( or 1000 feet ) boiling point of water drops by one degree celsius

if altitudeUnit == "Feet":
    newBoilingPoint = Altitude / 1000
else :
    newBoilingPoint = Altitude / 300

print("The boiling point is", newBoilingPoint)