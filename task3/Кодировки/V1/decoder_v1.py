#!/usr/bin/python3


def decoder(filein, fileout, filelog):
    l=[1,2,4,8,16,32,64,128]
    s = filein.read()

    n=filein.tell()//5 - 100
    s1=s[100:n+100]
    s2=s[200+n:n*2+200]
    s3=s[300+n*2:n*3+300]
    s4=s[400+n*3:n*4+400]
    s5=s[500+n*4:]
    #print(s1,s2,s3)


    b=bytearray([0 for x in range(n)])
    for z in range(1):
        for i in range(n):
            if s1[i]==s2[i] and s3[i]==s2[i] and s3[i]==s4[i] and s5[i]==s2[i]: b[i]=s1[i]
            else:
                x=0
                for j in range(8):
                    b1=s1[i]&l[j]
                    b2=s2[i]&l[j]
                    b3=s3[i]&l[j]
                    b4=s4[i]&l[j]
                    b5=s5[i]&l[j]
                    if (b1+b2+b3+b4+b5)>2*l[j]:x+=l[j]
                b[i]=x
    fileout.write(b)
