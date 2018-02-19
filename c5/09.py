import os.path
import numpy as np

def read_into_buffer(filename):
    #buf = np.array(os.path.getsize(filename)) not feasible
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        n = f.readinto(buf)
    return buf
    
buf = read_into_buffer('test.txt')
print(buf)
