'''
    Python cmath module
    It provides access to mathematical functions for complex numbers.
    Let's look at some of the important features of complex numbers using math module function.

    Phase of complex number
    The phase of a complex number is the angle between the real axis and
    the vector representing the imaginary part.
    The phase returned by math and cmath modules are in radians an dwe use the numpy.degrees()
    function to convert it to degrees.
'''
import cmath, numpy, math
c = 4+4j
# phase
phase = cmath.phase(c)
print('4+4j Phase = ',phase)
print('Phase in Degrees = ', numpy.degrees(phase))
print('-4-4j Phase = ', cmath.phase(-4-4j),'radians. Degrees =', numpy.degrees(cmath.phase(-4-4j)))

# We can get phase using math.atan2() functions too
print('Complex number phase using math.atan2() = ',math.atan2(2,1))