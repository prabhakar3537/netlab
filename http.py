from socket import *
host='localhost'
port=12345
s=socket(AF_INET,SOCK_STREAM)
s.bind((host,port))
s.listen(1)
html="""
HTTP/1.1
Content-Type: text/html

<html>
<head>This is the heading</h>
<body>
<h1>Heading</h1>
<br>
<p>Sample Paragraph</p>
</body>
</html>
"""
(conn,addr)=s.accept()
sent=conn.send(html)