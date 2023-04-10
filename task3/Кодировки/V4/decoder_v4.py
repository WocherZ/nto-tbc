#!/usr/bin/python3


def decoder(filein, fileout, filelog):
    dd=100
    l=[1,2,4,8,16,32,64,128]
    s = filein.read()

    n=filein.tell()//7 - dd
    s1=s[dd:n+dd]
    s2=s[2*dd+n:n*2+2*dd]
    s3=s[3*dd+n*2:n*3+3*dd]
    s4=s[4*dd+n*3:n*4+4*dd]
    s5=s[5*dd+n*4:n*5+5*dd]
    s6=s[6*dd+n*5:n*6+6*dd]
    s7=s[7*dd+n*6:]


    b=bytearray([0 for x in range(n)])
    for z in range(1):
        for i in range(n):
            if s1[i]==s2[i] and s3[i]==s2[i] and s3[i]==s4[i] and s5[i]==s2[i] and s6[i]==s2[i] and s7[i]==s2[i]: b[i]=s1[i]
            else:
                x=0
                for j in range(8):
                    b1=s1[i]&l[j]
                    b2=s2[i]&l[j]
                    b3=s3[i]&l[j]
                    b4=s4[i]&l[j]
                    b5=s5[i]&l[j]
                    b6=s6[i]&l[j]
                    b7=s7[i]&l[j]
                    if (b1+b2+b3+b4+b5+b6+b7)>3*l[j]:x+=l[j]
                b[i]=x
    fileout.write(b)

