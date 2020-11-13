import PySide2
from PySide2.QtWidgets import QGraphicsItem, QGraphicsPolygonItem
from PySide2.QtCore import Qt

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
            # if event.modifiers() == Qt.ShiftModifier:
            
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
            