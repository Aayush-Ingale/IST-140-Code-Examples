firstName = input("Enter your first name: ")
middleName = input("Enter your middle name: ")
lastName = input("Enter your last name: ")
phoneNumber = input("Enter your phone number: ")

print(lastName, firstName, middleName)
firstNameLetter =  firstName[0]
middleNameLetter = middleName[0]
lastNameLetter = lastName[0]

lastDigits = phoneNumber[6:10]
print(lastDigits)

userID = firstNameLetter + middleNameLetter + lastNameLetter + lastDigits
print(userID)