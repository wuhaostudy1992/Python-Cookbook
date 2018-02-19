import os
import glob

names = os.listdir('./')
print('all files in current directory', names)

files = [name for name in os.listdir('./') \
        if os.path.isfile(os.path.join('./', name))]
print(files)

dirs = [name for name in os.listdir('./') \
        if os.path.isdir(os.path.join('./', name))]
print(dirs)

txtfiles = [name for name in os.listdir('./') \
        if name.endswith('.txt')]
print(txtfiles)

tfiles = [name for name in os.listdir('./') \
        if name.startswith('0')]
print(tfiles)

tfiles = [name for name in os.listdir(os.path.pardir) \
        if os.path.isdir(os.path.join(os.path.pardir, name))]
print(tfiles)

pyfiles = glob.glob('*.py')
print(pyfiles)
