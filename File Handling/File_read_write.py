'''
    Once you've opened up a file, you'll want to read or write to the file. First off, let's cover
    reading a file. There are multiple methods that can be called on a file object to help you out:
   
    Method                |      What It Does
--------------------------|------------------------------------------------------------------------------------------------------------------------------
    .read(size=-1)        |      This reads from the file based on the number of size bytes. If no argument is passed or None or -1 is passed, then the entire file is read.
    .readline(size =-1)   |      This reads at most size number of characters from the line. This continues to the end of the line and then wraps back around. If no argument is passed or None or -1 is passed, then the entire line is read.
    .readlines()          |      This reads the remaining lines from the file object and returns them as a list.
'''
with open('C:\\Users\\Saurabh\\Documents\\Github\\HandsOn-Python-Notes\\File Handling\\test.txt', 'r') as reader:
    # read and print the entire file
    print(reader.read())

# Here is an example of how to read the 5 bytes of a line each time using the Python .readline() method:

with open('C:\\Users\\Saurabh\\Documents\\Github\\HandsOn-Python-Notes\\File Handling\\test.txt', 'r') as reader:
    # read and print the first 5 characters of the line 5 times
    print(reader.readline(5))
    # Notice that if the line is greater than the 5 characters and continues down the line,
    # reading 5 chars each time until the end of the line and then "wraps" around
    print(reader.readline(5))
    print(reader.readline(5))
    print(reader.readline(5))
    print(reader.readline(5))

# Here is an example of how to read the entire file as a list using the Python .readlines() method:

with open('C:\\Users\\Saurabh\\Documents\\Github\\HandsOn-Python-Notes\\File Handling\\test.txt', 'r') as reader:
    print(reader.readlines())

# The above example can be done using list() to create a list out of the file object:
f = open('C:\\Users\\Saurabh\\Documents\\Github\\HandsOn-Python-Notes\\File Handling\\test.txt', 'r')
print(list(f))
f.close()


'''
    Iterating over each in the file

    A common thing to do while reading a file is to iterate over each line. Here's an example of how to use the Python .readline()
    method to perform that iteration.
    
'''
with open('C:\\Users\\Saurabh\\Documents\\Github\\HandsOn-Python-Notes\\File Handling\\test.txt', 'r') as reader:
    # read and print entire file line by line
    line = reader.readline()
    while line!= '':
        print(line, end='')
        line = reader.readline()
'''
     Another way you could iterate over each line in this file is to use the Python .readlines() method of the file object.
     Remember, .readlines() returns a list where each element in the list represents a line in the file:
'''

with open('C:\\Users\\Saurabh\\Documents\\Github\\HandsOn-Python-Notes\\File Handling\\test.txt', 'r') as reader:
    for line in reader.readlines():
        print(line, end="")

'''
    Now let's dive into writing files. As with reading files, file objects have multiple methods that are useful for writing to a file:

    Method                              What it does
-----------------------------------------------------------------------------------------------------------------------------------
    .write()                              This write the string to the file
    .writelines(seq)                      This writes the sequence to the file. No line endings are appended to each sequence item.
'''

