from collections import deque
import itertools
dq = deque('abc')
dq.append('d')
dq.appendleft('z')
dq.extend('efg')
dq.extendleft('yxw')
print(dq) # print the deque
print(dq.pop())
print(dq.popleft())
print(dq)
dq.rotate(2) # move elements n step to the right in circular order
print(dq)
dq.rotate(-2) # move elements n step to the left in circular order
print(dq)

# Simple slicing in deqeue is not possible so to implement it we can use 
# itertools.islice() function.

print(list(itertools.islice(dq,3,9)))
