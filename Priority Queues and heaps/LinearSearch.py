'''
The searching operation id to findout a given item from the stored data. If the searched ite is available in the stored list then
it returns the index position where it is located, or else returns that the item is not found.
the simplest approach to search for an item in a list is the linear search method, in which we look for items one by one in
the whole list.
'''
# Unordered Linear Search
def search_un(unordered_list, term):
    for i in range(len(unordered_list)):
        if term == unordered_list[i]:
            return i
    return None

# Ordered Linear search
def search_or(ordered_list, term):
    for i in range(len(ordered_list)):
        if term == ordered_list[i]:
            return i
        elif ordered_list[i]>term:
            return None
    return None
