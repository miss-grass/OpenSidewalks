import numpy as np
import matplotlib.pyplot as plt
num = False

data = np.load('acc_final_output/output_0-4800.npy')

g1 = []
for item in data:
    if item[6] < 1000:
        if num:
            number = item[4]*2 + item[5]
            g1.append(int(number))
        else:
            number = item[7]*1000 + item[8]*100
            g1.append(number)

if num:
    bins = np.arange(1, 25)
    plt.xlabel('number of issues')
    plt.ylabel('frequency')
    plt.hist(g1, bins=bins)  # arguments are passed to np.histogram
    plt.title("Histogram of issue numbers on route")
    plt.savefig('issue_num')
else:
    bins = np.arange(1, 20)
    plt.xlabel('ave_number of issues/meter')
    plt.ylabel('frequency')
    plt.hist(g1, bins=bins)  # arguments are passed to np.histogram
    plt.title("Histogram of average issue numbers per meter on route")
    plt.savefig('issue_ave_num')




