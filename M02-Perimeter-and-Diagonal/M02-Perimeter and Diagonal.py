###
# Write a program that computes and displays the
# perimeter of a letter-size (8.5 × 11 inch) sheet
# of paper and the length of its diagonal.

from math import sqrt

WIDTH_IN_INCHES = #Enter value here either integer or float
HEIGHT_IN_INCHES = #Enter value here either integer or float

perimeter = 2 * WIDTH_IN_INCHES + 2 * HEIGHT_IN_INCHES
diagonal = sqrt(WIDTH_IN_INCHES ** 2 + HEIGHT_IN_INCHES ** 2)

print("Perimeter: ", "%.2f" % perimeter)
print("Diagonal: ", "%.2f" % diagonal)