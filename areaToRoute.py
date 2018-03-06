import numpy as np
import pandas as pd
from numpy import math


delta = 500

def mToLat(m):
    return 1.0 / 110540 * m


def mToLong(m, lat):
    return -1.0 / (111320 * math.cos(lat)) * m


def colorIndex(s, m):
    n = s * 1000 + m * 100
    # exist severe --> 4
    if s > 0:
        return 4
    # 0 --> 0
    if (n == 0):
        return 0
    # 0-1 --> 1
    elif (n <= 1):
        return 1
    # 1-5 --> 2
    elif (n <= 5):
        return 2
    # 5-10 --> 3
    elif (n <= 10):
        return 3
    # >10 --> 4
    else:
        return 4


def main():
    df = pd.read_csv('acc_final_output/output_0-4800.csv', skipinitialspace=True, dtype=object)
    lat = 47.64981280000001
    long = -122.3037817
    bfX = mToLat(delta)
    bfY = mToLong(delta, lat)
    x1 = lat - bfX
    x2 = lat + bfX
    y1 = long - bfY
    y2 = long + bfY

    result = np.zeros((47, 4), dtype=object)

    cnt = 0
    for index, row in df.iterrows():
        coord = row['starting coordinate'].split(',')
        x = float(coord[0])
        y = float(coord[1])
        coordE = row['ending coordinate'].split(',')
        xE = float(coordE[0])
        yE = float(coordE[1])
        if x >= x1 and x <= x2 and y >= y1 and y <= y2 and \
                        xE >= x1 and xE <= x2 and yE >= y1 and yE <= y2:

            result[cnt][0] = row['starting coordinate']
            result[cnt][1] = row['ending coordinate']
            result[cnt][2] = row['vertices']
            result[cnt][3] = colorIndex(float(row['ave_severe_issue/meter']), float(row['ave_minor_issue/meter']))
            #print(cnt, ':', x, print(row)
            cnt += 1

    print(result)
    filename = "acc_final_output/visualize.npy"
    np.save(filename, result)

if __name__ == "__main__":
    main()

