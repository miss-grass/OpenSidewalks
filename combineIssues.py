import numpy as np
import pandas as pd

to_csv = True


def main():
    filename1 = 'acc_final_output/newIssues_0-4000.npy'
    filename2 = 'acc_final_output/newIssues_4000-4800.npy'
    data1 = np.load(filename1)
    data2 = np.load(filename2)
    data = np.empty(((data1.shape[0]),0)).tolist()

    for i in range(0, data1.shape[0]):
        if len(data1[i]) == 0:
            data[i] = data2[i]
        elif len(data2[i]) == 0:
            data[i] = data1[i]
        else:
            data[i] = data1[i] + data2[i]

    df = pd.DataFrame(data)

    start = int(filename1[27:int(filename1.index('-'))])
    end = int(filename2[(int(filename2.index('-'))+1):int(filename2.index('.'))])

    if to_csv:
        savename = 'acc_final_output/newIssues_' + str(start) + '-' + str(end) + '.csv'
        df.to_csv(savename)

    else:
        savename = 'acc_final_output/newIssues_' + str(start) + '-' + str(end) + '.npy'
        np.save(savename, data)
        j = int(filename1[27:int(filename1.index('-'))])
        print(j)
        
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


if __name__ == '__main__':
    main()
