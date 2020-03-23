'''
The idea behind bubble sort algorithm is very simple. Given an unordered list, we compare adjacent elements in the list, and after
each comparison, place them in the right order of magnitude. This works by swapping adjacent items if they are not in order.
The process is repeated for n-1 times for a list of n items.In each such iteration the largest element would be placed at the
end.
'''
def BubbleSort(unordered_list):
    iteration_number = len(unordered_list) -1

    for i in range(iteration_number):
        swap = False
        for j in range(iteration_number-i):
            if unordered_list[j] > unordered_list[j+1]:
                swap = True
                temp = unordered_list[j]
                unordered_list[j] = unordered_list[j+1]
                unordered_list[j+1] = temp
        if swap == False:
            break
    return unordered_list

unordered_list = [8,5,3,9,2]

print(BubbleSort(unordered_list))