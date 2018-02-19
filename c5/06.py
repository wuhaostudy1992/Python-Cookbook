import io

s = io.StringIO()
s.write('Hello World\n')

print('This is a test IO file', file=s)

print(s.getvalue())
