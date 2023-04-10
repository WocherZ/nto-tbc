import matplotlib.pyplot as plt

abs_coords = []
radar_statuses = []

radar_positions = []


with open('3.log', 'r') as file:
    lines = file.readlines()
    for i in range(len(lines)):
        current_line = lines[i].replace('\n', '')

        if i % 6 == 1:
            radar_statuses.append(int(current_line))

        if i % 6 == 2:
            radar_positions.append(int(current_line))

        if i % 6 == 4:
            abs_coords.append(int(current_line))


print(abs_coords)
# print(radar_statuses)

plt.plot(abs_coords)

plt.show()