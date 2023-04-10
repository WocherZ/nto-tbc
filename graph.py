import numpy as np
f = open('gears.dat','r')
times = []
r1s, r2s, r3s = [], [], []
f.readline()
prev_line = ''
for line in f.readlines():
    if line != '':
        time, r1, r2, r3 = line.split()
        times.append(time)
        r1s.append(int(r1))
        r2s.append(int(r2))
        r3s.append(int(r3))
data = r1s

a = -11
b = 20
k = 81
new_times = [times[val] for val in
             np.linspace(np.argmax(r1s) + a, np.argmax(r1s) + 3105 + a + b, 102).round().astype(int)]
new_data = [data[val] for val in
            np.linspace(np.argmax(r1s) + a, np.argmax(r1s) + 3105 + a + b, 102).round().astype(int)]

np_data = np.array(new_data[1:-1])
np_data[np_data <= k] = 0
np_data[np_data > k] = 1


f = open('output.dat', 'w')
f.write("".join(str(i) for i in np_data))