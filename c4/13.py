import os
import fnmatch
import gzip
import bz2
import re

def gen_find(filepath, top):
    '''
    Find all filenames in filepath
    '''
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepath):
            yield os.path.join(path, name)

def gen_opener(filenames):
    if filename.endswith('.gz'):
        f = gzip.open(filename, 'rt')
    elif filename.endswith('.bz2'):
        f = bz2.open(filename, 'rt')
    else:
        f = open(filename, 'rt')
    yield f
    f.close()

def gen_concatenate(iterators):
    '''
    Chain a sequence of iterators together into a single sequence
    '''
    for it in iterators:
        yield from it

def gen_grep(pattern, lines):
    '''
    Look for a regex pattern in a sequence of lines
    '''
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line
            
lognames = gen_find('access-log*', 'www')
files = gen_opener(lognames)
lines = gen_concatenate(files)
pylines = gen_grep('(?i)python', lines)
for line in pylines:
    print(line)
