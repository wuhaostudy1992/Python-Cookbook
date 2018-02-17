a = [1, 2, 3, 4, 5]
for x in reversed(a):
    print(x)
    
    
class CountDown:
    def __init__(self, start):
        self.start = start
        
    #format iterator
    def __iter__(self):
        n = self.start
        while n>0:
            yield n
            n -= 1
    #Reverse iterator
    def __reversed__(self):
        n = 1
        while n<= self.start:
            yield n
            n += 1
for rr in reversed(CountDown(3)):
    print(rr)
for rr in CountDown(3):
    print(rr)
