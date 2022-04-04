import bagpy
from bagpy import bagreader

b = bagreader('./1450_L_001.bag')
for t in b.topics:
    data = b.message_by_topic(t)
    print(data)