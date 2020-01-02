
import pandas as pd
import plotly.figure_factory as ff

def lineToArray(line, numberOfMachines):
    p = line.strip()
    nums = p.split(" ")
    while nums.__len__() > numberOfMachines:
        nums.remove('')

    return list(map(int, nums))


def fileToDataFrame(file, numberOfJobs, numberOfMachines):
    file.readline()

    timeData = []

    for i in range(numberOfJobs):
        f = file.readline()
        f = lineToArray(f, numberOfMachines)
        timeData.append(f)

    time = pd.DataFrame(timeData)

    file.readline()

    machineData = []

    for i in range(numberOfJobs):
        f = file.readline()
        f = lineToArray(f, numberOfMachines)
        machineData.append(f)

    mach = pd.DataFrame(machineData)

    return (time, mach)


def getNumberOfJobs(filename):
    name = filename.split("_")
    name[1] = name[1][:-1]
    return int(name[1])


def getNumberOfMachines(filename):
    name = filename.split("_")
    mach = name[2].split(".")
    return int(mach[0][:-1])


if __name__ == "__main__":
    import numpy as np

    print(getNumberOfMachines("data_15J_15M.txt"))
