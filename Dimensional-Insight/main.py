import argparse

from datamanager import DataHandler
from plotlib import Plot

parser = argparse.ArgumentParser(description='Generates scatter plot for a csv file')
parser.add_argument('--filename', type=str, required=True, help='input CSV or TXT file name')
parser.add_argument('--outputfile', type=str, required=False, help='file name for the plot')
parser.add_argument('--outputtype', type=str, required=False, help='export type options HTML, PNG, SVG')
parser.add_argument('--chromepath', type=str, required=False, help='path to chromedriver executable')
parser.add_argument('-s', action='store_true', help='Flag to visualize plot')
parser.add_argument('-g', action='store_true', help='Generate new dummy data')

args = parser.parse_args()

dh = DataHandler()

# Generate CSV file with random data
if args.g:
    dh.generate_dummy_data("dummy.csv", categories=["A", "G", "B", "C","F"], datapoints=1000)

#Read csv or txt file and process
data = dh.read_data(args.filename)
#Remove header
data = data[1:]
#Process Data
categories = [row[0] for row in data]
id = [row[1] for row in data]
x=[float(row[2]) for row in data]
y=[float(row[3]) for row in data]

if args.chromepath:
    plt = Plot(args.chromepath)
else:
    plt = Plot()
    
#Generate scatter plot
p = plt.scatter(x,y, categories=categories)

if args.outputtype:
    plt.output_plot(p, args.outputfile, args.outputtype.lower())
if args.s:
    plt.show(p)