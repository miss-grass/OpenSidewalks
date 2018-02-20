"""
Wendong Cui, Zhu Li, Feb-19th-2018, CSE495, OpenSideWalk

The python code to send url request and fetch Json package from googleMap.api,
and process it as available edges of starting point and destination point

"""

import numpy as np
import requests


def main():
    coords = np.load('coordinates.npy')
    # the data of routes representing by edges
    edges = np.empty((coords.shape[0], 0)).tolist()
    # the data of elevations of each routes
    elevs = np.empty((coords.shape[0], 0)).tolist()
    # the data of distances for all routes
    dists = np.zeros(coords.shape[0])

    for i in range(0, coords.shape[0]):
        # the total distance of current route
        dist = 0
        # the list of route with points and edges
        route = []
        # the locations parameter for http request
        locations = ''
        # the list of elevations at each point of the route
        elev = []
        origin = coords[i][0]
        dest = coords[i][1]
        # get json response of routes from google map
        data_route = requests.get('https://maps.googleapis.com/maps/api/directions/json?alternatives=false'
                                  '&origin=' + origin + '&destination=' + dest +
                                  '&key=AIzaSyDreETIISig2mIIfjBxyHF9_BIjjrmYyLc&mode=walking').json()

        try:
            dist = data_route["routes"][0]["legs"][0]["distance"]["value"]
            for item in data_route["routes"][0]["legs"][0]["steps"]:
                start = (round(float(item['start_location']['lat']), 12), round(float(item['start_location']['lng']), 12))
                end = (round(float(item['end_location']['lat']), 12), round(float(item['end_location']['lng']), 12))
                route.append(start)
                route.append(end)
        except:
            # if any error happens, just take the starting and end points as the only edge
            x1 = round(float(origin.split(",")[0]), 12)
            y1 = round(float(origin.split(",")[1]), 12)
            x2 = round(float(dest.split(",")[0]), 12)
            y2 = round(float(dest.split(",")[1]), 12)
            route = [(x1, y1), (x2, y2)]

        # remove the duplicated points
        rm_dup_route = list(dict.fromkeys(route))
        # deal with the case that the two points are overlap
        if len(rm_dup_route) == 1:
            x1 = round(float(origin.split(",")[0]), 12)
            y1 = round(float(origin.split(",")[1]), 12)
            x2 = round(float(dest.split(",")[0]), 12)
            y2 = round(float(dest.split(",")[1]), 12)
            rm_dup_route = [(x1, y1), (x2, y2)]
        # cast the route into locations string to get elevation
        for coord in rm_dup_route:
            locations += (str(coord[0]) + ',' + str(coord[1]))
            locations += '|'
        locations = locations[:-1]
        # print(locations)

        # get json response of elevations from google map
        try:
            data_elevation = requests.get('https://maps.googleapis.com/maps/api/elevation/json?'
                                          'locations=' + locations +
                                          '&key=AIzaSyDreETIISig2mIIfjBxyHF9_BIjjrmYyLc').json()
            for item in data_elevation["results"]:
                elev.append(item['elevation'])
        except:
            elev = [0]

        # print(rm_dup_route)
        # print(dist)
        # print(elev)
        edges[i] = rm_dup_route
        dists[i] = dist
        elevs[i] = elev

        print(str(i) + "th route finished!")

    # np.save("new_edges_data/edges_new_test", edges)
    # np.save("new_edges_data/distances_test", dists)
    # np.save("new_edges_data/elevations_test", elevs)
    np.save("new_edges_data/edges_new", edges)
    np.save("new_edges_data/distances", dists)
    np.save("new_edges_data/elevations", elevs)
    print("finished! The edges of routes are stored in the edges.npy now!")


if __name__ == '__main__':
    main()
