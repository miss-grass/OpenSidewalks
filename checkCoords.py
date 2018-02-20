import numpy as np


def main():
    coord = np.load('coordinates.npy')
    for i in range(0, 100):
        print("the " + str(i) + "th coord")
        print(coord[i])
        print()
    print("there are totally " + str(coord.shape) + " lines")


if __name__ == '__main__':
    main()
