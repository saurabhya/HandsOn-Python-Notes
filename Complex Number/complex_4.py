"""
    Cmath module constants
        There are a couple of constants available in cmath module that are
        used in the complex number calculations:
"""
import cmath
print('pi =', cmath.pi)
print('e =', cmath.e)
print('tau =', cmath.tau)
print('Positive infinity =', cmath.inf)
print('Positive Complex infinity =', cmath.infj)
print('NaN =', cmath.nan)
print('NaN Complex =', cmath.nanj)

"""
    Power and Log Functions
        The cmath() module provides some useful functions for logarithmic
        and power operations.
"""
c = 1+2j
print('e^c = ', cmath.exp(c))
print('log2(c) = ', cmath.log(c,2))
print('log10(c) = ', cmath.log10(c))
print('sqrt(c) = ', cmath.sqrt(c))

"""
    Trigonometric Functions
"""
c = 2+4j
print('arc sine value:\n ', cmath.asin(c))
print('arc cosine value:\n ', cmath.acos(c))
print('arc tangent value:\n ', cmath.atan(c))
print('sine value:\n ', cmath.sin(c))
print('cosine value:\n ', cmath.cos(c))
print('tangent value:\n ', cmath.tan(c))

"""
    Hyperbolic Functions
"""
c = 2+4j
print('Inverse hyperbolic sine value: \n', cmath.asinh(c))
print('Inverse hyperbolic cosine value: \n', cmath.acosh(c))
print('Inverse hyperbolic tangent value: \n', cmath.atanh(c))
print('Inverse sine value: \n', cmath.sinh(c))
print('Inverse cosine value: \n', cmath.cosh(c))
print('Inverse tangent value: \n', cmath.tanh(c))