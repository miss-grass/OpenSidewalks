import numpy as np
import pandas as pd
from numpy import math


def main():
    issues = pd.read_csv('SidewalkObservations.csv', skipinitialspace=True, dtype=object)

    for i in range(0, 21):
        x = np.load('issueTablesNewNew/output' + str(i) + '.npy')
        for j in range(0,x.shape[0]):
            if (len(x[j][2]) > 0):

                for k in range(0, len(x[j][2])):
                    issue = issues.iloc[[x[j][2][k]]]
                    if issue.OBSERV_TYPE.item() == 'SURFCOND':
                        if issue.SURFACE_CONDITION.item() == 'CRACK>72' \
                                or issue.SURFACE_CONDITION.item() == 'GAP':
                            # severe issue
                            x[j][4] += 1
                        elif issue.SURFACE_CONDITION.item() == 'CRACK<36':
                            # minor issue
                            x[j][5] += 1
                    elif issue.OBSERV_TYPE.item() == 'HEIGHTDIFF':
                        if float(issue.HEIGHT_DIFFERENCE.item()) >= 3.5:
                            # severe issue
                            x[j][4] += 1
                        elif float(issue.HEIGHT_DIFFERENCE.item()) <= 0.5:
                            # minor issue
                            x[j][5] += 1
                    elif issue.OBSERV_TYPE.item() == 'XSLOPE':
                        if abs(float(issue.ISOLATED_CROSS_SLOPE.item())) <= 1:
                            # monor issue
                            x[j][5] += 1
                        elif abs(float(issue.ISOLATED_CROSS_SLOPE.item())) >= 5:
                            # severe issue
                            x[j][4] += 1
                    elif issue.OBSERV_TYPE.item() == 'OBSTRUCT':
                        if issue.CLEARANCE_IMPACTED.item() == 'HORIZONTAL' \
                                and float(issue.MINIMUM_WIDTH) >= 20:
                            # severe issue
                            x[j][4] += 1
                        elif issue.CLEARANCE_IMPACTED.item() == 'HORIZONTAL' \
                                and float(issue.MINIMUM_WIDTH) <= 5:
                            # monor issue
                            x[j][5] += 1
                        elif issue.CLEARANCE_IMPACTED.item() == 'BOTH':
                            # severe issue
                            x[j][4] += 1
                dist = x[j][3]
                x[j][6] = float(x[j][4]) / dist
                x[j][7] = float(x[j][5]) / dist

        filename = "issueTablesComplete/output" + str(i) + ".npy"
        np.save(filename, x)












if __name__ == "__main__":
    main()

