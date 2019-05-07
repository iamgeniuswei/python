import lm.helloworld_pb2
import sys
import socket

hw = lm.helloworld_pb2.items()
msg = hw.hw.add()
msg.id = 30
msg.str = "Third Item"
msg1 = hw.hw.add()
msg1.id = 40
msg1.str = "Forth Item"
bs = hw.SerializeToString()

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host, port))
s.send(bs)
s.close()
