import matplotlib.pyplot as plt

dx_values = []

with open('tracker.log', 'r') as file:
    for line in file.readlines()[1::]:
        values = line.replace('\n', '').split('\t')
        dx_values.append(int(values[1]))

plt.plot(dx_values)

plt.show()

print(dx_values)
