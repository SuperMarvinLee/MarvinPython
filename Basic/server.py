import socket
import sys

serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()

port = 9999

serversocket.bind((host, port))

# 设置最大连接数,超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket,addr = serversocket.accept()      

    print("连接地址: %s" % str(addr))
   
    msg='欢迎访问MarvinPython！'+ "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()