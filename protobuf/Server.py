# -*- coding: utf-8 -*-
# source: Server.py

import socket
import lm.helloworld_pb2
import sys
try:
    s = socket.socket()
    host = socket.gethostname()
    print(host)
    port = 12345
    s.bind((host, port))
    s.listen(5)
    while True:
        c, addr = s.accept()
        print('Accept addr: ', addr)
        recv = c.recv(1024)
        msg = lm.helloworld_pb2.items()
        msg.ParseFromString(recv)
        for item in msg.hw:
            print("Msg ID: ", item.id)
            print("Msg str: ", item.str)
        c.close()
except Exception as e:
    print(str(e))
