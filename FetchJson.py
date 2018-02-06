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
        data = requests.get('https://accessmap.io/api/v2/route.json?origin=' + origin + '&destination=' + dest).json()
        route = [item for item in data["routes"][0]["geometry"]["coordinates"]]
        edges[i] = route
        if i%100 == 0:
            print(str(i) + " steps finished!")

    np.save("edges", edges)
    print("finished! The edges of routes are stored in the edges.npy now!")


if __name__ == '__main__':
    main()
