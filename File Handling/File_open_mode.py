'''
    Except opening a file in read mode there are other options as well for opening a file.
    Following are some commonly used modes:

    Character         Meaning
   -----------------------------------------------------------------
    'r'               Open for reading(default)
    'w'               Open for writing, truncating(overwriting) the file first
    'rb' or 'wb'      open in binary mode(read/write using byte date)

    A file object is an object exposing a file-oriented API (with methods such as read() or write() to an underlying resource.)

    There are three different categories of file objects:
    * Text files
    * Buffered binary files
    * Raw binary files

    Each of these files types are defined in the io module.


    Text file types

    A text is the most common file that you'll encounter. Here are some examples of how these files are opened:
'''
file = open('C:\\Users\\Saurabh\\Documents\\Github\\HandsOn-Python-Notes\\File Handling\\test.txt')
print(type(file)) # This returns the default file object: <class '_io.TextIOWrapper'>
file.close()

'''
    Buffered Binary file types

    A buffered binary file type is used for reading and writing binary files. here are some examples of how these files are opened:
    
    open('test.txt', 'rb')
    open('test.txt', 'wb')
    
    With these types of files, open() will return either a BufferedReader of BufferedWriter file object:
'''
file = open('C:\\Users\\Saurabh\\Documents\\Github\\HandsOn-Python-Notes\\File Handling\\test.txt','rb')
print(type(file))
file.close()

# for writing 
file = open('C:\\Users\\Saurabh\\Documents\\Github\\HandsOn-Python-Notes\\File Handling\\test.txt','wb')
print(type(file))
file.close()

'''
    Raw file types

    A raw file type is generally used as a low level building block for binary and text streams.
    It is therefore not typically used.
    Following is an example of these files are opened:
'''
file = open('C:\\Users\\Saurabh\\Documents\\Github\\HandsOn-Python-Notes\\File Handling\\test.txt','rb', buffering=0)
print(type(file))
file.close()
