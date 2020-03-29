'''
    The lambda keyword creates an anonymous function within a Python expression.
    However, The simple syntax of Python limits the body of lambda functions to be pure expressions.
    In other words, the body of a lambda cannot make assignments or use any other Python statement
    such as while, try etc.

    The best use of anonymous functions is in the context of an argument list.
'''
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
print(sorted(fruits))
print(sorted(fruits, key= lambda word: word[::-1]))

'''
    Lundh's lambda refactoring recipe
    if you find a piece of code hard to understand because of a lamda, Fredrik Lundh suggests
    this following refactoring procedure :
    1. Write a comment explaining what the heck that lambda does.
    2. Study the comment for a while, and think of a name that captures the essence of the comment.
    3. Convert the lambda to a def statement, using that name.
    4. Remove the comment.
'''