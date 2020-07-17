'''
   Mathematical calculations on Complex numbers are similar to real numbers.
   Following simple mathematical calculations can be done with complex numbers.
'''
# First complex number
c1 = 3 + 6j
# Second complex number
c2 = 6 + 15j

# Addition
print("Addition of two complex numbers: ", c1+c2)

# Subtraction
print("Subtraction of two complex numbers: ", c1-c2)

# Multiplication
print("Multiplication of two complex numbers: ", c1*c2)

# Division
print("Division of two complex numbers: ", c1/c2)

'''
    However, complex numbers don't support comparison operators like
        <,>,<=,=> and it will through TypeError message:
'''

# c1<=c2  ------  Error
