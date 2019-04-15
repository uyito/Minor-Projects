import socket
import sys
from _thread import *

host = 'localhost'
port = 8081
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)
# server = 'pythonprogramming.net'
#
# server_ip = socket.gethostbyname(server)
# print(server_ip)
#
# request = "GET / HTTP/1.1\nHost: " + server+"\n\n"

# s.connect((server, port))
# s.send(request.enconde())
# result = s.recv(4000)

# print(result)

try:
    s.bind((host, port))

except socket.error as e:
    print(str(e))

s.listen(5)
print('Waiting for a connection')


def threaded_client(conn):
    conn.send(str.encode('welcom, type your message\n'))

    while True:
        data = conn.recv(2048)
        reply = 'Server output: ' + data.decode('utf-8')
        if not data:
            break
        conn.sendall(str.encode(reply))
    conn.close()

while True:

    conn, addr = s.accept()

    print('connected to: '+addr[0]+':'+str)

    start_new_thread(threaded_client, (conn, ))
