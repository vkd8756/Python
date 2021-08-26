from socket import *
import time
def createserver():
    #server ip--http://127.0.0.1:9000/
    serversocket=socket(AF_INET,SOCK_STREAM)
    try:
        serversocket.bind(("localhost",9000))
        serversocket.listen(5)
        while(1):
            #print("Server is getting on...")
            #time.sleep(3)
            #print("Server is ON now\n")
            (clientsocket,address)=serversocket.accept()
            rd=clientsocket.recv(5000).decode()
            pieces=rd.split("\n")
            if len(pieces)>0:
                print(pieces[0])
            data="HTTP/1.1 200 OK\r\n"
            data+="Content-Type: text/html, charset=utf-8\r\n"
            data+='\r\n'
            data+="<!DOCTYPE html><html lang=""><head><title>Vivek Dubey ... b3aa19 ... </title></head>"
            data+="<body><h1><strong>VIVEK DUBEY</strong></h1><pre>Hey..This is my <em>first</em> html web page.</pre>"
            data+="<p>Thankyou for <strong>visitng</strong> and <strong>grading.</strong></p>"
            data+="<p>Let's try some links now</p>"
            data+="<ul><li><p><a href=\"https://www.google.com\">Google</a></p></li>"
            data+='<li><p><a href="https://www.wikipedia.com">Wikipedia</a></p></li>'
            data+='<li><p><a href="https://www.dj4e.com/.com">dr-chuck\'s site</a> A good place for learner\'s.</p></li></ul>'
            data+='<p>My mother has <span style="color:blue">blue</span> eyes.</p>'
            data+='<div class="alpha"><h2>This is a heading in a div element</h2><p>This is some text in a div element.</p>'
            data+='<h3>Table in html</h3>'
            data+='<table><tbody>'
            data+='<tr>'
            data+='<th>First</th>'
            data+='<th>Second</th>'
            data+='<th>Third</th>'
            data+='</tr>'
            data+='<tr><td>1</td><td>2</td><td>3</td></tr>'
            data+='<tr><td>11</td><td>22</td><td>33</td></tr>'
            data+='</tbody></table>'
            data+='</div>'
            data+='</body>'
            data+='</html>'
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)
            #break
    except KeyboardInterrupt:
        print("\n shutting down ...\n")
    except Exception as exc :
        print("Error: \n")
        print(exc)
    serversocket.close()
print("access http:localhost 9000")
createserver()
