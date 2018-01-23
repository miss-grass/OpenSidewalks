import numpy as np
import pandas as pd
import geopandas as gpd
from geopandas import GeoDataFrame
from shapely.geometry import Point
from shapely.geometry import LineString
from shapely.geometry import Polygon
import re


def get_geometry(df):
    points = df.points
    geometry = np.zeros(points.shape[0], dtype=object)
    for i in range(0, points.shape[0]):
        pt = points[i]
        pt = re.sub('[[\]\']', '', pt)
        pt = pt.split(',')
        geometry[i] = list(set(pt))

    for i in range(0, geometry.shape[0]):
        if len(geometry[i]) == 1:
            geometry[i] = Polygon([(0, 0), (0, 0), (0, 0)])
        else:
            route = geometry[i]
            pointList = np.zeros(len(route), dtype=Point)
            for j in range(0, len(route)):
                pt = route[j].split('|')

                pointList[j] = Point(float(pt[0]), float(pt[1]))
            poly = Polygon([[p.x, p.y] for p in pointList])
            geometry[i] = poly

    return geometry

def get_convex_hull(gdf):
    ch = gdf.convex_hull
    df = pd.DataFrame({"convex hull": ch})
    df.to_csv("convex hull", index=False)  # write to file for checking

    return ch


def get_centroid(ch):
    cent = ch.centroid

    df = pd.DataFrame({"centroid": cent})
    df.to_csv("centroid", index=False)  # write to file for checking

    return cent


def main():
    df = pd.read_csv("API_Transfer_route.csv")

    geometry = get_geometry(df)

    crs = {'init': 'epsg:4326'}
    gdf = GeoDataFrame(df, crs=crs, geometry=geometry)

    gdf.to_file("output2")

    ch = get_convex_hull(gdf)
    print(type(ch))

    cent = get_centroid(ch)
    print(cent)






if __name__ == "__main__":
    main()