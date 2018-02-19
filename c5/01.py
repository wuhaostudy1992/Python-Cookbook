with open('test.txt', 'rt') as f:
	data = f.read()

print(data)

with open('test.txt', 'wt') as f:
	f.write('This is the first line.')
	f.write('This is the second line.')
	f.write('\n')
	f.write('This is the last line.')

with open('test.txt', 'at') as f:
	f.writh
