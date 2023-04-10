import os

def decoder(filein, fileout, filelog):
    l = [1, 2, 4, 8, 16, 32, 64, 128]
    blocksize = 9
    s = filein.read(blocksize * 3)

    n = blocksize
    s1 = s[:n]
    s2 = s[n:n * 2]
    s3 = s[n * 2:]

    if not s:
        return
    while True:
        fileout.write(s)
        for i in range(n):
            if s1[i] == s2[i] and s3[i] == s2[i]:
                fileout.write(bytes([s1[i]]))
            else:
                x = 0
                for j in range(9):
                    b1 = s1[i] & l[j]
                    b2 = s2[i] & l[j]
                    b3 = s3[i] & l[j]
                    if (b1 + b2 + b3) // l[j] > 1: x += l[j]
                fileout.write(bytes([x]))
        s = filein.read(blocksize)
        if not s:
            break
