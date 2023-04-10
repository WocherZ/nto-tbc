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

filein = open('encoded_file.txt', 'rb')
fileout = open('decoded_fileout.txt', 'wb')

filelog = open('filelog.txt', 'wb')

decoder(filein, fileout, filelog)

filein.close()
fileout.close()
filelog.close()
