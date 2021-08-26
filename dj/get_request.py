#run server.py first, then run it in other command window
import urllib.request
fhand=urllib.request.urlopen('http://127.0.0.1:9000/')
for line in fhand:
    print(line.decode().strip())
