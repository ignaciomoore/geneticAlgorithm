
import pandas as pd
import plotly.figure_factory as ff

def lineToArray(line):
    p = line.strip()
    nums = p.split(" ")
    while nums.__len__() > 15:
        nums.remove('')

    return list(map(int, nums))


def fileToDataFrame(file, tableSize):
    file.readline()

    timeData = []

    for i in range(tableSize):
        f = file.readline()
        f = lineToArray(f)
        timeData.append(f)

    time = pd.DataFrame(timeData)

    file.readline()

    machineData = []

    for i in range(tableSize):
        f = file.readline()
        f = lineToArray(f)
        machineData.append(f)

    mach = pd.DataFrame(machineData)

    return (time, mach)


if __name__ == "__main__":
    import numpy as np

    results = np.array()

    for i in range(5):
        results.append(i)
    print(results)
