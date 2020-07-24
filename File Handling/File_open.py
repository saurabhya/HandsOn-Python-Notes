"""
    When you want to work with a file, the first thing to do is to open it.
    This is done by invoking the open() built-in function. open() has a single
    required argument that is the path to the file.open() has a single return,
    the file object:
"""
#file = open("C:\\Users\\Saurabh\\Documents\\Github\\HandsOn-Python-Notes\\File Handling\\test.txt")

"""
    After you open a file, the next thing to learn is how to close it.
    It's important to remember that it's programmer responsibility to close the file.
    In most cases, upon termination of an application or script, a file will be closed
    eventually. However, there is no guarantee when exactly that will happen.
    This can lead to unwanted behavior including resource leaks. It's also a best
    practice within Python to make sure that your code behaves in a way that is well
    defined and reduces any unwanted behavior.

    When you are manipulating a file, there are two ways that you can use to ensure that
    a file is closed properly, even when encountering an error. The first way to close a file
    is to use the try-finaly block:
"""
reader = open('C:\\Users\\Saurabh\\Documents\\Github\\HandsOn-Python-Notes\\File Handling\\test.txt')
try:
    pass #Further file processing
finally:
    reader.close()

"""
    The second way to close a file is to use with statement:
"""
with open('C:\\Users\\Saurabh\\Documents\\Github\\HandsOn-Python-Notes\\File Handling\\test.txt') as reader:
    pass # further file processing

"""
    The with statement automatically take care of closing the file once it leaves
    the with block, even in cases of error. I higly recommend that you use the with
    statement as much as possible, as it follows for cleaner code and makes handling
    any unexpected erorrs easier for you.
    Most likely, you'll also want to use the second positional argument, mode. This argument
    is the string that contains multiple charatcers to represent how you want to open the file.
    The default and most common is 'r, which is opening the file in read-only mode as a text file.
"""
with open('C:\\Users\\Saurabh\\Documents\\Github\\HandsOn-Python-Notes\\File Handling\\test.txt', 'r') as reader:
    pass # further precessing of file
