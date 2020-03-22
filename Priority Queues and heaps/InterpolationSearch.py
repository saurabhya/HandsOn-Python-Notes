'''
The interpolation search algorithm is an improved version of binary search algorithm. It performs very efficiently when there are uniformly distributed
elements in the sorted list. In a binarry search, we always start searching from the middle of the list, whereas
in the interpolation search we determine the starting position depending on the item to be searched. In the interpolation
search algorithm, the starting search position is most likely to be closest to the start or end of the list depending
on the search item. If the search item is near to the first elementin the list, then the starting position is likely
to be near the start of the list.

In the case of a binry search we divide the data into equal halves and in the case of an interpolation search,
we divide the data using the following fomula:

mid_point = lower_bound_index + ((upper_bound_index - lower_bound_index)//(input_list[upper_bound_index] - input_list[lower_bound_index])) * (search_value - input_list[lower_bound_index])

For a given list to search for an element, a more humanlike method would be to pick a middle element in such a way
as to not only split the array in half but to get as close as possible to the search term.
mid_point = (index_of_first_element + index_of_last_element)//2

We shall replace this formula with a better one that brings us closer to the search term in the case of interpolation
search algorithm. The mid_point will recieve the return value of the nearest_mid function, which is computed using
the following method:
'''
def nearest_mid(input_list, lower_bound_index, upper_bound_index, search_value):
    return lower_bound_index + ((upper_bound_index - lower_bound_index)//(input_list[upper_bound_index] - input_list[lower_bound_index])) * (search_value - input_list[lower_bound_index])

def interpolation_search(ordered_list, term):
    size_of_list = len(ordered_list) - 1
    index_of_first_element = 0
    index_of_last_element = size_of_list

    while index_of_first_element <= index_of_last_element:
        mid_point = nearest_mid(ordered_list, index_of_first_element, index_of_last_element, term)
        if mid_point > index_of_last_element or mid_point < index_of_first_element:
            return None
        if ordered_list[mid_point] == term:
            return mid_point
        if term > ordered_list[mid_point]:
            index_of_first_element = mid_point+1
        else:
            index_of_last_element = mid_point-1
    if index_of_first_element > index_of_last_element:
        return None