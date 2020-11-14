import sys
import PySide2
from PySide2.QtGui import QBrush, QImage, QPainter, QPen, QPixmap, QPolygonF, QColor, QIcon
from PySide2.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QGridLayout, QLabel, QMainWindow, QWidget, QAction
from PySide2.QtCore import QPoint, QRect, Qt

class DrawingArea(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        """
        Basic Config
        """
        #region
        self.setGeometry(154, 41, 559, 655)
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.update()

        self.label = QLabel()
        self.label.setPixmap(QPixmap.fromImage(self.image))

        self.pen = QPen()
        self.brush = QBrush()

        self.lastPoint = QPoint()
        self.vertices = []

        self.paintMode = False
        self.vertexMode = True
        #endregion
        
        self.show()

    """
    Events
    """
    #region
    def mousePressEvent(self, event: PySide2.QtGui.QMouseEvent):
        self.lastPoint = event.pos()
        if event.button() == Qt.LeftButton:
            if self.vertexMode:
                self.vertices.append(self.lastPoint)
                self.drawVertex()

    def mouseMoveEvent(self, event: PySide2.QtGui.QMouseEvent):
        if(event.buttons() == Qt.LeftButton) and self.paintMode:
            painter = QPainter(self.image)
            painter.setPen(self.pen)
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()
    
    def mouseReleaseEvent(self, event):
        return
    
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(self.rect(), self.image, self.image.rect()) #last is source
        self.label.setPixmap(QPixmap.fromImage(self.image))
    #endregion
    
    """
    Helpers
    """
    #region
    def drawVertex(self) -> None:
        painter = QPainter(self.image)
        painter.setPen(QPen(Qt.red, 10, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawPoint(self.lastPoint)
        self.update()

    def togglePaintMode(self, tf: bool) -> None:
        self.paintMode = tf
    
    def toggleVertexMode(self, tf: bool) -> None:
        self.vertexMode = tf

    def updatePen(self, pen: QPen) -> None:
        self.pen = pen
        return

    def updateBrush(self, brush: QBrush) -> None:
        self.brush = brush
        return

    def getVertices(self) -> list:
        return self.vertices

    def clearVertices(self) -> None:
        self.vertices.clear()

    def clearDrawing(self) -> None:
        self.image.fill(Qt.white)
        self.label.setPixmap(QPixmap.fromImage(self.image))
        self.update()

    def getPen(self) -> QPen:
        return self.pen
    
    def getBrush(self) -> QBrush:
        return self.brush
    #endregion
        