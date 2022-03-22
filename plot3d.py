import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation
# steps = 512
def update(frame, csv_data, poses):
    # data = np.vstack((xlist[frame], ylist[frame]))
    # poses.set_offsets(data.T)
    # poses.set_3d_offsets(zlist[frame])
    xs = csv_data[frame].T[0]
    ys = csv_data[frame].T[1]
    zs = csv_data[frame].T[2]
    print(zs)
    poses._offsets3d = (xs, ys, zs)
    return poses#, lines

def main():
    csv_data = np.loadtxt('./MOCAP/test.csv', delimiter=',')
    xlist = []
    ylist = []
    zlist = []
    csv_data = csv_data.reshape(-1, 14, 3)
    csv_data = csv_data[0::100]
    print(csv_data.shape)
    len_data = len(csv_data)
    # print(type(data['xs']))
    xs = csv_data[0].T[0]
    ys = csv_data[0].T[1]
    zs = csv_data[0].T[2]
    # print(csv_data[0], xs)
    # zs = data['cs'][0: len(data['cs']): 10]

    #     xlist.append(xs)
    #     ylist.append(ys)
    #     zlist.append(zs)
    
    # # xlist = xlist[0: len(xlist): 50]
    # # ylist = ylist[0: len(ylist): 50]
    # # zlist = zlist[0: len(zlist): 50]
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.set_xlim([-2000, 2000])
    ax.set_ylim([0, 2000])
    ax.set_zlim([200, 2000])
    poses = ax.scatter(xs, ys, zs, c=range(len(zs)))
    # # lines, = ax.plot(xlist[0], ylist[0], zlist[0])


    ani = FuncAnimation(fig, update, fargs=[csv_data, poses], frames=range(len(csv_data)), interval=1)
    # # ani.save('exAnimation.gif', writer='imagemagick', fps=30, dpi=100)
    plt.show()


if __name__ == '__main__':
    main()
