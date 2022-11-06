import itertools
from selenium.webdriver import Chrome

from bokeh.plotting import figure, show, save, output_file
from bokeh.io import export_svg, export_png
from bokeh.models import ColumnDataSource
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

    def scatter(self, x , y, categories = None, palette=None):
        p = figure(plot_width=self.width, plot_height=self.height, title=self.title)
        if categories:
            categorycolors = self.__create_color_map(categories)
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
