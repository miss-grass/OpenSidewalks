import numpy as np


def main():
    # routes = np.load('coordinates.npy')
    data = np.load('test.npy')
    # old = np.load('test 2.npy')
    # edges = np.load('edges.npy')
    for i in range(0, data.shape[0]):
        print(len(data[i]))
        print(data[i])
        # print(len(old[i]))
        # print(old[i])
        # print(routes[i])
        print()
        """
        for j in range(0, int(data[i].shape)):
            print(data[0][int(i*2)] + data[0][int(2*i+1)])
        """


if __name__ == '__main__':
    main()