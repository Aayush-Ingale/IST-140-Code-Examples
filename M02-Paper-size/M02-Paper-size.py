#Write a program that displays the dimensions of a
# letter-size (8.5 × 11 inch) sheet of paper in
# millimeters. There are 25.4 millimeters per inch.
# Use constants and comments in your program


Width_IN_INCHES = #Enter integer value
HEIGHT_IN_INCHES = #Enter integer value
MILLIMETERS_PER_INCH = 25.4

widthInMilimeters = Width_IN_INCHES * MILLIMETERS_PER_INCH
heightINMilimeters = HEIGHT_IN_INCHES * MILLIMETERS_PER_INCH

print("Width:" , "%.2f" % widthInMilimeters, "mm")
print("Height:", "%.2f" % heightINMilimeters, "mm")