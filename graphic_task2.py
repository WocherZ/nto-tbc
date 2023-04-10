from matplotlib import pyplot as plt
import numpy as np
import random


def get_colors_by_values(values):
        colors = []
        for value in values:
                colors.append(COLORS.get(value))
        return colors


START_STATE = 2

COLORS = {
        1: 'gray',
        0: '#000000',
        2: 'white'
}


f = open('msg.dat', 'r')

values = [START_STATE]
for i in range(100):
        val = int(f.read(1))
        print(val)
        values.append(val)

colors = get_colors_by_values(values)
print(colors)

graph_data = [3.5643564356435]
for i in range(100):
        graph_data.append(3.5643564356435)

# Creating plot
fig = plt.figure(figsize=(15, 10)) # 10 7
plt.pie(graph_data, colors=colors, counterclock=False)


print(values)

# show plot
plt.show()
plt.savefig('img.png')