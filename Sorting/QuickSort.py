'''
The quick sort algorithmis very efficient for sorting. The quik sort algorithm falss under divide and conquer class
of algorithms, similar to the merge sort algorithms, where we break a problem into smaller subproblems that are
much simpler to solve.

The concept behind quick sorting is partitioning a given list or array. To partition the list, we first select pivot.
At the end of the partitioning process, all elements that are less than the pivot will be to the left of the pivot, while
all the elements greater than the pivot will lie to the right of the pivot in the list.

For the sake of the simplicity, we'll take the first element in an array as the pivot. This kind of pivot selection
degrades in performance, espacially when sorting an already sorted array. Randomly piking the middle or last element
in the array asthe pivot does not improve the performance of the quick sort.
'''
def partition(unsorted_array, first_index, last_index):
    pivot = unsorted_array[first_index]
    pivot_index = first_index
    index_of_last_element = last_index
    less_than_pivot_index = index_of_last_element
    greater_than_pivot_index = first_index + 1
    while True:
        while unsorted_array[greater_than_pivot_index] < pivot and greater_than_pivot_index < last_index:
            greater_than_pivot_index += 1
        while unsorted_array[less_than_pivot_index] > pivot and less_than_pivot_index >= first_index:
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

def quick_sort(unsorted_array, first, last):
    if last - first <= 0:
        return
    else:
        partition_point = partition(unsorted_array, first, last)
        quick_sort(unsorted_array, first, partition_point-1)
        quick_sort(unsorted_array, partition_point+1, last)


unordered_list = [8,5,3,9,2]

quick_sort(unordered_list,0, len(unordered_list)-1)
print(unordered_list)
