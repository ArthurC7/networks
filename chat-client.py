import socket
import sys

name = sys.argv[1]
host = sys.argv[2]
port = int(sys.argv[3])
to_send = sys.argv[4: len(sys.argv)]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(host, port)
sock.sendall(name + "\n")
in_chat = True
count_to_timeout = 0

while(in_chat):
    message = input("mess: ")
    sock.send("mess: " + message + "\n")
    response = sock.recv(16)
    print(response)
sock.close()


def keep_alive(alive_count):
    sock.sendall("alive:\n")
    alive_count += 1
    return alive_count

