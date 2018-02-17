from itertools import dropwhile
from itertools import islice

with open('test.txt') as f:
    #The below code will ignore the first several lines which starts with #
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')
        
items = [1,2,3,4,5,6,7,8,9]
for x in islice(items, None, 5):
    print(x)
