import plotly.figure_factory as ff 
import statistics
import pandas as pd
import csv
import random
import plotly.graph_objects as go

f = pd.read_csv('medium_data.csv')
data = f["claps"].tolist()
mean = statistics.mean(data)
stdev = statistics.stdev(data)
st1start, st1end = mean-stdev, mean+stdev
st2start, st2end = mean-(2*stdev), mean+(2*stdev)
st3start, st3end = mean-(3*stdev), mean+(3*stdev)
print(mean, stdev)

def randommeans(n):
    dataset = []
    for i in range(0, n):
        r = random.randint(0, len(data)-1)
        dataset.append(data[r])
    mean = statistics.mean(dataset)
    return mean

def graph(data, mean2):
    fig = ff.create_distplot([data], ["claps"], show_hist = False)
    fig.add_trace(go.Scatter(x=[mean, mean], y = [0, 0.17], mode='lines', name = "mean"))
    fig.add_trace(go.Scatter(x=[mean2, mean2], y = [0, 0.17], mode='lines', name = "mean 2"))
    fig.add_trace(go.Scatter(x=[st1start, st1start], y=[0, 0.17], mode= 'lines', name = "1st standard dev"))
    fig.add_trace(go.Scatter(x=[st2start, st2start], y=[0, 0.17], mode= 'lines', name = "2nd standard dev"))
    fig.add_trace(go.Scatter(x=[st3start, st3start], y=[0, 0.17], mode= 'lines', name = "3rd standard dev"))
    fig.add_trace(go.Scatter(x=[st3end, st3end], y=[0, 0.17], mode= 'lines', name = "3rd standard dev end"))
    fig.add_trace(go.Scatter(x=[st2end, st2end], y=[0, 0.17], mode= 'lines', name = "2nd standard dev end"))
    fig.add_trace(go.Scatter(x=[st1end, st1end], y=[0, 0.17], mode= 'lines', name = "1st standard dev end"))
    fig.show()

def st():
    meanlist = []
    for i in range(0, 100):
        m = randommeans(30)
        meanlist.append(m)
    stdev2 = statistics.stdev(meanlist)
    print(stdev2)
    samplemean = statistics.mean(meanlist)
    print("z score: ", (samplemean-mean)/stdev)
    graph(meanlist, samplemean)

st()
