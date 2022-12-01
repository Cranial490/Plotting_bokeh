from operator import xor
from re import X
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Plot(QtWidgets.QMainWindow):
    def __init__(self, height=1000, width=1000, padding = 200):
        super().__init__()
        self.label = QtWidgets.QLabel()
        self.pen = QtGui.QPen()
        self.plotheight = height
        self.plotwidth = width
        self.padding = padding
        self.gridmin = 0
        self.gridmax = self.plotheight - 2*self.padding
        self.initCanvas()

    def getscale(self,x, datamin, datamax, gridmin, gridmax):
      dataRange = datamax - datamin
      if(dataRange == 0):
          print("range error")
          exit()
      else:
          gridRange = gridmax - gridmin
          return (((x - datamin)*gridRange)/dataRange) + gridmin

    def getposition(self,x,y,xorigin,yorigin):
        return (xorigin+x, yorigin-y)

    def initCanvas(self):
      canvas = QtGui.QPixmap(self.plotheight, self.plotwidth)
      canvas.fill(QtGui.QColor("white"))
      self.label.setPixmap(canvas)
      self.setCentralWidget(self.label)

    def getMultiple(self, range):
      return range//10

    def drawPlot(self,painter,xorigin,yorigin):
      painter.drawLine(QtCore.QLineF(xorigin, yorigin, xorigin, yorigin-(self.gridmax+50)))
      painter.drawLine(QtCore.QLineF(xorigin, yorigin, xorigin + self.gridmax+50,yorigin))

    def drawMarkings(self,painter,axismax,axismin,xorigin,yorigin,axis=1):
      axisrange = axismax-axismin
      marker = self.getMultiple(axisrange)
      axismark = axismin + marker
      pad = 30
      while True:
        if axismark <= axismax:
          point = self.getscale(axismark, axismin, axismax, self.gridmin, self.gridmax)
          if axis:
            xGrid, yGrid = self.getposition(0,point, xorigin-pad, yorigin)
          else:
            xGrid, yGrid = self.getposition(point,0, xorigin, yorigin+pad)

          self.pen.setWidth(2)
          self.pen.setColor(QtGui.QColor('#5D6D7E'))
          painter.setPen(self.pen)
          if axis:
            painter.drawLine(QtCore.QLineF(xGrid, yGrid, xGrid-8, yGrid))
            painter.drawText(QtCore.QPointF(xGrid-35,yGrid), str(int(axismark)))
            self.pen.setWidth(1)
            self.pen.setColor(QtGui.QColor('#D0D9E3'))
            painter.setPen(self.pen)
            painter.drawLine(QtCore.QLineF(xGrid, yGrid, xGrid+self.gridmax+pad, yGrid))
          else:
            painter.drawLine(QtCore.QLineF(xGrid, yGrid, xGrid, yGrid+8))
            painter.drawText(QtCore.QPointF(xGrid,yGrid+20), str(int(axismark)))
            self.pen.setWidth(1)
            self.pen.setColor(QtGui.QColor('#D0D9E3'))
            painter.setPen(self.pen)
            painter.drawLine(QtCore.QLineF(xGrid, yGrid, xGrid, yGrid-(self.gridmax+pad)))
          axismark += marker
        else:
          break
    
    def drawCircles(self,painter,xdata,ydata,categdata,xmin,xmax,ymin,ymax,xorigin,yorigin, colorMap):
        for i in range(len(xdata)):
          self.pen.setWidth(10)
          self.pen.setColor(QtGui.QColor(colorMap[categdata[i]]))
          painter.setPen(self.pen)
          x,y = self.getposition(self.getscale(xdata[i],xmin,xmax,self.gridmin,self.gridmax),self.getscale(ydata[i],ymin,ymax,self.gridmin,self.gridmax), xorigin,yorigin)
          painter.drawPoint(QtCore.QPointF(x,y))
          self.pen.setColor(QtGui.QColor("black"))
          painter.setPen(self.pen)
          painter.drawEllipse(QtCore.QPointF(x,y), 1,1)

    def getColorMap(self,categories):
        categorySet = list(set(categories))
        colorMap = {}
        colors = ["#922B21", "#2471A3", "#239B56", "#76D7C4", "#F39C12", "#2C3E50", "#4A235A", "#0B5345", "#6E2C00"]
        col = 0
        if len(colors) < len(categorySet):
            print("Too many categories for now")
            exit()
        for c in categorySet:
            colorMap[c] = colors[col]
            col += 1
        return colorMap

    def scatter(self, xdata, ydata, categories=None):
        xmin = min(xdata)
        xmax = max(xdata)
        ymin = min(ydata)
        ymax = max(ydata)
        #determining plot origin.
        xorigin = self.padding
        yorigin = self.plotheight-self.padding

        painter = QtGui.QPainter(self.label.pixmap())

        self.pen.setCapStyle(Qt.RoundCap)
        self.pen.setWidth(2)
        self.pen.setColor(QtGui.QColor('#5D6D7E'))
        painter.setPen(self.pen)
        self.drawPlot(painter, xorigin-30, yorigin+30)
        self.drawMarkings(painter, ymax, ymin, xorigin, yorigin, 1)
        self.drawMarkings(painter, xmax, xmin, xorigin, yorigin, 0)
        self.drawCircles(painter, xdata, ydata, categories, xmin, xmax,ymin, ymax, xorigin, yorigin, self.getColorMap(categories))
        painter.end()

xdata = [0,10,20,30,40]
ydata = [40,30,20,10,0]

app = QtWidgets.QApplication(sys.argv)