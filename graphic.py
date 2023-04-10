import numpy as np

file = 'tracker.log'

# n = np.array([ord(z) for z in open(file, 'r').readline()])
#
# print(n)
#
# for i in n:
#   print(i, end=' ')


file_handler = open(file, "rb")

data_byte = file_handler.read(1)

while data_byte:
    print(int.from_bytes(data_byte, "big", signed="True"), end=' ')
    data_byte = file_handler.read(1)


# f = open("tracker.txt", "w+")
#
# for i in range(n.shape[0]):
#   f.write(str(n[i])+'\n')
#
# f.close()