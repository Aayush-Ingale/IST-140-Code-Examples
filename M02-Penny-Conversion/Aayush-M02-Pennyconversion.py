###
# Convert pennies to dollars and cents. Create a variable, pennies, initialized with the value 1984. Then convert this amount to dollars (as an integer), along with the remaining number of cents. Display the output of both calculations. Then modify your code to also prompt the user for the number of pennies and then do the calculations.

pennies = # Enter an integer value here

dollars = pennies // 100
print("$",dollars)

cents = pennies % 100
print(cents, "₵")

print(pennies, "pennies equals", dollars, "dollars and", cents, "cents")

pennies = int(input('Enter a number of pennies: '))

dollars = pennies // 100
#whatever number is inserted, it will take the first digits (i.e 2025 the number 20 will be displayed along with print command below)
print("$", dollars)

cents = pennies %  100
#takes the last digits (i.e 2025 this time it will take the number 25 and display it with the following print command)
print(cents,"₵")

print(pennies, "pennies equals", dollars, "dollars and", cents, "cents")