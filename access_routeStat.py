import numpy as np
import pandas as pd
from numpy import math


delta = 0.000018
issues = pd.read_csv('SidewalkObservations.csv', skipinitialspace=True, dtype=object)
start_num = 0
end_num = 1000


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


def severity(AC):
    severe = 0
    minor = 0
    for k in range(0, len(AC)):
        issue = issues.iloc[[AC[k]]]
        if issue.OBSERV_TYPE.item() == 'SURFCOND':
            if issue.SURFACE_CONDITION.item() == 'CRACK>72' \
                    or issue.SURFACE_CONDITION.item() == 'CRACK<72' \
                    or issue.SURFACE_CONDITION.item() == 'GAP':
                # severe issue
                severe += 1
            else:
                # minor issue
                minor += 1
        elif issue.OBSERV_TYPE.item() == 'HEIGHTDIFF':
            if float(issue.HEIGHT_DIFFERENCE.item()) >= 3.5:
                # severe issue
                severe += 1
            else:
                # minor issue
                minor += 1
        elif issue.OBSERV_TYPE.item() == 'XSLOPE':
            if abs(float(issue.ISOLATED_CROSS_SLOPE.item())) >= 5:
                # severe issue
                severe += 1
            else:
                # minor issue
                minor += 1
        elif issue.OBSERV_TYPE.item() == 'OBSTRUCT':
            if issue.CLEARANCE_IMPACTED.item() == 'HORIZONTAL' \
                    and float(issue.MINIMUM_WIDTH) >= 20:
                # severe issue
                severe += 1
            elif issue.CLEARANCE_IMPACTED.item() == 'BOTH':
                # severe issue
                severe += 1
            else:
                # minor issue
                minor += 1
        else:
            # monor issue
            minor += 1

    return severe, minor


def main():
    issues = pd.read_csv('SidewalkObservations.csv', skipinitialspace=True, dtype=object)

    routes = np.load('OpenSidewalks/new_edges_data/edges_new.npy')
    grades = np.load('OpenSidewalks/new_edges_data/grades.npy')
    distances = np.load('OpenSidewalks/new_edges_data/distances.npy')

    result = np.zeros(((end_num - start_num), 10), dtype=object)

    for i in range(start_num, end_num):
        xs = routes[i][0][0]
        ys = routes[i][0][1]
        xe = routes[i][len(routes[i])-1][0]
        ye = routes[i][len(routes[i])-1][1]
        # start point
        result[i-start_num][0] = str(xs) + "," + str(ys)
        # end point
        result[i-start_num][1] = str(xe) + "," + str(ye)
        # set of points on the route
        result[i-start_num][2] = routes[i]
        # set of slope for each edge
        result[i-start_num][9] = grades[i]

        AC = []
        for j in range (0,len(routes[i]) - 1):
            x1 = routes[i][j][0]
            y1 = routes[i][j][1]
            x2 = routes[i][j+1][0]
            y2 = routes[i][j+1][1]

            mag = lineMagnitude(x1, y1, x2, y2)

            if mag > 0:
                for index, row in issues.iterrows():
                    px = float(row['Y'])
                    py = float(row['X'])
                    dist = DistancePointLine(px, py, x1, y1, x2, y2)
                    if dist <= delta:
                        # issue is in the range
                        AC.append(row['OBJECTID'])

            print('finish ', j, ' edge in ', i, ' route')

        # list of issue ids
        result[i-start_num][3] = AC

        severe, minor = severity(AC)
        # severe issue number
        result[i-start_num][4] = severe
        # minor issue number
        result[i-start_num][5] = minor

        # total distance
        dist = distances[i]
        result[i-start_num][6] = dist

        # severe issue number / meter
        if severe > 0:
            result[i-start_num][7] = float(severe) / float(dist)

        # severe issue number / meter
        if minor > 0:
            result[i-start_num][8] = float(minor) / float(dist)

        print(result[i])

    filename = "bigTable/output-" + str(start_num) + "-" + str(end_num) + ".npy"
    np.save(filename, result)


if __name__ == "__main__":
    main()

