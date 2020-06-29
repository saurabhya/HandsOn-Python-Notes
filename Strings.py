words = str.split('The longest word is this sentence')
lst = sorted(words, key=len)
print(lst)

# Case insensitive sorting
sl = ['A','b','a','C','c']
sl.sort(key=str.lower)
print(sl)
sl.sort()
print(sl)

# Use of lambda in key
items = [['rice',2.4,8],['flour',1.9,5],['corn',4.7,6]]
items.sort(key= lambda item: item[0])
print(items)