import numpy as np

file = 'tracker.log'

N_BYTES = 26
#
# n = np.array([ord(z) for z in open(file, 'r').readline()])
#
# for i in n:
#   print(i, end=' ')


file_handler = open(file, "rb")

data_byte = file_handler.read(N_BYTES)

while data_byte:
    #print(int.from_bytes(data_byte, "big", signed="True"), end=' ')
    print(data_byte)
    print(int(data_byte) & 0x0fff)
    print(data_byte.decode('ascii').replace('\n', ''))
    value_in_string = data_byte.decode('ascii').replace('\n', '')
    print(int(value_in_string) & 0x0fff)
    #print(int(data_byte) & 0x0fff0000, int(data_byte) & 0x0fff)
    data_byte = file_handler.read(N_BYTES + 1)


# f = open("tracker.txt", "w+")
#
# for i in range(n.shape[0]):
#   f.write(str(n[i])+'\n')
#
# f.close()
#
# with open(file, "rb") as f:
#     array = []
#     f.readline()
#     while f.readline():
#         string_value = f.readline()
#         if string_value:
#             array.append(int(string_value))
#         # print(f.readline())
#     print(array)
