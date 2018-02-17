import itertools

def count(n):
    while 1:
        yield n
        n += 1
        
c = count(0)
for x in itertools.islice(c, 10, 20):
    print(x)
