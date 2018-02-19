import os
import sys

fd = os.open('test.txt', os.O_WRONLY | os.O_CREAT)

f = open(fd, 'a', closefd=False)
f.write('Hello World\n')
f.close()
