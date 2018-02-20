import numpy as np


def main():
    edges = np.load('edges_new.npy')
    i = 1
    for edge in edges:
        print("the " + str(i) + "th route")
        print(edge)
        print()
        i += 1


if __name__ == '__main__':
    main()
