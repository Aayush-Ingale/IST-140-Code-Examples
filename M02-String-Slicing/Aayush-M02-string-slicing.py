##
#Write a program that prompts the user for a string and two integers,
#then prints a slice of the string using the two integers as the starting and end positions.
userString = input("Enter a string: ")
startingPosition = int(input("Enter a starting position: "))
endingPosition = int(input("Enter a ending position: "))

print("Here is the sliced string:",userString[startingPosition:endingPosition])
