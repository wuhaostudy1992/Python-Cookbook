import heapq
a = [1,4,7,5,8,9]
b = [2,5,6,9,11]

for c in heapq.merge(a, b):
    print(c)
