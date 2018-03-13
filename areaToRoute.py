import numpy as np
from numpy import math

final_lat = 47.6498128
final_long = -122.3037817
delta = 500


def m_to_lat(m):
    return 1.0 / 110540 * m


def m_to_long(m, lat):
    return -1.0 / (111320 * math.cos(lat)) * m


def color_index(s, n):
    # exist severe --> 4
    if s > 0:
        return 4
    # 0 --> 0
    if n == 0:
        return 0
    # 0-3 --> 1
    elif n <= 3:
        return 1
    # 3-5 --> 2
    elif n <= 5:
        return 2
    # 5-8 --> 3
    elif n <= 8:
        return 3
    # >8 --> 4
    else:
        return 4


def main():
    data = np.load('acc_final_output/output_0-4800.npy')
    bfX = m_to_lat(delta)
    bfY = m_to_long(delta, final_lat)
    x1 = final_lat - bfX
    x2 = final_lat + bfX
    y1 = final_long - bfY
    y2 = final_long + bfY

    routes = []
    inds = []
    for route in data:
        x = float(route[0].split(',')[0])
        y = float(route[0].split(',')[1])
        xE = float(route[1].split(',')[0])
        yE = float(route[1].split(',')[1])
        # we want this route
        if x1 <= x <= x2 and y1 <= y <= y2 and x1 <= xE <= x2 and y1 <= yE <= y2:
            ind = color_index(route[4], route[5])
            routes.append(route[2])
            inds.append(ind)
            print(route[2])
            print(ind)
            print()
    """
    filename = "acc_final_output/visualize.npy"
    np.save(filename, result)
    """

if __name__ == "__main__":
    main()

