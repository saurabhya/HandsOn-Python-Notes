# Dictionary for text analysis
'''
Following code creates a dictionary where wach word in the text is used as a key
and the number of occurences as its values.
'''
def wordcount(fname):
    try:
        fhand = open(fname)
    except:
        print('File can not be opened !!!')
        exit()

    count = dict()
    for lines in fhand:
        words = lines.split()
        for word in words:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
    return count

count = wordcount("C:\Users\Saurabh\Desktop\editor\.vscode\HandsonDataStructuresandAlgorithmsin Python\ test.txt")
print(count) 