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

def median_of_medians(elems):
    sublists = [elems[j:j+5] for j in range(0, len(elems), 5)]
    medians = []
    for sublist in sublists:
        medians.append(sorted(sublist)[len(sublist)//2])
    if len(medians) <= 5:
        return sorted(medians)[len(medians)//2]
    else:
        return median_of_medians(medians)

def get_index_of_nearest_median(array_list, first, second, median):
    if first == second:
        return first
    else:
        return first + array_list[first:second].index(median)

def swap(array_list, first, second):
    temp = array_list[first]
    array_list[first] = array_list[second]
    array_list[second] = temp

def partition(unsorted_array, first_index, last_index):
    if first_index == last_index:
        return first_index
    else:
        nearest_median = median_of_medians(unsorted_array[first_index:last_index])

    index_of_nearest_median = get_index_of_nearest_median(unsorted_array, first_index, last_index, nearest_median)
    swap(unsorted_array, first_index, index_of_nearest_median)
    pivot = unsorted_array[first_index]
    pivot_index = first_index
    index_of_last_element = last_index
    less_than_pivot_index = index_of_last_element
    greater_than_pivot_index = first_index + 1

    while True:
        while unsorted_array[less_than_pivot_index] < pivot  and greater_than_pivot_index < last_index:
            greater_than_pivot_index += 1
        while unsorted_array[greater_than_pivot_index] > pivot and less_than_pivot_index >= first_index:
            less_than_pivot_index -= 1
        if greater_than_pivot_index < less_than_pivot_index:
            temp = unsorted_array[greater_than_pivot_index]
            unsorted_array[greater_than_pivot_index] = unsorted_array[less_than_pivot_index]
            unsorted_array[less_than_pivot_index] = temp
        else:
            break
    unsorted_array[pivot_index] = unsorted_array[less_than_pivot_index]
    unsorted_array[less_than_pivot_index] = pivot
    return less_than_pivot_index

def deterministic_select(array_list, left, right, k):
    split = partition(array_list, left, right)
    if split == k:
        return array_list[split]
    elif split < k:
        return deterministic_select(array_list, split+1, right, k)
    else:
        return deterministic_select(array_list, left, split-1, k)