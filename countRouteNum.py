import numpy as np
import pandas as pd
from numpy import math
s = 1
e = 7

def main():
    routes = np.load("acc_final_output/output_0-4800.npy")
    list = np.zeros((50, 1), dtype=int)
    for item in routes:
        num = int(item[4]) + int(item[5])
        if num < 50:
            list[num] += 1

    # print(list)
    print("the total number of routes: " + str(sum(list)))
    print("the total number of routes that have issues: " + str(sum(list[1:])))
    total = sum(list[s:e])
    print("the total number of routes that have less than " + str(e) + " issues: " + str(total))
    print("the percentage is: " + str(int(total)/int(sum(list[1:]))))


#4053

if __name__ == "__main__":
    main()

