import numpy as np


def main():
    elevs = np.load('elevations.npy')
    i = 1
    for elev in elevs:
        print("the " + str(i) + "th elev")
        print(elev)
        print()
        i += 1


if __name__ == '__main__':
    main()
