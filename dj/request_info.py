import socket
#to connect to the local host--9000
my_s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#http://data.pr4e.org/intro-short.txt
my_s.connect(('localhost', 9000))
#htm or txt can be used to get requests
#cmd='GET http://data.pr4e.org/into-short.htm HTTP/1.0\r\n\r\n'.encode()
'''Ip of the local host is http://127.0.0.1:9000/'''
cmd='GET http://127.0.0.1:9000/ HTTP/1.0\r\n\r\n'.encode()
my_s.send(cmd)
while True:
    data=my_s.recv(512)
    if len(data)<1:
        break
    print(data.decode(),end=" ")
my_s.close()
