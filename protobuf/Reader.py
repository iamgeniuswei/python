import lm.helloworld_pb2
import sys

msg = lm.helloworld_pb2.items()
try:
    f = open("./log6", "rb")
    # print(f.read())
    msg.ParseFromString(f.read())

    for item in msg.hw:
        print("Msg ID: ", item.id)
        print("Msg str: ", item.str)
        # print("Msg New:", item.new)
except Exception as e:
    print(str(e))