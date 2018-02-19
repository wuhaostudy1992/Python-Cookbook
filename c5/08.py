from functools import partial

CHUNKSIZE = 10

with open('test.txt') as f:
    i = 0
    for chunk in iter(lambda: f.read(CHUNKSIZE), ''):
        i += 1
        print(i)
        print(chunk)

with open('test.txt') as f:
    i = 0
    for r in iter(partial(f.read, CHUNKSIZE), ''):
        i += 1
        print(i)
        print(r)
