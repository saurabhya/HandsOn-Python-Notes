# Use of map()
lst = [1,2,3,4,5]
print("Map() :")
items = [item for item in map(lambda x: x**2, lst)]
print(items)

# Use of filter
print("filter():")
items = [item for item in filter(lambda x: x<4, lst)]
print(items)