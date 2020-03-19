import collections
dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {'d':4, 'e':5}
chainmap = collections.ChainMap(dict1, dict2)
print(chainmap)
print(chainmap.maps)
print(chainmap.values)
print(chainmap['b'])
################################################

defaults = {'theme':'Default', 'language':'eng', 'shoeIndex':True, 'showFooter':True}
cm = collections.ChainMap(defaults) #create a chainmap with default configuration
print(cm.maps)
print(cm.values())
cm2 = cm.new_child({'theme':'bluesky'})
print(cm2['theme'])