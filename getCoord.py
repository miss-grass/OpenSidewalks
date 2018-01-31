import numpy as np
import pandas as pd


def main():
    fields = ['exit_coord', 'transfer_coord', 'Walking_distance']
    df = pd.read_csv('API_Transfer_route.csv', skipinitialspace=True, usecols=fields, dtype=object)
    res = df[df['Walking_distance'] != 0]

    for index, row in res.iterrows():
        row['exit_coord'] = row['exit_coord'].replace("|", ",")
        row['transfer_coord']= row['transfer_coord'].replace("|", ",")

    res.pop('Walking_distance')
    print(res)
    np.save("coordinates.npy", res)




if __name__ == "__main__":
    main()

