from datamanager import DataHandler
from scatterPlot import Plot

dh = DataHandler()
data = dh.read_csv("dummyData1.csv")
data = data[1:]
categories = [row[0] for row in data]   
id = [row[1] for row in data]
x=[row[2] for row in data]
y=[row[3] for row in data]

plt = Plot()
p = plt.scatter(x,y, categories)
plt.show(p)