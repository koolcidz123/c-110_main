import csv
import random
import statistics
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

df = pd.read_csv("newdata.csv")
average_list = df["average"].tolist()
PopulationMean = statistics.mean(average_list)
PopulationStandard = statistics.stdev(average_list)

print("Population - ", PopulationMean, PopulationStandard)
fig = ff.create_distplot([average_list], ["Average"], show_hist= False)
fig.show()


def getSample(counter):
    dataSet = []
    for i in range(0,counter):
        randomeIndex = random.randint(0, len(average_list)-1)
        value = average_list[randomeIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean


def showFig(meanList):
    mean = statistics.mean(meanList)
    stdv = statistics.stdev(meanList)

    print("Sampling mean and stdv", mean, stdv)
    figure = ff.create_distplot([meanList], ["MEAN"], show_hist=False)
    figure.add_trace(go.Scatter(x=[mean, mean], y=[0, 12], mode="lines", name="MEAN"))
    figure.show()

def setUp():
    meanList = []
    for i in range(0,1000):
        mean = getSample(100)
        meanList.append(mean)
    showFig(meanList)


setUp()
