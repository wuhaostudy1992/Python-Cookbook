import urllib.request
import io

u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u, encoding='utf-8')
test = f.read()
#print(test)

#change unicode:
#sys.stdout.detach()


