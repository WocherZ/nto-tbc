#!/usr/bin/python3


def encoder(filein,fileout):
    b=bytearray([x for x in range(100)])
    s=filein.read()
    fileout.write(b)

    fileout.write(s)

    fileout.write(b)

    fileout.write(s)

    fileout.write(b)

    fileout.write(s)

    fileout.write(b)

    fileout.write(s)

    fileout.write(b)

    fileout.write(s)

                 
