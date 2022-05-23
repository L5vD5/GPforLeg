import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation
import matplotlib.ticker as MaxNLocator

from csv import reader


def main():
    file_name = "./ROSBAG/1450_R_000/Position.csv"
    data = []
    with open(file_name, "r") as csv_file:
        csv_reader = reader(csv_file)

        for row in csv_reader:
            data.append(row)
    data = np.array(data)
    header = data[0]
    time = data[1:, 0]
    data = data[1:, 3:]
    print(time.shape, data.shape)
    fig = plt.figure()
    ax = fig.add_subplot()

    # plot = ax.plot(np.asarray(data[:, 0], float))
    plot = ax.plot(np.asarray(data[:, 6], float))

    plt.show()


if __name__ == '__main__':
    main()
