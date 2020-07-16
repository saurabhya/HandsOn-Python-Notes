'''
   A complex number is created from real numbers. Python complex
   number can be created either using direct assignment statement or by using complex() function.

   Complex numbers which are mostly used where we are using two real numbers.
   For instance, an electric circuit which is defined by voltage(v)
   and current (c) are used is geometry, scientific calculations and calculus.
'''

# Creating a simple complex number 
c = 3 +6j
print(type(c)) # <class, 'complex'>
print(c)

# another way of assignment 
c1 = complex(3, 6)
print(type(c1)) # <class, 'complex'>
print(c1)

# complex numbers can also be created using strings
s = '3+6j'
c2 = complex(s)
print(type(c2)) # <class, 'complex'>
print(c2)


'''
    From above results, we can see python complex numbers are of type complex.
    Each complex number consist of one real and one imaginary part.
'''

print('Complex number: Real part is:', c.real)
print('Complex number: Imaginary part is:', c.imag)
print('Complex number: Conjugate part is:', c.conjugate())
