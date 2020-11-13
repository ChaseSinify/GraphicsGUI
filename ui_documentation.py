# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'documentation.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Documentation(object):
    def setupUi(self, Documentation):
        if not Documentation.objectName():
            Documentation.setObjectName(u"Documentation")
        Documentation.resize(1280, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Documentation.sizePolicy().hasHeightForWidth())
        Documentation.setSizePolicy(sizePolicy)
        Documentation.setMinimumSize(QSize(1280, 720))
        Documentation.setMaximumSize(QSize(1280, 720))
        Documentation.setSizeIncrement(QSize(1280, 720))
        Documentation.setBaseSize(QSize(1280, 720))
        Documentation.setStyleSheet(u"background-color: grey")
        self.textEdit = QTextEdit(Documentation)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(23, 69, 1231, 631))
        self.textEdit.setStyleSheet(u"background: rgb(50,50,50)")
        self.textEdit.setReadOnly(True)
        self.label = QLabel(Documentation)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 811, 51))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: white")

        self.retranslateUi(Documentation)

        QMetaObject.connectSlotsByName(Documentation)
    # setupUi

    def retranslateUi(self, Documentation):
        Documentation.setWindowTitle(QCoreApplication.translate("Documentation", u"Documentation", None))
        self.textEdit.setHtml(QCoreApplication.translate("Documentation", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#55aaff;\">***</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#ffffff;\">Move this window so it isn't covering the App :)</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#55aaff;\">***</span></p>\n"
""
                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#55aaff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#55aaff;\">General Info:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#ffffff;\">	The shortcut for this documentation is &quot;Cntrl+D&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#55aaff;\">	</span><span style=\" font-family"
                        ":'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#ffffff;\">Almost every item has a &quot;hover&quot; function that displays a tool tip!</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#55aaff;\">	</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">The tool box is on a floatable dock widget on the left.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#55aaff;\">	</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">The left window is for drawing vertices, or simply painting.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent"
                        ":0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#55aaff;\">	</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">The right window renders the graphics polygons as true 2d objects.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">	At any time, you can clear either window (drawing, graphics) by</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">		pressing the &quot;clear&quot; buttons on the bottom left of the tool dock.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; f"
                        "ont-weight:600; color:#55aaff;\">	</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">With this program, you can:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#55aaff;\">		</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#ffffff;\">* </span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">Draw arbitrary creations with the &quot;paint&quot; tool;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#55aaff;\">		</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">* Create custom polygons with the &quot;vertex&quot; tool;</span></p>\n"
"<p sty"
                        "le=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">		* Modify (translate, transform, scale and rotate) 2d graphics objects;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#55aaff;\">			</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#55aaff;\">Drawing Polygons:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt;\">	</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#"
                        "ffffff;\">1. Select the &quot;Vertex&quot; tool from the left toolbar dock (enabled by default)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">	2. In the drawing area (left pane), click to place vertices (these are displayed</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">		in red). Once you have a sufficient amount to draw a polygon (3+) and</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">		are happy, press </span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#ffffff;\">&quot;return"
                        "&quot;</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\"> to draw the polygon in the graphics view</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">		on the right (right pane).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">	3. The polygon appears in the right graphics view, where it can be modified</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">		(more on this below)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;"
                        " -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:24pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#55aaff;\">Customizing Polygons:	</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#55aaff;\">		</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">On the left side of the application, we have a tool bar with many </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">	different settings. In the middle of the toolbar, there is a tab section with </span></p>\n"
"<p style"
                        "=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">	specific settings for the pen and the brush. These settings determine the </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">	colors, size, opacity, line style, textures, etc. of the drawings and shapes </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">	created.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">		Specifically, the </span>"
                        "<span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#ffffff;\">PEN</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\"> directly impacts the drawing area paint tool, as well</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">	as the </span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#ffffff;\">BORDER </span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">of the 2d graphics polygons on the right (which are created </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">	by drawing vertices on the left). The </span><span style=\" font-family:'MS Shell Dlg 2'; font-"
                        "size:24pt; font-weight:600; color:#ffffff;\">BRUSH</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\"> directly impacts the </span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#ffffff;\">FILL</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\"> of the </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">	2d graphics polygons on the right.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">		Inside the tool box on the left dock, modify the colors, alpha, pen style,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-inden"
                        "t:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">	brush texture, etc. to produce a different color/style of polygon. At any given</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">	time, the color/alpha in RGBA is displayed on the colored sqaure within the</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">	pen or brush tab that is active.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px;"
                        " -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#55aaff;\">Transforming Polygons:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#55aaff;\">		</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">Polygon transformations occur in the graphics window (right pane). </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">	These item are true 2d graphics objects, and support transformations. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt"
                        "; color:#ffffff;\">	To modify one, start by selecting it (click on the polygon).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">	*</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#ffffff;\">ROTATION: </span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">Hover the polygon and use mouse scroll wheel</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">		or the arrow keys (more precise, but slow).</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">	*</span><sp"
                        "an style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#ffffff;\">SCALING: </span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">Select a polygon and use the up and down arrows.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">	*</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#ffffff;\">TRANSLATION: </span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">Click and drag a polygon.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-inde"
                        "nt:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#55aaff;\">Drawing:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#55aaff;\">		</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">On the left window, with the paint tool selected from the tool dock, </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">	click and drag to paint the current </span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#ffffff;\">PEN</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\"> settings onto the drawing area.</span></p>\n"
"<p style=\"-qt-paragraph-type:empt"
                        "y; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#55aaff;\">Coming Soon:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; font-weight:600; color:#55aaff;\">	</span><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">*3D objects with QOpenGl</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">	*Significantly cleaner UI design and colors</span><"
                        "/p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">	*Ability to upload custom images and texture maps</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">	*Saving/Opening projects and items</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">	*Significantly more customization and control</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">	*Easter eggs and small bug fixes (what bu"
                        "gs? :) )</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2';\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:24pt; color:#ffffff;\">		</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Documentation", u"2DGraphics Application Documentation", None))
    # retranslateUi

