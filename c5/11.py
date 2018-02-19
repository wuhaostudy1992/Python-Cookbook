import os

absdirname = os.path.abspath('test.txt')
print('parent dir:', os.path.pardir)
print(absdirname)
#dirname = os.path.dirname(os.path.abspath("test.txt"))
#print(dirname)
print(os.path.basename(absdirname))
print(os.path.dirname(absdirname))
print('parent dir:', os.path.pardir)
