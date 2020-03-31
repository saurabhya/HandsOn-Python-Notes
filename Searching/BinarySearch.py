'''
A binary search is a search strategy used to find elements within a sorted array or list; thus, the binary search
algorithm finds a given item from the given sorted list of items. It is a very fast and efficient algorithm to search
an element, and the only drawback is that we need a sorted list. The worst case running time complexity of a binary
search algorithm is O(log n) whereas the linear search has O(n).
'''
def binary_search(ordered_list, term):
    size_of_list = len(ordered_list)-1
    index_of_first_element = 0
    index_of_last_element = size_of_list
    while index_of_first_element <= index_of_last_element:
        mid_point = (index_of_first_element + index_of_last_element)//2
        if ordered_list[mid_point] == term:
            return mid_point
        if term > ordered_list[mid_point]:
            index_of_first_element = mid_point + 1
        else:
            index_of_last_element = mid_point - 1
    if index_of_first_element > index_of_last_element:
        return None


