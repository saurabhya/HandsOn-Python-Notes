'''
    The quickselect algorithm is used to obtain the kth smallest element in an unordered list of items, and is based on
    quickSort algorithm. In quickSort, we recursively sort the elements of both the sublists from the pivot point.
    In quick sort in each iteration, we know that the pivot value reaches its correct position in the list with two sublists,
    having all of their elements set to be unordered.

    However, in case of quickselect algorithm, we recursively call the function exclusively for the sublist that has the kth
    smallest element. In the quickselect algorithm, we compare the index of pivot point with the k value to obtain the kth
    smallest element from the given unordered list. There wil be three cases in the quickselect algorithm :
    1. If the index of the pivot position is smaller than k, then we are sure that kyh smallest value will be present in the right
       sublist of the pivot point. So, we only recursively call quickselect funtion for the right sub-list.
    2. If the index of the pivot point is greater than k, then it is obvious that the kth smallest element is located in the left
       sublist. So we only recursively call quickselect algorithm for the left sub-list.
    3. If the index of the pivot point is equal to k, then it means that we have found out the kth smallest element, we return it.
'''

def partition(unsorted_array, first_index, last_index):
    if first_index == last_index:
        return first_index
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


def quick_select(array_list, left, right, k):
    split = partition(array_list, left, right)
    if split == k:
        return array_list[split]
    elif split < k:
        return quick_select(array_list, split+1,right, k)
    else:
        return quick_select(array_list, left, split-1, k)
