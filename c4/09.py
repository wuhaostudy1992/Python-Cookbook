from itertools import permutations
from itertools import combinations
from itertools import combinations_with_replacement

items = [1,2,3]
#print all posible arrays
for p in permutations(items):
    print(p)

#print specific length arrays
for p in permutations(items, 2):
    print(p)
print('___')
for c in combinations(items, 2):
    print(c)
    
print('____')
for c in combinations_with_replacement(items, 2):
    print(c)
