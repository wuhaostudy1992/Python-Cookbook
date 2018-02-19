import os
import time

print(os.path.exists('c5/test.txt'))
print(os.path.exists('/home/hao/Documents/git/Python-Cookbook/c5/test.txt'))
print('curent path:', os.path.exists('./test.txt'))
print(os.path.isfile('/home/hao/Documents'))
print(os.path.isdir('/home/hao/Documents'))

print(os.path.getsize('./test.txt'))
try:
    print(time.ctime(os.path.getmtime('./test.txt')))
except PermissionError:
    print('You have no permission to access this file.')
