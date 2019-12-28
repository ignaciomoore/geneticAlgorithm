
import pandas as pd

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

    file = open("data.txt", "r")

    data = fileToDataFrame(file, 15)

    print(data[0])
    print(data[1])