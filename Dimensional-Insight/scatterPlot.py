import itertools
from turtle import color
from bokeh.plotting import figure, show, save, output_file
from bokeh.io import export_svg, export_png
import numpy as np
from datamanager import DataHandler
from bokeh.transform import factor_cmap
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral6, Spectral10
from selenium.webdriver import Chrome, ChromeOptions
from bokeh.io import export_png, export_svg
class Plot:
    def __init__(self) -> None:
        self.colorpalette = Spectral10
        options = ChromeOptions()
        self.web_driver = Chrome(executable_path='/home/cranial/chromedriver')

    def scatter(self, x , y, categories = None, palette=None):
        p = figure(plot_width=1000, plot_height=800, title="Dummy Data")
        if categories:
            categorycolors = self.create_color_map(categories)
            source = ColumnDataSource(dict(x=x, y= y, color=categorycolors, label=categories))
            p.circle(x = 'x', y = 'y', color='color', fill_alpha=0.4, size=8, legend_group='label', source=source)
        else:
            p.circle(x , y , fill_alpha=0.4, size=8)
        return p

    def create_color_map(self, categories, palette=None):
        if palette:
            self.colorpalette = palette
        categorySet = list(set(categories))
        colorPallete = itertools.cycle(self.colorpalette)
        colorMap = {}
        idx = 0
        for shade in colorPallete:
            if idx >= len(categorySet):
                break
            colorMap[categorySet[idx]] = shade
            idx += 1
        return [colorMap[x] for x in categories]

    def output_plot(self, p, filename="plot", type="html"):
        if type == "png":
            export_png(p, filename=filename+'.'+type, webdriver=self.web_driver)
        elif type == "svg":
            export_svg(p, filename=filename+'.'+type, webdriver=self.web_driver)
        else:
            output_file(filename =filename+'.'+type, title="Static HTML file")
            save(p)
    def show(self, plot):
        show(plot)

    
    