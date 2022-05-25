import bagpy
from bagpy import bagreader
from os.path import isfile, join
from os import listdir

ros_path = './ROSBAG'
onlyfiles = [ros_path + '/' + f for f in listdir(ros_path) if isfile(join(ros_path, f))]
for filename in onlyfiles:
    print(filename)
    b = None
    try:
        b = bagreader(filename)
        for t in b.topics:
            data = b.message_by_topic(t)
            print(data)
    except:
        print('Error')
