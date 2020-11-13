""" BUILD NEW UI COMMAND:
pyside2-uic mainwindow.ui > ui_mainwindow.py
"""

"""
Bugs:
#if we start drawing outside of area and then enter, it connets them all i.e. draws out of bounds -> just make custom drawing area class
"""
#region imports
from CustomPolygon import CustomPolygon
import sys
import PySide2
import PySide2.QtOpenGL
from PySide2.QtGui import QBrush, QCursor, QIcon, QImage, QPaintDeviceWindow, QPainter, QPainterPath, QPen, QPicture, QPolygon, QPolygonF, QColor
from PySide2.QtWidgets import QApplication, QGraphicsItem, QGraphicsPolygonItem, QGraphicsScene, QGraphicsView, QGridLayout, QLabel, QMainWindow, QPushButton, QWidget, QAction
from PySide2.QtCore import QEvent, QFile, QObject, QPoint, QRect, QSize, Qt, Signal, Slot
from ui_mainwindow import Ui_MainWindow
#endregion

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        """
        Basic Configurations
        """
        #region
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # default init information: name, location, size, icon
        title = "2D Graphics Tool"

        # setting default information
        self.setWindowTitle(title)
        
        # white drawing background
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        # MAINWINDOW STYLESHEET
        self.setStyleSheet("background-color: ")
        #endregion

        """
        Helpers
        """
        #region
        # BRUSH AND PEN
        self.penTypes = [Qt.SolidLine, Qt.DotLine]
        self.pen = QPen() #TODO: make setters for all of these so we can just call pen .. ?
        self.penR = 0 # red channel
        self.penG = 0 # green channel
        self.penB = 0 # blue channel
        self.penA = 255 # alpha channel
        self.penSize = 1
        self.penLineType = Qt.SolidLine

        self.brush = QBrush()

        # tool states
        self.painting = False
        self.vertexing = False
        self.erasing = False

        # vertex drawing information -- will be dynamic later i.e. selectable from menu
        self.vertices = [] #store each of the vertex in an array so we can draw them dynamically later

        # last mouse position
        self.lastPoint = QPoint

        # eraser drawing information -- will be dynamic later i.e. selectable from menu
        #endregion

        """
        Mainwindow UI Bindings
        """
        #region
        # TOOL BUTTONS
        self.paintTool = self.ui.paintTool
        self.vertexTool = self.ui.vertexTool
        self.eraserTool = self.ui.eraserTool

        # CLEAR BUTTONS
        self.clearGraphics = self.ui.clearGraphicsButton
        self.clearDrawing = self.ui.clearDrawingButton

        # PEN TAB
        self.penRedSlider = self.ui.penRedSlider
        self.penGreenSlider = self.ui.penGreenSlider
        self.penBlueSlider = self.ui.penBlueSlider
        self.penAlphaSlider = self.ui.penAlphaSlider
        self.penSizeSlider = self.ui.penSizeSlider
        self.penLineTypeComboBox = self.ui.penLineStyleComboBox
        #endregion
       
        """
        MainWindow Init Items | Drawing Area, Graphics Scene
        """
        #region
        # DRAWING AREA
        self.drawingLabel = QLabel(self)
        self.drawingLabel.setGeometry(154, 21, 75, 21)
        self.drawingLabel.setText("Drawing Area")
        self.drawingLabel.setStyleSheet("background-color: white; color: black; font-size: 24; border: 1px solid black; border-style: outset")
        self.drawingLabel.show()

        self.validDrawingArea = QRect(155, 42, 549, 654) #IMPOPTANT
        self.drawingAreaLabel = QLabel(self)
        self.drawingAreaLabel.setGeometry(154, 41, 550, 655)
        self.drawingAreaLabel.setStyleSheet("border: 2px solid black; border-style: outset")
        self.drawingAreaLabel.show()

        # 2D GRAPHICS VIEW SCENE
        self.graphicsLabel = QLabel(self)
        self.graphicsLabel.setGeometry(707, 21, 75, 21)
        self.graphicsLabel.setText("Graphics Area")
        self.graphicsLabel.setStyleSheet("background-color: white; color: black; font-size: 24; border: 1px solid black; border-style: outset")
        self.graphicsLabel.show()

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene, self)
        self.view.setGeometry(707, 41, 550, 655)
        self.view.setStyleSheet("border: 2px solid black; border-style: outset")
        #endregion

        """
        Signals & Slots | UI functions
        """
        #region
        # TOOL BUTTONS
        self.paintTool.toggled.connect(self.onPaintToolToggled)
        self.vertexTool.toggled.connect(self.onVertexToolToggled)
        self.eraserTool.toggled.connect(self.onEraserToolToggled)

        # CLEAR BUTTONS
        self.clearGraphics.clicked.connect(self.onClearGraphicsClicked)
        self.clearDrawing.clicked.connect(self.onClearDrawingClicked)

        # PEN TAB
        self.penRedSlider.valueChanged.connect(self.onPenRedSliderValueChanged)
        self.penGreenSlider.valueChanged.connect(self.onPenGreenSliderValueChanged)
        self.penBlueSlider.valueChanged.connect(self.onPenBlueSliderValueChanged)
        self.penAlphaSlider.valueChanged.connect(self.onPenAlphaSliderValueChanged)
        self.penSizeSlider.valueChanged.connect(self.onPenSizeSliderValueChanged)
        self.penLineTypeComboBox.currentTextChanged.connect(self.onPenLineTypeComboBoxVCurrentTextChanged)
        #endregion

    """
    Signals & Slots | UI functions
    """
    #region
    # TOOL BUTTONS
    def onPaintToolToggled(self):
        self.painting = True if self.paintTool.isChecked() == True else False

    def onVertexToolToggled(self):
        self.vertexing = True if self.vertexTool.isChecked() == True else False
        # clear the vertices array if we are toggling from on -> off
        if self.vertexTool.isChecked() == False:
            self.vertices.clear()

    def onEraserToolToggled(self):
        self.erasing = True if self.eraserTool.isChecked() == True else False

    # CLEAR BUTTONS
    def onClearGraphicsClicked(self):
        self.scene.clear()
        return
    
    def onClearDrawingClicked(self):
        self.vertices.clear()
        self.resetDrawingArea()

    # PEN TAB
    def onPenRedSliderValueChanged(self):
        self.penR = self.penRedSlider.value()
    
    def onPenGreenSliderValueChanged(self):
        self.penG = self.penGreenSlider.value()
        
    def onPenBlueSliderValueChanged(self):
        self.penB = self.penBlueSlider.value()
    
    def onPenAlphaSliderValueChanged(self):
        self.penA = self.penAlphaSlider.value()
    
    def onPenSizeSliderValueChanged(self):
        self.penSize = self.penSizeSlider.value()

    #TODO: Need to make a dict that binds the text values of this combobox
    # to build into Qt line styles
    def onPenLineTypeComboBoxVCurrentTextChanged(self):
        self.penLineType = self.penTypes[self.penLineTypeComboBox.currentIndex()]
    #endregion
    
    """
    Events
    """
    #region
    def mousePressEvent(self, event: PySide2.QtGui.QMouseEvent):
        self.lastPoint = event.pos()
        if self.validDrawingArea.contains(event.pos()):
            if event.button() == Qt.LeftButton:
                #if we are in vertex mode, append the point to the array
                if self.vertexing:
                    self.vertices.append(self.lastPoint)
                    self.drawVertex()

    def mouseMoveEvent(self, event):
        if self.validDrawingArea.contains(event.pos()):
            if(event.buttons() & Qt.LeftButton) & self.painting:
                painter = QPainter(self.image)
                painter.setPen(QPen(QColor(self.penR, self.penG, self.penB, self.penA), self.penSize, self.penLineType, Qt.RoundCap, Qt.RoundJoin)) #Qt.SolidLine
                painter.drawLine(self.lastPoint, event.pos())
                self.lastPoint = event.pos()
                self.update()

    def mouseReleaseEvent(self, event):
        return
        
    def keyPressEvent(self, event: PySide2.QtGui.QKeyEvent):
        if self.vertexing:
            if event.key() == Qt.Key_Return:
                if len(self.vertices) >= 3:
                    # self.drawCustomPolygon()
                    self.addPolygonToScene(self.generatePolygon(self.vertices))
                    self.resetDrawingArea()
                    self.update()
                
    def paintEvent(self, event):
        # painter = QPainter(self)
        painter = QPainter(self)
        painter.drawImage(self.rect(), self.image, self.image.rect())
    #endregion

    """
    Helpers
    """
    #region
    # draws a custom polygon based on the vertex points in self.vertices
    def drawCustomPolygon(self):
        painter = QPainter(self.image)
        painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        painter.setRenderHint(QPainter.HighQualityAntialiasing)
        for i in range(len(self.vertices) - 1):
            painter.drawLine(self.vertices[i], self.vertices[i+1])
        painter.drawLine(self.vertices[-1], self.vertices[0]) #close the shape: end -> start line
        self.update()
        self.vertices.clear()

    # draws a temp vertex to shown user what points will be used in polygon creation
    def drawVertex(self):
        painter = QPainter(self.image)
        painter.setPen(QPen(Qt.red, 10, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawPoint(self.lastPoint)
        self.update()

    """
    TODO: Make these take brush/pen/etc params from the tool menu when drawing
    """
    # make a QPolygon from list of QPoints
    def generatePolygon(self, points):
        p = QPolygonF(points)
        return p

    # add a polygon from painter into a 2d graphics scene item
    def addPolygonToScene(self, polygon):
        # item = QGraphicsPolygonItem(polygon)
        poly = CustomPolygon(polygon)
        self.scene.addItem(poly)
        self.vertices.clear()

    # temp, should clean this up, also add true erase button
    def resetDrawingArea(self):
        self.image.fill(Qt.white)
        self.update()
    #endregion

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

#region extra code
# event filter (TESTING)
        # self.installEventFilter(self)

    # TESTING EVENT FILTER
    # def eventFilter(self, watched: PySide2.QtCore.QObject, event: PySide2.QtCore.QEvent) -> bool:
    #     return True
#endregion