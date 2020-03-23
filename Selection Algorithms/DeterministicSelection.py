'''
The worst case performance of a randomized selection algorithm is O(n^2). It is posibble to improve the selection
of an element of the randomized selection algorithm to obtain a worst-case performance of O(n). We can obtain the performance
of O(n) by using an algorithm, deterministic selection.

Median of median is an algorithm that provides us with the approxiamate median value, that is, a value close to the actual median for
a given unsorted list of elements. This approximate median is often used as pivot point in the quickselect algorithm for selecting
the ith smallest element from the list. It is due to the fact that median of median algorithm finds the estimated median in a linear
time, and when thiis estimated median is used as a pivot point in the quickselect algorithm, the worst-case running time improves
from O(n^2) to O(n).

The general approach to te deterministic algorithm to select the ih smallest element is listed here:
1. Select a pivot:
    1. Split a list of unordered items into groups of five elements each.
    2. Sort and find the median of all groups.
    3. Repeat steps 1 and 2 recursively to obtain the true median of the list.
2. Use the true median to partition the list of unordered items.
3. Recurse into the part of the partitioned list that may contain the ith smallest element.
'''

def partition(unsorted_array, first_index, last_index):
    if first_index == last_index:
        return first_index
    else:
        nearest_median = median_of_medians(unsorted_array[first_index:last_index])

    index_of_nearest_median = get_index_of_median(unsorted_array, first_index, last_index, nearest_median)
    swap(unsorted_array, first_index, index_of_nearest_median)
    pivot = unsorted_array[first_index]
    pivot_index = first_index
    index_of_last_element = last_index
    less_than_pivot_index = index_of_last_element
    greater_than_pivot_index = first_index + 1
