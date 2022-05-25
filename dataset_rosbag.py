import os
from csv import reader
import numpy as np

SAVE = False
if __name__ == "__main__":
    root_dir = "./Dataset/ROSBAG/1450/L"
    data = np.empty(shape=(0,12))

    for (root, dirs, files) in os.walk(root_dir):
        print("# root : " + root)
        # if "1450" not in root:
        #     continue
        dirs.sort()
        if len(dirs) > 0:
            for dir_name in dirs:
                print("dir: " + dir_name)

        if len(files) > 0:
            for file_name in files:
                print("file: " + file_name)
                if (file_name == 'Position.csv'):
                    csv_data = np.loadtxt(root+'/'+file_name, delimiter=',', skiprows=1, usecols=tuple(range(3,15)))
                    print(csv_data.shape)
                    data = np.append(data, csv_data, axis=0)

    if SAVE:
        np.save('positionL.npy', data)