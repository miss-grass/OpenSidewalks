import numpy as np
import pandas as pd
from numpy import math


delta = 0.000018

# Source: https://nodedangles.wordpress.com/2010/05/16/measuring-distance-from-a-point-to-a-line-segment/
def lineMagnitude (x1, y1, x2, y2):
    lineMagnitude = np.math.sqrt(np.math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
    return lineMagnitude

# Compute minimum distance from a point and a line segment
def DistancePointLine(px, py, x1, y1, x2, y2):
    LineMag = lineMagnitude(x1, y1, x2, y2)

    if LineMag < 0.0000000001:
        DistancePointLine = 9999
        return DistancePointLine

    u1 = (((px - x1) * (x2 - x1)) + ((py - y1) * (y2 - y1)))
    u = u1 / (LineMag * LineMag)

    if (u < 0.00001) or (u > 1):
        # // closest point does not fall within the line segment, take the shorter distance
        # // to an endpoint
        ix = lineMagnitude(px, py, x1, y1)
        iy = lineMagnitude(px, py, x2, y2)
        if ix > iy:
            DistancePointLine = iy
        else:
            DistancePointLine = ix
    else:
        # Intersecting point is on the line, use the formula
        ix = x1 + u * (x2 - x1)
        iy = y1 + u * (y2 - y1)
        DistancePointLine = lineMagnitude(px, py, ix, iy)

    return DistancePointLine


def main():
    issues = pd.read_csv('SidewalkObservations.csv', skipinitialspace=True, dtype=object)

    routes = np.load('test.npy')

    for i in range(0,routes.shape[0]):
        result = np.zeros((len(routes[i])-1,5), dtype=object)
        for j in range (0,len(routes[i]) - 1):
            y1 = routes[i][j][0]
            x1 = routes[i][j][1]
            y2 = routes[i][j+1][0]
            x2 = routes[i][j+1][1]
            result[j][0] = str(x1) + "," + str(y1)
            result[j][1] = str(x2) + "," + str(y2)
            result[j][3] = lineMagnitude(x1, y1, x2, y2)
            AC = []
            for index, row in issues.iterrows():
                px = float(row['Y'])
                py = float(row['X'])
                dist = DistancePointLine(px, py, x1, y1, x2, y2)
                if dist <= delta:
                    # issue is in the range
                    AC.append(str(px) + "," + str(py))
            result[j][4] = AC
            print('finish ', j, ' edge in ', i, ' route')

        filename = "output"+str(i)+".npy"
        np.save(filename, result)





if __name__ == "__main__":
    main()

