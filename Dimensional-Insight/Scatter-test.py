from operator import xor
from re import X
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
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
        self.drawPlot()

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

    def drawPlot(self):
      canvas = QtGui.QPixmap(self.plotheight, self.plotwidth)
      canvas.fill(QtGui.QColor("white"))
      self.label.setPixmap(canvas)
      self.setCentralWidget(self.label)

    def getMultiple(self, range):
      return((range//10)//10)*10

    def scatter(self, xdata, ydata):
        xmin = min(xdata)
        xmax = max(xdata)
        ymin = min(ydata)
        ymax = max(ydata)
        dataRange = xmax-xmin
        marker =  self.getMultiple(dataRange)
        xorigin = self.padding
        yorigin = self.plotheight-self.padding

        painter = QtGui.QPainter(self.label.pixmap())

        self.pen.setCapStyle(Qt.RoundCap)
        self.pen.setWidth(2)
        self.pen.setColor(QtGui.QColor('#5D6D7E'))
        painter.setPen(self.pen)
      
        painter.drawLine(QtCore.QLineF(xorigin, yorigin, xorigin, yorigin-(self.gridmax+50)))
        painter.drawLine(QtCore.QLineF(xorigin, yorigin, xorigin + self.gridmax+50,yorigin))
        
        #markings for y axis
        yrange = ymax-ymin
        marker = self.getMultiple(yrange)
        ymark = ymin + marker
        while 1:
          if ymark <= ymax:
            y = self.getscale(ymark, ymin, ymax, self.gridmin, self.gridmax)
            xGrid, yGrid = self.getposition(0,y, xorigin, yorigin)
            self.pen.setWidth(2)
            self.pen.setColor(QtGui.QColor('#5D6D7E'))
            painter.setPen(self.pen)
            painter.drawLine(QtCore.QLineF(xGrid, yGrid, xGrid-8, yGrid))
            painter.drawText(QtCore.QPointF(xGrid-35,yGrid), str(ymark))
            self.pen.setWidth(1)
            self.pen.setColor(QtGui.QColor('#D0D9E3'))
            painter.setPen(self.pen)
            painter.drawLine(QtCore.QLineF(xGrid, yGrid, xGrid+self.gridmax, yGrid))
            ymark += marker
          else:
            break
        
        #markings for x axis
        xrange = xmax-xmin
        marker = self.getMultiple(xrange)
        xmark = xmin + marker
        while 1:
          if xmark <= xmax:
            x = self.getscale(xmark, xmin, xmax, self.gridmin, self.gridmax)
            xGrid, yGrid = self.getposition(x,0, xorigin, yorigin)
            self.pen.setWidth(2)
            self.pen.setColor(QtGui.QColor('#5D6D7E'))
            painter.setPen(self.pen)
            painter.drawLine(QtCore.QLineF(xGrid, yGrid, xGrid, yGrid+8))
            painter.drawText(QtCore.QPointF(xGrid,yGrid+20), str(xmark))
            self.pen.setWidth(1)
            self.pen.setColor(QtGui.QColor('#D0D9E3'))
            painter.setPen(self.pen)
            painter.drawLine(QtCore.QLineF(xGrid, yGrid, xGrid, yGrid-self.gridmax))
            xmark += marker
          else:
            break
          
          
        
        self.pen.setWidth(15)
        self.pen.setColor(QtGui.QColor('blue'))
        painter.setPen(self.pen)
        
        for i in range(len(xdata)):
          x,y = self.getposition(self.getscale(xdata[i],xmin,xmax,self.gridmin,self.gridmax),self.getscale(ydata[i],ymin,ymax,self.gridmin,self.gridmax), xorigin,yorigin)
          painter.drawPoint(QtCore.QPointF(x,y))
        painter.end()

xdata = [-100, 0, 10, 40, 50, 60, 100]
ydata = [-40, 0, 100, 40, 33, 23, 200]

app = QtWidgets.QApplication(sys.argv)
window = Plot()
window.scatter(xdata, ydata)
window.show()
app.exec_()