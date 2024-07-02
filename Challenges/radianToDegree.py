# Created by Bhushan Udupa at 1:59 PM 7/2/2024 using PyCharm

# Write a function in Python that accepts one numeric parameter.
# This parameter will be the measure of an angle in radians.
# The function should convert the radians into degrees and then return that value.


numInRadian = float(input("Enter a number in radian: "))
toDegree = numInRadian * (180 / 3.143)
print(str(numInRadian) + " radian in degree is: " + str(format(toDegree, ".2f")))

