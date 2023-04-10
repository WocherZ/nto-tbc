import base64

#!/usr/bin/python3
def encoder(filein,fileout):
    blocksize=8
    while True:
        s=filein.read(blocksize)
        if not s:
            break
        encoded_message = base64.b64encode(s)
        print(s, encoded_message)
        fileout.write(encoded_message)

filein = open('filein.txt', 'rb')
fileout = open('encoded_file.txt', 'wb')

encoder(filein, fileout)

filein.close()
fileout.close()