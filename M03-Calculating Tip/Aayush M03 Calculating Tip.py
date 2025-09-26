print("Please use the following scale: ")
print("1. Totally Satisfied")
print("2. Satisfied")
print("3. Dissatisfied")
satisfactionInt= int(input("What was your level of satisfaction? "))
billAmount = float(input("What was your bill? "))

if satisfactionInt == 1:
    tip = billAmount * 0.2
    satisfactionLevel = "totally satisfied"
elif satisfactionInt == 2:
    tip = billAmount * 0.15
    satisfactionLevel = "satisfied"
else:
    tip = billAmount * 0.10
    satisfactionLevel = "dissatisfied"

print("Because you were", satisfactionLevel, "the tip amount is $%.2f" % tip)

