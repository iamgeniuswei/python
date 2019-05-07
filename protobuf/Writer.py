import lm.helloworld_pb2
import sys



# msg = lm.helloworld_pb2.helloworld()
# msg.id = 10
# msg.str = "dfafafafaf"

# msg1 = lm.helloworld_pb2.helloworld()
# msg1.id = 10
# msg1.str = "dfafafafaf"

hw = lm.helloworld_pb2.items()
msg = hw.hw.add()
msg.id = 30
msg.str = "Third Item"
msg.new = "New Field"
msg1 = hw.hw.add()
msg1.id = 40
msg1.str = "Forth Item"
print(msg.IsInitialized())
print(msg1.IsInitialized())
# msg1.new = "New Field Forth"
# hw.hw.add(msg1)
try:
    f = open('log6', "ab+")
    bs = hw.SerializeToString()
    f.write(bs)
except Exception as e:
    print(str(e))

# msg.id = 20
# msg.str = "my name "
# try:
#     f = open('log5', "ab")
#     f.write(msg.SerializeToString())
# except Exception as e:
#     print(str(e))