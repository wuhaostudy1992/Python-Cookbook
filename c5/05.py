with open('test.txt', 'wt') as f:
    f.write('Hello')

try:
    with open('test.txt', 'xt') as f:
        f.write('Hello')
except FileExistsError:
    print('File already exists.')

