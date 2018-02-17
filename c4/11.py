from itertools import zip_longest

itemx = [1,2,3,4,5,6]
itemy = [2,4,6,8,10,12,14]

for x, y in zip(itemx, itemy):
    print(x, y)
print('____')
for x, y in zip_longest(itemx, itemy):
    print(x, y)
