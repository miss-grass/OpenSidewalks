import numpy as np


def main():
    dists = np.load('distances.npy')
    i = 1
    for dist in dists:
        print("the " + str(i) + "th distance")
        print(dist)
        print()
        i += 1


if __name__ == '__main__':
    main()
