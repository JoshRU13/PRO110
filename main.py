import csv
import pandas as pd
import random
import statistics
import plotly.figure_factory as ff
df=pd.read_csv("data.csv")
data=df["temp"].tolist()
def randomset(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean
def showfig(meanlist):
    df=meanlist
    mean=statistics.mean(df)
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.show()
def setup():
    meanlist=[]
    for i in range(0,1000):
        setupmean=randomset(100)
        meanlist.append(setupmean)
    mean=statistics.mean(meanlist)
    print("sampling mean",mean)
    std=statistics.stdev(meanlist)
    print("sampling deviation",std)
setup()
    
