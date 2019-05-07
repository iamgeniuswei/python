import os
i=0
while i<2000:
    os.system('nc 127.0.0.1 12345')
    i += 1