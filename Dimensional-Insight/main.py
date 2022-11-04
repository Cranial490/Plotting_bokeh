import argparse
from datamanager import DataHandler
from scatterPlot import Plot
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--filename', type=str, required=True, help='Input CSV file name')
parser.add_argument('--outputfile', type=str, required=True, help='output file name for the plot')
parser.add_argument('--outputtype', type=str, required=False, help='export type for plot')

args = parser.parse_args()

dh = DataHandler()

dh.generate_dummy_data("dummy.csv", datapoints= 100000, categories=["A", "B", "C", "D", "E", "F", "G"])

data = dh.read_csv(args.filename)
data = data[1:]
categories = [row[0] for row in data]   
id = [row[1] for row in data]
x=[row[2] for row in data]
y=[row[3] for row in data]

plt = Plot()
p = plt.scatter(x,y, categories)

if args.outputtype:
    plt.output_plot(p, args.outputfile, args.outputtype)
else:
    plt.show(p)