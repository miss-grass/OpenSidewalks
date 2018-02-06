"""
Wendong Cui, Zhu Li, Feb-2nd-2018, CSE495, OpenSideWalk

Fetch the top 20 routes's edges from AccessMap.io

"""

import numpy as np
import requests


def main():
    coords = np.load('coordinates.npy')
    test = np.empty((20, 0)).tolist()

    for i in range(0, 20):
        origin = coords[i][0]
        dest = coords[i][1]
        # print(origin)
        # print(dest)
        data = requests.get('https://accessmap.io/api/v2/route.json?maxdown=-0.1&ideal=-0.01&&maxup=0.1&origin='
                            + origin + '&destination=' + dest + '&avoid=construction').json()
        try:
            route = [(float(item[1]), float(item[0])) for item in data["routes"][0]["geometry"]["coordinates"]]
        except TypeError:
            x1 = round(float(origin.split(",")[0]), 7)
            y1 = round(float(origin.split(",")[1]), 7)
            x2 = round(float(dest.split(",")[0]), 7)
            y2 = round(float(dest.split(",")[1]), 7)
            route = [(x1, y1), (x2, y2)]

        # remove the duplicated points
        rm_dup_route = list(dict.fromkeys(route))
        test[i] = rm_dup_route

        print("route " + str(i+1) + ", " + str(len(rm_dup_route)) + " points")
        print()
    np.save("test", test)
    print("finished! The edges of test 20 routes are stored in the test.npy now!")


if __name__ == '__main__':
    main()
