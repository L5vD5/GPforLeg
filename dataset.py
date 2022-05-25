import os
from csv import reader
import numpy as np
if __name__ == "__main__":
    root_dir = "./ROSBAG/"
    data = np.array([[]])

    for (root, dirs, files) in os.walk(root_dir):
        print("# root : " + root)
        if len(dirs) > 0:
            for dir_name in dirs:
                print("dir: " + dir_name)

        if len(files) > 0:
            for file_name in files:
                print("file: " + file_name)
                if (file_name == 'Position.csv'):
                    with open(root+'/'+file_name, "r") as csv_file:
                        csv_reader = reader(csv_file)

                        for row in csv_reader:
                            # data = data[1:, 3:]
                            data = np.append([row], data)

    print(data)