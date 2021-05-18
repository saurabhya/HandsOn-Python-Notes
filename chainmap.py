import collections
dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {'d':4, 'e':5}
chainmap = collections.ChainMap(dict1, dict2)
print("Chain map is: ",chainmap)
print("Chainmap.maps: ",chainmap.maps)
print("Chainmap.values: ",chainmap.values)
print("Chainmap['b']: ",chainmap['b'])
################################################

# Some other functions realted to chain maps

defaults = {'theme':'Default', 'language':'eng', 'shoeIndex':True, 'showFooter':True}
cm = collections.ChainMap(defaults) #create a chainmap with default configuration
print(cm.maps)
print(cm.values())
cm2 = cm.new_child({'theme':'bluesky'})
print(cm2['theme'])
