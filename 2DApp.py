""" BUILD NEW UI COMMAND:
pyside2-uic mainwindow.ui > ui_mainwindow.py
pyside2-uic documentation.ui > ui_documentation.py
"""

"""
Bugs:
#if we start drawing outside of area and then enter, it connets them all i.e. draws out of bounds -> just make custom drawing area class
# CAUSE -> we always set last point even if start location in mouse press wasnt valid. Either change logic or custom class
"""

"""
#TODO IMPORTANT: Make a full screen pop-out widget with the docs on in so user is forced to read it and put it off to the side when using
"""

#region imports
import sys
import PySide2
from PySide2.QtGui import QBrush, QImage, QPainter, QPen, QPolygonF, QColor, QIcon
from PySide2.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QLabel, QMainWindow, QWidget, QAction
from PySide2.QtCore import QPoint, QRect, Qt
from ui_mainwindow import Ui_MainWindow
from CustomPolygon import CustomPolygon
from Documentation import Documentation
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
        
        # focus policy
        self.setFocusPolicy(Qt.StrongFocus)

        # white drawing background
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        # MAINWINDOW STYLESHEET
        self.setStyleSheet("background-color: ")

        # DOCUMENTATION
        self.docs = Documentation(self)
        self.docs.show()
        #endregion

        """
        MenuBar & StatusBar - Actions
        """
        #region
        # MAINWINDOW STATUSBAR
        self.statusBar().showMessage("Status Bar")

        # MAIN WINDOW MENUBAR
        #menubar
        menubar = self.menuBar()

        #exit action
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)

        #docs action
        docsAction = QAction(QIcon('exit.png'), '&Docs', self)
        docsAction.setShortcut('Ctrl+D')
        docsAction.setStatusTip('Launch documentation window')
        docsAction.triggered.connect(self.openDocs)

        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        docMenu = menubar.addMenu('&Docs')
        docMenu.addAction(docsAction)

        #endregion

        """
        Helpers
        """
        #region
        # PEN
        self.penStyles = [Qt.SolidLine, Qt.DashLine, Qt.DotLine, Qt.DashDotLine, Qt.DashDotDotLine]
        self.pen = QPen() #TODO: make setters for all of these so we can just call pen .. ?
        self.penR = 0 # red channel
        self.penG = 0 # green channel
        self.penB = 0 # blue channel
        self.penA = 255 # alpha channel
        self.penSize = 1
        self.penLineStyle = Qt.SolidLine

        # BRUSH
        self.brush = QBrush() #TODO: make setters for all of these so we can just call brush .. ?
        self.brushTextures = [Qt.SolidPattern, Qt.Dense1Pattern, Qt.Dense2Pattern, Qt.Dense3Pattern, Qt.Dense4Pattern, Qt.Dense5Pattern,
                                Qt.Dense6Pattern, Qt.Dense7Pattern, Qt.HorPattern, Qt.VerPattern, Qt.CrossPattern, Qt.BDiagPattern,
                                Qt.FDiagPattern, Qt.DiagCrossPattern] #Qt.LinearGradientPattern, Qt.RadialGradientPattern, Qt.ConicalGradientPattern
        self.brushR = 0
        self.brushG = 0
        self.brushB = 0
        self.brushA = 255
        self.brushTexture = Qt.SolidPattern
        #TODO: add textures and additional settings

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
        Init Items | Drawing Area, Graphics Scene, Button States
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
        UI Bindings
        """
        #region
        # MENU BAR
        # self.menuBar().addAction()

        # TOOL BUTTONS
        self.vertexTool = self.ui.vertexTool
        self.paintTool = self.ui.paintTool
        # self.eraserTool = self.ui.eraserTool

        # CLEAR BUTTONS
        self.clearGraphics = self.ui.clearGraphicsButton
        self.clearDrawing = self.ui.clearDrawingButton

        # PEN TAB
        #tab
        self.penTab = self.ui.penTab
        #color square
        self.penColorSquare = self.ui.penColorSquare
        #red
        self.penRedSliderLabel = self.ui.penRedSliderLabel
        self.penRedSlider = self.ui.penRedSlider
        #green
        self.penGreenSliderLabel = self.ui.penGreenSliderLabel
        self.penGreenSlider = self.ui.penGreenSlider
        #blue
        self.penBlueSliderLabel = self.ui.penBlueSliderLabel
        self.penBlueSlider = self.ui.penBlueSlider
        #alpha
        self.penAlphaSliderLabel = self.ui.penAlphaSliderLabel
        self.penAlphaSlider = self.ui.penAlphaSlider
        #size
        self.penSizeSliderLabel = self.ui.penSizeSliderLabel
        self.penSizeSlider = self.ui.penSizeSlider
        #style
        self.penLineStyleComboBoxLabel = self.ui.penLineStyleComboBoxLabel
        self.penLineStyleComboBox = self.ui.penLineStyleComboBox

        # BRUSH TAB
        #tab
        self.brushTab = self.ui.brushTab
        #color square
        self.brushColorSquare = self.ui.brushColorSquare
        #red
        self.brushRedSliderLabel = self.ui.brushRedSliderLabel
        self.brushRedSlider = self.ui.brushRedSlider
        #green
        self.brushGreenSliderLabel = self.ui.brushGreenSliderLabel
        self.brushGreenSlider = self.ui.brushGreenSlider
        #blue
        self.brushBlueSliderLabel = self.ui.brushBlueSliderLabel
        self.brushBlueSlider = self.ui.brushBlueSlider
        #alpha
        self.brushAlphaSliderLabel = self.ui.brushAlphaSliderLabel
        self.brushAlphaSlider = self.ui.brushAlphaSlider
        #texture
        self.brushTextureComboBoxLabel = self.ui.brushTextureComboBoxLabel
        self.brushTextureComboBox = self.ui.brushTextureComboBox
        #endregion

        """
        Tool Tips & Status Tips & Whats This Bindings
        """
        #region
        # TOOL BUTTONS
        self.vertexTool.setToolTip("Allows the painting of vertices (marked in red when drawn) in the drawing area. After painting the desired\n"+
                                    "vertices, press enter to generate the graphics object in the graphics view on the right.\n"+
                                    "The pen settings determine the border of the graphic, the brush settings determine the fill.")
        self.paintTool.setToolTip("Allows for drawing in the drawing area. The color, alpha, size and line styles are determined\n"+
                                    "by the pen settings.")

        # CLEAR BUTTONS
        self.clearDrawing.setToolTip("Clears everything in the drawing area")
        self.clearGraphics.setToolTip("Clears everything in the graphics area")

        # PEN TAB
        self.penTab.setToolTip("The pen settings determine the drawing pen, as well as the outline of shapes in the graphics view")
        self.penRedSlider.setToolTip("Adjusts the red color channel for the pen, range(0, 255) inclusive")
        self.penGreenSlider.setToolTip("Adjusts the green color channel for the pen, range(0, 255) inclusive")
        self.penBlueSlider.setToolTip("Adjusts the blue color channel for the pen, range(0, 255) inclusive")
        self.penAlphaSlider.setToolTip("Adjusts the alpha channel for the pen, range(0, 255) inclusive")
        self.penSizeSlider.setToolTip("Adjusts the size of the pen, range(0, 100) inclusive")
        self.penLineStyleComboBox.setToolTip("Adjusts the line style of the pen - solid, dotted, etc")

        # BRUSH TAB
        self.brushTab.setToolTip("The brush settings determine the fill of the shapes generated in the graphics view")
        self.brushRedSlider.setToolTip("Adjusts the red color channel for the brush, range(0, 255) inclusive")
        self.brushGreenSlider.setToolTip("Adjusts the green color channel for the brush, range(0, 255) inclusive")
        self.brushBlueSlider.setToolTip("Adjusts the blue color channel for the brush, range(0, 255) inclusive")
        self.brushAlphaSlider.setToolTip("Adjusts the alpha channel for the brush, range(0, 255) inclusive")
        self.brushTextureComboBox.setToolTip("Adjusts the texture for the brush - solid, dotted fill, etc")

        # DRAWING AREA
        self.drawingAreaLabel.setToolTip("This is where drawing is enabled for the pen, as well as the vertex tool.\n"+
                                            "Free draw with the paint tool, or draw a polygon by vertices with the vertext tool\n"+
                                            "Once vertices are ready, press return/enter to spawn the polygon in the graphics view.")

        # GRAPHICS AREA
        self.view.setToolTip("This is where polygons generated from vertices in the drawing area are spawned and rendered.\n"+
                                "These polygons support translations, transforms, scaling and rotations with the arrow keys and mouse wheel.")
        #endregion
       
        """
        Signals & Slots | UI functions
        """
        #region
        # TOOL BUTTONS
        self.paintTool.toggled.connect(self.onPaintToolToggled)
        self.vertexTool.toggled.connect(self.onVertexToolToggled)
        # self.eraserTool.toggled.connect(self.onEraserToolToggled)

        # CLEAR BUTTONS
        self.clearGraphics.clicked.connect(self.onClearGraphicsClicked)
        self.clearDrawing.clicked.connect(self.onClearDrawingClicked)

        # PEN TAB
        self.penRedSlider.valueChanged.connect(self.onPenRedSliderValueChanged)
        self.penGreenSlider.valueChanged.connect(self.onPenGreenSliderValueChanged)
        self.penBlueSlider.valueChanged.connect(self.onPenBlueSliderValueChanged)
        self.penAlphaSlider.valueChanged.connect(self.onPenAlphaSliderValueChanged)
        self.penSizeSlider.valueChanged.connect(self.onPenSizeSliderValueChanged)
        self.penLineStyleComboBox.currentIndexChanged.connect(self.onPenLineStyleComboBoxVCurrentIndexChanged)

        # BRUSH TAB
        self.brushRedSlider.valueChanged.connect(self.onBrushRedSliderValueChanged)
        self.brushGreenSlider.valueChanged.connect(self.onBrushGreenSliderValueChanged)
        self.brushBlueSlider.valueChanged.connect(self.onBrushBlueSliderValueChanged)
        self.brushAlphaSlider.valueChanged.connect(self.onBrushAlphaSliderValueChanged)
        self.brushTextureComboBox.currentIndexChanged.connect(self.onBrushTextureComboBoxCurrentIndexChanged)
        #endregion

        """
        Default Values
        """
        #region
        # TOOLS
        self.vertexTool.setChecked(True)
        self.vertexing = True

        # PEN TAB
        self.penAlphaSlider.setValue(255)
        self.ui.toolDockTabWidget.setCurrentWidget(self.ui.toolDockTabWidget.findChild(QWidget, "penTab"))

        # BRUSH TAB
        self.brushAlphaSlider.setValue(255)
        #endregion

    """
    Actions
    """
    #region
    def openDocs(self):
        self.docs.show()

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
        self.penRedSliderLabel.setStyleSheet(f'color: rgb({self.penR}, 0, 0);')
        self.penColorSquare.setStyleSheet(f'background-color: rgba({self.penR}, {self.penG}, {self.penB}, {self.penA});')
    
    def onPenGreenSliderValueChanged(self):
        self.penG = self.penGreenSlider.value()
        self.penGreenSliderLabel.setStyleSheet(f'color: rgb(0, {self.penG}, 0);')
        self.penColorSquare.setStyleSheet(f'background-color: rgba({self.penR}, {self.penG}, {self.penB}, {self.penA});')
        
    def onPenBlueSliderValueChanged(self):
        self.penB = self.penBlueSlider.value()
        self.penBlueSliderLabel.setStyleSheet(f'color: rgb(0, 0, {self.penB});')
        self.penColorSquare.setStyleSheet(f'background-color: rgba({self.penR}, {self.penG}, {self.penB}, {self.penA});')
    
    def onPenAlphaSliderValueChanged(self):
        self.penA = self.penAlphaSlider.value()
        self.penColorSquare.setStyleSheet(f'background-color: rgba({self.penR}, {self.penG}, {self.penB}, {self.penA});')
    
    def onPenSizeSliderValueChanged(self):
        self.penSize = self.penSizeSlider.value()

    def onPenLineStyleComboBoxVCurrentIndexChanged(self):
        self.penLineStyle = self.penStyles[self.penLineStyleComboBox.currentIndex()]

    # BRUSH TAB
    def onBrushRedSliderValueChanged(self):
        self.brushR = self.brushRedSlider.value()
        self.brushRedSliderLabel.setStyleSheet(f'color: rgb({self.brushR}, 0, 0);')
        self.brushColorSquare.setStyleSheet(f'background-color: rgba({self.brushR}, {self.brushG}, {self.brushB}, {self.brushA});')
    
    def onBrushGreenSliderValueChanged(self):
        self.brushG = self.brushGreenSlider.value()
        self.brushGreenSliderLabel.setStyleSheet(f'color: rgb(0, {self.brushG}, 0);')
        self.brushColorSquare.setStyleSheet(f'background-color: rgba({self.brushR}, {self.brushG}, {self.brushB}, {self.brushA});')
        
    def onBrushBlueSliderValueChanged(self):
        self.brushB = self.brushBlueSlider.value()
        self.brushBlueSliderLabel.setStyleSheet(f'color: rgb(0, 0, {self.brushB});')
        self.brushColorSquare.setStyleSheet(f'background-color: rgba({self.brushR}, {self.brushG}, {self.brushB}, {self.brushA});')
    
    def onBrushAlphaSliderValueChanged(self):
        self.brushA = self.brushAlphaSlider.value()
        self.brushColorSquare.setStyleSheet(f'background-color: rgba({self.brushR}, {self.brushG}, {self.brushB}, {self.brushA});')
    
    def onBrushTextureComboBoxCurrentIndexChanged(self):
        self.brushTexture = self.brushTextures[self.brushTextureComboBox.currentIndex()]
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
                painter.setPen(QPen(QColor(self.penR, self.penG, self.penB, self.penA), self.penSize, self.penLineStyle, Qt.RoundCap, Qt.RoundJoin)) #Qt.SolidLine
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

    # make a QPolygon from list of QPoints
    def generatePolygon(self, points):
        p = QPolygonF(points)
        return p

    # add a polygon from painter into a 2d graphics scene item
    def addPolygonToScene(self, polygon):
        poly = CustomPolygon(polygon)
        #TODO: allow settings other than roundcap and roundjoin
        pen = QPen(QColor(self.penR, self.penG, self.penB, self.penA), self.penSize, self.penLineStyle, Qt.RoundCap, Qt.RoundJoin)
        poly.setPen(pen)

        #TODO: look at brush styles and textures
        brush = QBrush(QColor(self.brushR, self.brushG, self.brushB, self.brushA), self.brushTexture)
        poly.setBrush(brush)
        
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