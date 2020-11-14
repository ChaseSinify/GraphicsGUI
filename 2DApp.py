""" BUILD NEW UI COMMAND:
pyside2-uic mainwindow.ui > ui_mainwindow.py
pyside2-uic documentation.ui > ui_documentation.py
"""
#region imports
import sys
import PySide2
from PySide2.QtGui import QBrush, QImage, QPainter, QPen, QPolygonF, QColor, QIcon
from PySide2.QtWidgets import QApplication, QGraphicsScene, QGraphicsView, QLabel, QMainWindow, QPushButton, QWidget, QAction
from PySide2.QtCore import QPoint, QRect, Qt
from ui_mainwindow import Ui_MainWindow
from CustomPolygon import CustomPolygon
from Documentation import Documentation
from DrawingArea import DrawingArea
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

        # MAINWINDOW STYLESHEET
        self.setStyleSheet("background-color: black")

        # DOCUMENTATION
        self.docs = Documentation(self)
        self.docs.show()

        # DRAWING AREA
        self.drawingArea = DrawingArea(self)
        self.drawingArea.show()
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
        Init Items | Drawing Area, Graphics Scene, Button States
        """
        #region
        # DRAWING AREA
        self.drawingLabel = QLabel(self)
        self.drawingLabel.setGeometry(154, 22, 75, 18)
        self.drawingLabel.setText("Drawing Area")
        self.drawingLabel.setStyleSheet("background-color: white; color: black; font-size: 24; border: 1px solid black; border-style: outset")
        self.drawingLabel.show()

        # 2D GRAPHICS VIEW SCENE
        self.graphicsLabel = QLabel(self)
        self.graphicsLabel.setGeometry(707, 22, 75, 18)
        self.graphicsLabel.setText("Graphics Area")
        self.graphicsLabel.setStyleSheet("background-color: white; color: black; font-size: 24; border: 1px solid black; border-style: outset")
        self.graphicsLabel.show()

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene, self)
        self.view.setGeometry(707, 41, 550, 655)
        self.view.setStyleSheet("background: white; border: none;")
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
        self.drawingArea.setToolTip("This is where drawing is enabled for the pen, as well as the vertex tool.\n"+
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

        # PEN TAB
        self.penAlphaSlider.setValue(255)
        self.ui.toolDockTabWidget.setCurrentWidget(self.ui.toolDockTabWidget.findChild(QWidget, "penTab"))

        # BRUSH TAB
        self.brushAlphaSlider.setValue(255)
        #endregion

    """
    Events
    """
    #region
    def keyPressEvent(self, event: PySide2.QtGui.QKeyEvent):
        if event.key() == Qt.Key_Return:
            if len(self.drawingArea.getVertices()) >= 3:
                self.addPolygonToScene(self.generatePolygon(self.drawingArea.getVertices()))
                self.drawingArea.clearVertices()
                self.drawingArea.clearDrawing()
    #endregion

    """
    Actions
    """
    #region
    def openDocs(self) -> None:
        self.docs.show()
    #endregion

    """
    Signals & Slots | UI functions
    """
    #region
    # TOOL BUTTONS
    def onPaintToolToggled(self) -> None:
        self.drawingArea.togglePaintMode(True if self.paintTool.isChecked() == True else False)

    def onVertexToolToggled(self) -> None:
        self.drawingArea.toggleVertexMode(True if self.vertexTool.isChecked() == True else False)
 
    # CLEAR BUTTONS
    def onClearGraphicsClicked(self) -> None:
        self.scene.clear()
        return
    
    def onClearDrawingClicked(self) -> None:
        self.drawingArea.clearVertices()
        self.drawingArea.clearDrawing()

    # PEN TAB
    def onPenRedSliderValueChanged(self) -> None:
        penInfo = self.getPenInfo()
        self.penRedSliderLabel.setStyleSheet(f'color: rgb({penInfo[0]}, 0, 0);')
        self.updatePenColorSquare()
        self.updateDrawingAreaPen()
    
    def onPenGreenSliderValueChanged(self) -> None:
        penInfo = self.getPenInfo()
        self.penGreenSliderLabel.setStyleSheet(f'color: rgb(0, {penInfo[1]}, 0);')
        self.updatePenColorSquare()
        self.updateDrawingAreaPen()

    def onPenBlueSliderValueChanged(self) -> None:
        penInfo = self.getPenInfo()
        self.penBlueSliderLabel.setStyleSheet(f'color: rgb(0, 0, {penInfo[2]});')
        self.updatePenColorSquare()
        self.updateDrawingAreaPen()

    def onPenAlphaSliderValueChanged(self) -> None:
        self.updatePenColorSquare()
        self.updateDrawingAreaPen()
    
    def onPenSizeSliderValueChanged(self) -> None:
        self.updateDrawingAreaPen()

    def onPenLineStyleComboBoxVCurrentIndexChanged(self) -> None:
        self.updateDrawingAreaPen()

    # BRUSH TAB
    def onBrushRedSliderValueChanged(self) -> None:
        brushInfo = self.getBrushInfo()
        self.brushRedSliderLabel.setStyleSheet(f'color: rgb({brushInfo[0]}, 0, 0);')
        self.updateBrushColorSquare()
        self.updateDrawingAreaBrush()
    
    def onBrushGreenSliderValueChanged(self) -> None:
        brushInfo = self.getBrushInfo()
        self.brushGreenSliderLabel.setStyleSheet(f'color: rgb(0, {brushInfo[1]}, 0);')
        self.updateBrushColorSquare()
        self.updateDrawingAreaBrush()
        
    def onBrushBlueSliderValueChanged(self) -> None:
        brushInfo = self.getBrushInfo()
        self.brushBlueSliderLabel.setStyleSheet(f'color: rgb(0, 0, {brushInfo[2]});')
        self.updateBrushColorSquare()
        self.updateDrawingAreaBrush()
    
    def onBrushAlphaSliderValueChanged(self) -> None:
        self.updateBrushColorSquare()
        self.updateDrawingAreaBrush()
    
    def onBrushTextureComboBoxCurrentIndexChanged(self) -> None:
        self.updateDrawingAreaBrush()
    #endregion
    
    """
    Helpers
    """
    #region
    # updates the drawing area pen to match the main window ui state
    def updateDrawingAreaPen(self) -> None:
        #get the pen information from the UI
        penInfo = self.getPenInfo()
        r, g, b, a = penInfo[:4]
        self.drawingArea.updatePen(QPen(QColor(r, g, b, a), penInfo[4], penInfo[5], Qt.RoundCap, Qt.RoundJoin))
        return

    # returns the Qt.PenStyle representation of the current ui index
    def getPenStyle(self, index: int) -> Qt.PenStyle:
        styles = [Qt.SolidLine, Qt.DashLine, Qt.DotLine, Qt.DashDotLine, Qt.DashDotDotLine]
        return styles[index]
    
    # updates the drawing area brush to match the main window ui state
    def updateDrawingAreaBrush(self) -> None:
        brushInfo = self.getBrushInfo()
        r, g, b, a = brushInfo[:4]
        self.drawingArea.updateBrush(QBrush(QColor(r, g, b, a), brushInfo[4]))
        return
    
    # returns the Qt.BrushStyle representation of the current ui index
    def getBrushTexture(self, index: int) -> Qt.BrushStyle:
        textures = [Qt.SolidPattern, Qt.Dense1Pattern, Qt.Dense2Pattern, Qt.Dense3Pattern, Qt.Dense4Pattern, Qt.Dense5Pattern,
                    Qt.Dense6Pattern, Qt.Dense7Pattern, Qt.HorPattern, Qt.VerPattern, Qt.CrossPattern, Qt.BDiagPattern,
                    Qt.FDiagPattern, Qt.DiagCrossPattern] #Qt.LinearGradientPattern, Qt.RadialGradientPattern, Qt.ConicalGradientPattern
        return textures[index]
    
    # returns the current pen information from the ui
    def getPenInfo(self) -> tuple:
        penR = self.ui.penRedSlider.value()
        penG = self.ui.penGreenSlider.value()
        penB = self.ui.penBlueSlider.value()
        penA = self.ui.penAlphaSlider.value()
        penSize = self.ui.penSizeSlider.value()
        penLineStyle = self.getPenStyle(self.ui.penLineStyleComboBox.currentIndex())
        return (penR, penG, penB, penA, penSize, penLineStyle)

    # returns the current brush information from the ui
    def getBrushInfo(self) -> tuple:
        brushR = self.ui.brushRedSlider.value()
        brushG = self.ui.brushGreenSlider.value()
        brushB = self.ui.brushBlueSlider.value()
        brushA = self.ui.brushAlphaSlider.value()
        brushTexture = self.getBrushTexture(self.ui.brushTextureComboBox.currentIndex())
        return (brushR, brushG, brushB, brushA, brushTexture)

    # update the rbga of the pen color square on the ui
    def updatePenColorSquare(self) -> None:
        penInfo = self.getPenInfo()
        r, g, b, a = penInfo[:4]
        self.penColorSquare.setStyleSheet(f'background-color: rgba({r}, {g}, {b}, {a});')
        return

    # update the rgba of the brush color square on the ui
    def updateBrushColorSquare(self) -> None:
        brushInfo = self.getBrushInfo()
        r, g, b, a = brushInfo[:4]
        self.brushColorSquare.setStyleSheet(f'background-color: rgba({r}, {g}, {b}, {a});')
        return

    # make a QPolygon from list of QPoints
    def generatePolygon(self, points) -> QPolygonF:
        p = QPolygonF(points)
        return p

    # add a polygon from painter into a 2d graphics scene item
    def addPolygonToScene(self, polygon) -> None:
        poly = CustomPolygon(polygon)
        #TODO: allow settings other than roundcap and roundjoin
        pen = self.drawingArea.getPen()
        poly.setPen(pen)

        #TODO: look at brush styles and textures
        brush = self.drawingArea.getBrush()
        poly.setBrush(brush)
        
        self.scene.addItem(poly)
        self.drawingArea.clearVertices()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

#region extra code
# event filter (TESTING)
#endregion