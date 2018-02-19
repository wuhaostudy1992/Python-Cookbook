import sys
import os

print(sys.getfilesystemencoding())
print(os.listdir(b'.'))
with open(b'test.txt', 'r') as f:
    print(f.read())
