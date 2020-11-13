import sys
import math
import PySide2
import PySide2.QtOpenGL
from PySide2.QtGui import QBrush, QCursor, QIcon, QImage, QPaintDeviceWindow, QPainter, QPainterPath, QPen, QPicture, QPolygon, QPolygonF
from PySide2.QtWidgets import QApplication, QGraphicsItem, QGraphicsPolygonItem, QGraphicsScene, QGraphicsView, QGridLayout, QLabel, QMainWindow, QPushButton, QWidget, QAction
from PySide2.QtCore import QEvent, QFile, QObject, QPoint, QRect, QSize, Qt, Signal, Slot, QPointF
from ui_mainwindow import Ui_MainWindow

class DraggableGraphicsItemSignaller(QObject):

    positionChanged = Signal(QPointF)

    def __init__(self):
        super().__init__()

class CustomPolygon(QGraphicsPolygonItem):
    def __init__(self, polygon):
        QGraphicsPolygonItem.__init__(self, polygon)
        
        # can call all of these with one setFlags i.e. self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemSendsScenePositionChanges)
        self.setFlag(QGraphicsItem.ItemIsFocusable)
        self.setFlag(QGraphicsItem.ItemIsSelectable)
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemSendsScenePositionChanges)

        self.setTransformOriginPoint(self.boundingRect().center())

    def keyReleaseEvent(self, event: PySide2.QtGui.QKeyEvent):
        #reset flags to false for key states if needed
        return

    def keyPressEvent(self, event: PySide2.QtGui.QKeyEvent):
        if self.isSelected():
            if event.modifiers() == Qt.ShiftModifier:
                1==1
                
            if event.key() == Qt.Key_Return:
                self.setBrush(QBrush(Qt.red))

            # rotations
            if event.key() == Qt.Key_Right:
                self.setRotation(self.rotation() + 1)
            elif event.key() == Qt.Key_Left:
                self.setRotation(self.rotation() - 1)

            # scaling
            if event.key() == Qt.Key_Up:
                self.setScale(self.scale() + .05)
            elif event.key() == Qt.Key_Down:
                self.setScale(self.scale() - .05)

    def wheelEvent(self, event: PySide2.QtWidgets.QGraphicsSceneWheelEvent):
        self.setRotation(self.rotation() + event.delta() / 8)
            

