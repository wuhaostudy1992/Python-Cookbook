from tempfile import TemporaryFile
from tempfile import NamedTemporaryFile

with TemporaryFile('w+t') as f:
    f.write('Hello? \n')
    f.write('This is a test\n')
    
    f.seek(0)
    data=f.read()
    print(data)
    
with NamedTemporaryFile('w+t') as f:
    print('filename is:', f.name)
