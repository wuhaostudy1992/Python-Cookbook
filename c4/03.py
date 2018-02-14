def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


for n in frange(0, 3.0, 0.3):
    #print(n)
    #The result show: 0.9 as 0.899999...

n = frange(0, 3.0, 0.3)
print(next(n))
print(next(n))
print(next(n))
print(next(n))
