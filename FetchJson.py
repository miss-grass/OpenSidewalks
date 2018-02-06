"""
Wendong Cui, Zhu Li, Feb-2nd-2018, CSE495, OpenSideWalk

The python code to send url request and fetch Json package from accessMap.io,
and process it as available edges of starting point and destination point

"""

import numpy as np
import requests


def main():
    coords = np.load('coordinates.npy')
    edges = np.empty((coords.shape[0], 0)).tolist()

    for i in range(0, coords.shape[0]):
        origin = coords[i][0]
        dest = coords[i][1]
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
        edges[i] = rm_dup_route

        if i%100 == 0:
            print(str(i) + " steps finished!")

    np.save("edges", edges)
    print("finished! The edges of routes are stored in the edges.npy now!")


if __name__ == '__main__':
    main()
