from turtle import color
from bokeh.plotting import figure, show, save, output_file
from bokeh.io import export_svg, export_png
import numpy as np
from datamanager import DataHandler
from bokeh.transform import factor_cmap
from bokeh.palettes import Spectral6

# N = 4000
# data  = [[0,1,3], [1,3,52], [0,4,76], [1,43,30]]
# # create a new plot with a title and axis labels
# p = figure(title="Multiple glyphs example", x_axis_label="x", y_axis_label="y")
# output_file(filename="custom_filename.html", title="Static HTML file")
# # add multiple renderers
# colors = ["red","yellow"]
# for d in data:
#     p.circle(d[1], d[0], radius=1, legend_label="Objects", line_color=colors[d[0]], size=12)
# # p.circle(x, y1, legend_label="Objects", color="black", size=12)

# # show the results
# # export_svg(p, filename="plot.svg")
# # export_png(p, filename="plot.png")
# show(p)
# # save(p)

from selenium.webdriver import Chrome, ChromeOptions

options = ChromeOptions()

options.add_argument('--headless')
options.add_argument("--window-size=2000x2000")
metrics = { "deviceMetrics": { "pixelRatio": 1.0 } }
options.add_experimental_option("mobileEmulation", metrics)
web_driver = Chrome(executable_path='/home/cranial/chromedriver')

import numpy as np

from bokeh.plotting import figure, show, output_file

dh = DataHandler()
data = dh.read_csv("dummyData.csv")

#removing header
data = data[1:]
categories = [row[0] for row in data]
id = [row[1] for row in data]
x = [row[2] for row in data][:100]
y = [row[3] for row in data][:100]
print(x)
categorySet = set(categories)
cmap = factor_cmap('Categories', palette=Spectral6, factors=list(categorySet))

p = figure(plot_width=600, plot_height=450, title="Dummy Data")

p.circle(x, y, color="black", fill_alpha=0.2)

show(p)
# from bokeh.io import export_png

# export_png(p, filename="out.png", webdriver=web_driver)