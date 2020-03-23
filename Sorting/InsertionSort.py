'''
The idea of swapping adjacent lements to sort a list of items can also be used to implement the insertion sort. An insertion
sorting algorithm maintains a sub-list that is always sorted, while the other portion remains unsorted. We take elements
fro the unsorted sub-list and insert them in the correct position in the sorted sub-list, in such a way that this
sub-list remains sorted.
In insertion sort we start with one element assuming it to be sorted, and then take another element from the unsorted
sub-list and place it to the correct position in the sorted sub-list. This means that our sorted sub-list now has two
elements. Then, we again take another element from the unsorted sub-list, and place it in the orrect position
in the sorted sub-list. We repeatedly follow this process to insert all elements one by one from the unsorted sub-list
ino the sorted sub-list.
'''

def InsertionSort(unsorted_list):
    for index in range(1, len(unsorted_list)):
        search_index = index
        insert_value = unsorted_list[index]
        while search_index > 0 and unsorted_list[search_index-1] > insert_value:
            unsorted_list[search_index] = unsorted_list[search_index-1]
            search_index -= 1
        unsorted_list[search_index] = insert_value
    return unsorted_list


unordered_list = [8,5,3,9,2]

print(InsertionSort(unordered_list))