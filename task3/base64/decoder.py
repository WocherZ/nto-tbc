import base64

#!/usr/bin/python3
def decoder(filein, fileout, filelog):
    blocksize = 12
    s = filein.read(blocksize)
    if not s:
        return
    while True:
        decoded_message = base64.b64decode(s)
        print(s, decoded_message)
        fileout.write(decoded_message)
        s = filein.read(blocksize)
        if not s:
            break

