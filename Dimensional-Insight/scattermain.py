from Scatter import *
import argparse

from datamanager import DataHandler

parser = argparse.ArgumentParser(description='Generates scatter plot for a csv file')
parser.add_argument('--filename', type=str, required=True, help='input CSV or TXT file name')

args = parser.parse_args()
dh = DataHandler()

#Read csv or txt file and process
data = dh.read_data(args.filename)
#Remove header
data = data[1:]
#Process Data
categories = [row[0] for row in data]
id = [row[1] for row in data]
x=[float(row[2]) for row in data]
y=[float(row[3]) for row in data]

categorySet = list(set(categories))
colorMap = {}
colors = ["red", "blue", "green", "cyan", "black"]
for c in categorySet:
    colorMap[c] = colors.pop()

window = Plot()
window.scatter(x, y, categories, colorMap)
window.show()
app.exec_()