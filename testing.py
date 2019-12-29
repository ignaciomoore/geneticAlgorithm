
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

    import plotly
    #from plotly.offline import iplot, init_notebook_mode, download_plotlyjs

    #init_notebook_mode(connected=True)

    df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28'),
          dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15'),
          dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30')]

    fig = ff.create_gantt(df)
    plotly.offline.plot(fig)
