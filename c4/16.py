CHUNKSIZE = 8192

def read(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        pass
        # process chunk

def openfile():
    with open('test.txt') as f:
        for chunk in iter(lambda: f.read(100), ''):
            print(chunk)
            
openfile()
