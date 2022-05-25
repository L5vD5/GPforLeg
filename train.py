import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation
# steps = 512

def main():
    velocityL = np.load('./Dataset/Raw/1450/velocityL.npy')
    velocityR = np.load('./Dataset/Raw/1450/velocityR.npy')
    positionL = np.load('./Dataset/Raw/1450/positionL.npy')
    positionR = np.load('./Dataset/Raw/1450/positionR.npy')

    print(velocityL.shape, velocityR.shape, positionL.shape, positionR.shape)

if __name__ == '__main__':
    main()
