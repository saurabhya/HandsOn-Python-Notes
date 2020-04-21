"""
    Here we will see implementation of some well known algorithmic problem's solution
    in a single line using Lambda functions.
    Lamnda function has great powers if used corretly and we will witness it as
    we go through different problems. These are well known problems or will be understandable
    just by the names, so will not be going throug the explanation of the problem
    but our focus will be on the use of lambda function.
"""

# Finding Anagrams
# return True if give strings are anagrams else retur False

is_anagram = lambda x1, x2: sorted(x1) == sorted(x2)

# Now check for the result.
print("Output of is_anagram function: ")
print(is_anagram("elvis", "lives"))
print(is_anagram("elvis", "data"))


print("\n")

# Finding Palindromes
# return True if given string is a palindrome or not.

is_palindrome = lambda x: x == x[::-1]

# Now check for the result
print("Output of is_palindrome function: ")
print(is_palindrome("anna"))
print(is_palindrome("rats live on no evil star"))

print("\n")
# Finding factorials
# return factorial of a given number

factorial = lambda n: n*factorial(n-1) if n > 1 else 1

#Now check the result
print("Output of factorial: ")
print(factorial(5))
print(factorial(7))

print("\n")

# Finding Levenshtein Distance
# return the no of editing steps required to reach from sring a to string b

## Test cases
a = "cat"
b = "chello"
c = "chess"

ls = lambda a, b: len(b) if not a else len(a) if not b else min(ls(a[1:], b[1:])+(a[0]!=b[0]), ls(a[1:], b)+1, ls(a, b[1:])+1)

# Now check the result
print("Output of levenshtein distance: ")
print(ls(a,b))
print(ls(b,c))
print(ls(a,c))