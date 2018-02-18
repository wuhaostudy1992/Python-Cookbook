CHUNKSIZE = 8192

def read(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        pass
        # process chunk
