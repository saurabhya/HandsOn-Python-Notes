'''
The heap data structure can be used to implement a sorting algoritm called heap sort.
we will be using the heap class that we built earlier and try to write our sorting method inside the class.
'''
class Heap:
    def __init__(self):
        self.heap = [0] # We initialize our heap list with 0 to represent the dummy first element.
        self.size = 0

    def arrange(self, k):
        while k//2 > 0:
            if self.heap[k]< self.heap[k//2]:
                self.heap[k], self.heap[k//2] = self.heap[k//2], self.heap[k]
            k = k//2

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self.arrange(self.size)

    def minindex(self, k):
        if k*2+1 > self.size:
            return k*2
        elif self.heap[k*2] < self.heap[k*2+1]:
            return k*2
        else:
            return k*2+1

    def sink(self, k):
        while k*2 <= self.size:
            mi = self.minindex(k)
            if self.heap[k] > self.heap[mi]:
                self.heap[k], self.heap[mi] = self.heap[mi], self.heap[k]
            k = mi

    def pop(self):
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.sink(1)
        return item

    def heap_sort(self):
        sorted_list =[]
        for node in range(self.size):
            n = self.pop()
            sorted_list.append(n)
        return sorted_list

h = Heap()

unsorted_list = [4,8,7,2,9,10,5,1,3,6]
for i in unsorted_list:
    h.insert(i)

print("Unsorted List : {}".format(unsorted_list))

print("Sorted List : {}".format(h.heap_sort()))