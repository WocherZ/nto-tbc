#!/usr/bin/python3


def encoder(filein,fileout):
    dd=100
    b=bytearray([x for x in range(dd)])
    s=filein.read()
    for i in range(7):
        fileout.write(b)

        fileout.write(s)

                 
