from PySide2.QtWidgets import QDialog
from PySide2.QtCore import Qt
from ui_documentation import Ui_Documentation

class Documentation(QDialog):

    def __init__(self, parent=None):
        super(Documentation, self).__init__(parent)
        self.setWindowTitle("2DGraphicsGUI -> Documentation")

        self.setFocusPolicy(Qt.StrongFocus)

        self.ui = Ui_Documentation()
        self.ui.setupUi(self)
