import csv
import pandas as pd
import random
import statistics
import plotly.figure_factory as ff
df=pd.read_csv("data.csv")
data=df["temp"].tolist()
print("mean",statistics.mean(data))
print("standard deviation",statistics.stdev(data))
fig=ff.create_distplot([data],["temp"],show_hist=False)
fig.show()