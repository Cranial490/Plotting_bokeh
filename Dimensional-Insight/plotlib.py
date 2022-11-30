import itertools
from selenium.webdriver import Chrome

from bokeh.plotting import figure, show, save, output_file
from bokeh.io import export_svg, export_png
from bokeh.models import ColumnDataSource
from bokeh.models import Range1d

from bokeh.palettes import Spectral10


class Plot:
    def __init__(self, height=800, width=800, size=8, alpha=0.5, title = "Dummy Data",chromepath = '/home/cranial/chromedriver') -> None:
        self.height = height
        self.width = width
        self.size = size
        self.alpha = alpha
        self.title = title
        self.colorpalette = Spectral10
        self.web_driver = Chrome(executable_path=chromepath)

    def scatter(self, x , y, categories = None, x_label = "X axis", y_label = "Y axis", x_range = None, y_range = None, palette=None):
        p = figure(plot_width=self.width, plot_height=self.height, title=self.title)
        if x_range:
            p.x_range = Range1d(x_range[0], x_range[1])
        if y_range:
            p.y_range = Range1d(y_range[0], y_range[1])
        p.xaxis.axis_label = x_label
        p.yaxis.axis_label = y_label
        if categories:
            categorycolors = self.__create_color_map(categories, palette)
            source = ColumnDataSource(dict(x=x, y=y, color=categorycolors, label=categories))
            p.circle(x = 'x', y = 'y', color='color', fill_alpha=self.alpha, size=self.size, legend_group='label', source=source)
        else:
            p.circle(x , y , fill_alpha=self.alpha, size=self.size)
        return p

    def __create_color_map(self, categories, palette=None):
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
