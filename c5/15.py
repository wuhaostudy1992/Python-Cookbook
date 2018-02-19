def bad_filename(filename):
    return repr(filename)[:]
    
def bad_filename_new(filename):
    temp = filename.encode(sys.getfilesystemencoding(), errors='surrogateescape')
    return temp.decode('utf-8')
    
try:
    print(filename)
except UnicodeEncodeError:
    print(bad_filename(filename))
