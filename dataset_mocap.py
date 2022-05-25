import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation
from csv import reader

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
    csv_data = np.loadtxt('./Dataset/MOCAP/1450/L/1450_L_001.csv', delimiter=',', skiprows=1)
    csv_data = csv_data.reshape(-1, 45)
    time_data = csv_data[:,2]
    position_data = csv_data[:,3:]
    position_data = position_data.reshape(-1,14,3)
    print(time_data.shape)

    file_name = "./Dataset/ROSBAG/1450/L/1450_L_001/Position.csv"
    ros_time_data = np.loadtxt('./Dataset/ROSBAG/1450/L/1450_L_001/Position.csv', delimiter=',', skiprows=1, usecols=(0,))
    # print(ros_time_data)
    ros_csv_data = np.loadtxt('./Dataset/ROSBAG/1450/L/1450_L_001/Position.csv', delimiter=',', skiprows=1, usecols=tuple(range(3,15)))
    print(ros_csv_data.shape)

if __name__ == '__main__':
    main()
