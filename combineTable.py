import numpy as np
import pandas as pd

total_size = 4805
to_csv = False


def main():
    filename1 = 'final_output/output_1000-1300.npy'
    filename2 = 'final_output/output_1300-1700.npy'
    filename3 = 'final_output/output_1700-2000.npy'
    data1 = np.load(filename1)
    data2 = np.load(filename2)
    data3 = np.load(filename3)
    data = np.zeros(((data1.shape[0]+data2.shape[0]+data3.shape[0]), 10), dtype=object)
    i = 0
    for item in data1:
        data[i] = item
        i += 1
    for item in data2:
        data[i] = item
        i += 1
    for item in data3:
        data[i] = item
        i += 1
    df = pd.DataFrame(data)
    # print(df)
    start = int(filename1[20:int(filename1.index('-'))])
    end = int(filename3[(int(filename3.index('-'))+1):int(filename3.index('.'))])
    # print(start)
    # print(end)
    if to_csv:
        savename = 'final_output/output_' + str(start) + '-' + str(end) + '.csv'
        df.to_csv(savename, header=['starting coordinate', 'ending coordinate', 'vertices', 'issues ID',
                                    'severe issue', 'minor issue', 'total distance', 'ave_severe_issue/meter',
                                    'ave_minor_issue/meter', 'elevation'])

    else:
        savename = 'final_output/output_' + str(start) + '-' + str(end) + '.npy'
        np.save(savename, data)
        j = int(filename1[20:int(filename1.index('-'))])
        for item in data1:
            print("the " + str(j) + "th route:")
            print(item)
            print()
            print()
            j += 1
        for item in data2:
            print("the " + str(j) + "th route:")
            print(item)
            print()
            print()
            j += 1
        for item in data3:
            print("the " + str(j) + "th route:")
            print(item)
            print()
            print()
            j += 1


if __name__ == '__main__':
    main()
