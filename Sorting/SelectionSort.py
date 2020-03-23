'''
The selection sorting algorithm begins by finding the samallest element in the list, and interchanges it with the data stored
at the first postion in the list. Thus, it makes the sub-list sorted up to the first element. Next, the second smallest element
which is the smallest element in the remaining list, is identified and interchanged with second position in the list.
this makes the initial two elements sorted. The process is repeated for (n-1) times to sort n items.
'''
def SelectionSort(unsorted_list):
    size_of_list = len(unsorted_list)
    for i in range(size_of_list-1):
        for j in range(i+1, size_of_list):
            if unsorted_list[j] < unsorted_list[i]:
                temp = unsorted_list[i]
                unsorted_list[i] = unsorted_list[j]
                unsorted_list[j] = temp

    return unsorted_list

unordered_list = [8,5,3,9,2]

print(SelectionSort(unordered_list))