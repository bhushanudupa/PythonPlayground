# Created by Bhushan Udupa at 1:59 PM 7/2/2024 using PyCharm

"""
 In python, immutability refers to the property of an object whose value cannot be
 changed after it is created.
 Immutable datatypes: Numbers(int, float, complex), Strings, Tuples, Frozen sets
"""

# # Example:
# x = 5   # 'x' is an integer, which is immutable
# y = x   # 'y' now refers to the same object as x
# x = 10  # This creates a new object with the value 10, and x now refers to that.
# print(x)
# print(y)

# Below code throws error as we are trying change its value
x = 'hello'
x[0] = "B"  # Here we are trying to set first character to 'B'
print(x)    # Throws "TypeError: 'str' object does not support item assignment" error.
