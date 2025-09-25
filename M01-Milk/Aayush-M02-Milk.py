######
#Convert the following pseudocode into Python:
#Prompt for the number of ounces of milk
#Compute the number of omelettes that can be made (4 ounces of milk per omelette)
#Use modulus division to determine the ounces of milk remaining
#Output the total number of omelettes that can be made
#Output the number of ounces remaining

Milk = int(input("Enter the number of ounces of milk: "))

Omlettes = Milk // 4
print(Omlettes)

leftover = Milk % 4

print(Milk, "ounces of milk will give us", Omlettes, "omlettes")
print("We will have", leftover, "ounces of milk left over")
