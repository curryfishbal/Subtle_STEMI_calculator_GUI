# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from mainprocessor import mainprocessor
from PyQt6 import QtCore, QtGui, QtWidgets
import xml.etree.ElementTree as ET
from PyQt6.QtCore import Qt

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(750, 847)
        Form.setStyleSheet("background-color: #000000;\n"
"color: white;\n"
"\n"
"")
        self.textBrowser_2 = QtWidgets.QTextBrowser(parent=Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 20, 681, 61))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 250, 311, 181))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vectorlayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vectorlayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.vectorlayout.setContentsMargins(0, 0, 0, 0)
        self.vectorlayout.setObjectName("vectorlayout")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.verticalLayoutWidget)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setStyleSheet("color: white;\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.vectorlayout.addWidget(self.textBrowser)
        self.textBrowser_3 = QtWidgets.QTextBrowser(parent=self.verticalLayoutWidget)
        self.textBrowser_3.setStyleSheet("color: white;\n"
"")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.vectorlayout.addWidget(self.textBrowser_3)
        self.textBrowser_4 = QtWidgets.QTextBrowser(parent=self.verticalLayoutWidget)
        self.textBrowser_4.setStyleSheet("color: white;\n"
"")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.vectorlayout.addWidget(self.textBrowser_4)
        self.textBrowser_5 = QtWidgets.QTextBrowser(parent=self.verticalLayoutWidget)
        self.textBrowser_5.setStyleSheet("color: white;\n"
"")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.vectorlayout.addWidget(self.textBrowser_5)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(parent=Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(660, 250, 81, 181))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.unitlayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.unitlayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.unitlayout.setContentsMargins(0, 0, 0, 0)
        self.unitlayout.setObjectName("unitlayout")
        self.V2QRSunit = QtWidgets.QTextBrowser(parent=self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.V2QRSunit.setFont(font)
        self.V2QRSunit.setStyleSheet("color: white;\n"
"")
        self.V2QRSunit.setObjectName("V2QRSunit")
        self.unitlayout.addWidget(self.V2QRSunit)
        self.QTcunit = QtWidgets.QTextBrowser(parent=self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.QTcunit.setFont(font)
        self.QTcunit.setStyleSheet("color: white;\n"
"")
        self.QTcunit.setObjectName("QTcunit")
        self.unitlayout.addWidget(self.QTcunit)
        self.V3STE60unit = QtWidgets.QTextBrowser(parent=self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.V3STE60unit.setFont(font)
        self.V3STE60unit.setStyleSheet("color: white;\n"
"")
        self.V3STE60unit.setObjectName("V3STE60unit")
        self.unitlayout.addWidget(self.V3STE60unit)
        self.V4Runit = QtWidgets.QTextBrowser(parent=self.verticalLayoutWidget_3)
        self.V4Runit.setStyleSheet("color: white;\n"
"")
        self.V4Runit.setObjectName("V4Runit")
        self.unitlayout.addWidget(self.V4Runit)
        self.textBrowser_6 = QtWidgets.QTextBrowser(parent=Form)
        self.textBrowser_6.setEnabled(True)
        self.textBrowser_6.setGeometry(QtCore.QRect(330, 220, 151, 38))
        self.textBrowser_6.setStyleSheet("color: white;\n"
"")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(parent=Form)
        self.textBrowser_7.setEnabled(True)
        self.textBrowser_7.setGeometry(QtCore.QRect(500, 220, 151, 38))
        self.textBrowser_7.setStyleSheet("color: white;\n"
"")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.draganddropplace = QtWidgets.QTextBrowser(parent=Form)
        self.draganddropplace.setGeometry(QtCore.QRect(200, 90, 391, 121))
        self.draganddropplace.setStyleSheet("border: 2px dashed white;\n"
"background:rgb(20, 20, 20);\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"")
        self.draganddropplace.setObjectName("draganddropplace")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(parent=Form)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(500, 250, 160, 181))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.manuallayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.manuallayout.setContentsMargins(0, 0, 0, 0)
        self.manuallayout.setObjectName("manuallayout")
        self.manualQTc = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget_4)
        self.manualQTc.setStyleSheet("border: 2px solid white;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"")
        self.manualQTc.setObjectName("manualQTc")
        self.manualQTc.setHtml("<div style='text-align:center;'/div>")
        self.manuallayout.addWidget(self.manualQTc)
        self.manualV2 = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget_4)
        self.manualV2.setStyleSheet("border: 2px solid white;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"")
        self.manualV2.setObjectName("manualV2")
        self.manualV2.setHtml("<div style='text-align:center;'/div>")
        self.manuallayout.addWidget(self.manualV2)
        self.manualV3 = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget_4)
        self.manualV3.setStyleSheet("border: 2px solid white;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"")
        self.manualV3.setObjectName("manualV3")
        self.manualV3.setHtml("<div style='text-align:center;'/div>")
        self.manuallayout.addWidget(self.manualV3)
        self.manualV4 = QtWidgets.QTextEdit(parent=self.verticalLayoutWidget_4)
        self.manualV4.setStyleSheet("border: 2px solid white;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"")
        self.manualV4.setObjectName("manualV4")
        self.manualV4.setHtml("<div style='text-align:center;'/div>")
        self.manuallayout.addWidget(self.manualV4)
        self.manual_calculation_button = QtWidgets.QPushButton(parent=Form)
        self.manual_calculation_button.setGeometry(QtCore.QRect(530, 440, 113, 32))
        self.manual_calculation_button.setAutoFillBackground(False)
        self.manual_calculation_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(215, 197, 190);\n"
"border-radius: 5px;\n"
"color: rgb(78, 61, 68);\n"
"    border: 2px solid #a0a0a0; /* Adjust the border as needed */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: rgb(78, 61, 68);\n"
"    background-color: rgb(225, 207, 200);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"color: rgb(78, 61, 68);    \n"
"background-color: rgb(185, 167, 160);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"")
        self.manual_calculation_button.setObjectName("manual_calculation_button")
        self.layoutWidget = QtWidgets.QWidget(parent=Form)
        self.layoutWidget.setGeometry(QtCore.QRect(330, 250, 149, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.Pythonvaluelayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.Pythonvaluelayout.setContentsMargins(0, 0, 0, 0)
        self.Pythonvaluelayout.setObjectName("Pythonvaluelayout")
        self.QTcvalue = QtWidgets.QLabel(parent=self.layoutWidget)
        self.QTcvalue.setEnabled(True)
        self.QTcvalue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.QTcvalue.setStyleSheet("border: 2px solid white;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"\n"
"")
        self.QTcvalue.setText("")
        self.QTcvalue.setObjectName("QTcvalue")
        self.Pythonvaluelayout.addWidget(self.QTcvalue)
        self.V2QRSvalue = QtWidgets.QLabel(parent=self.layoutWidget)
        self.V2QRSvalue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.V2QRSvalue.setStyleSheet("border: 2px solid white;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"")
        self.V2QRSvalue.setText("")
        self.V2QRSvalue.setObjectName("V2QRSvalue")
        self.Pythonvaluelayout.addWidget(self.V2QRSvalue)
        self.V3STE60value = QtWidgets.QLabel(parent=self.layoutWidget)
        self.V3STE60value.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.V3STE60value.setStyleSheet("border: 2px solid white;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"")
        self.V3STE60value.setText("")
        self.V3STE60value.setObjectName("V3STE60value")
        self.Pythonvaluelayout.addWidget(self.V3STE60value)
        self.V4Rvalue = QtWidgets.QLabel(parent=self.layoutWidget)
        self.V4Rvalue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.V4Rvalue.setStyleSheet("border: 2px solid white;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"")
        self.V4Rvalue.setText("")
        self.V4Rvalue.setObjectName("V4Rvalue")
        self.Pythonvaluelayout.addWidget(self.V4Rvalue)
        self.textBrowser_8 = QtWidgets.QTextBrowser(parent=Form)
        self.textBrowser_8.setGeometry(QtCore.QRect(20, 490, 231, 41))
        self.textBrowser_8.setStyleSheet("")
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.frame = QtWidgets.QFrame(parent=Form)
        self.frame.setGeometry(QtCore.QRect(20, 520, 671, 161))
        self.frame.setStyleSheet("border: 2px solid white;\n"
"border-radius: 5px;\n"
"padding: 4px;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.ResultValue = QtWidgets.QLabel(parent=self.frame)
        self.ResultValue.setGeometry(QtCore.QRect(0, 0, 321, 161))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.ResultValue.setFont(font)
        self.ResultValue.setStyleSheet("border: 2px solid white;\n"
"")
        self.ResultValue.setText("")
        self.ResultValue.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.ResultValue.setObjectName("ResultValue")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(320, 0, 351, 161))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: 2px solid white;\n"
"\n"
"\n"
"")
        self.label_2.setObjectName("label_2")
        self.textBrowser_8.raise_()
        self.frame.raise_()
        self.textBrowser_2.raise_()
        self.verticalLayoutWidget.raise_()
        self.verticalLayoutWidget_3.raise_()
        self.textBrowser_6.raise_()
        self.textBrowser_7.raise_()
        self.draganddropplace.raise_()
        self.verticalLayoutWidget_4.raise_()
        self.manual_calculation_button.raise_()
        
        self.layoutWidget.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; color:#fd9391;\">Subtle STEMI Calculator</span></p></body></html>"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">QTc(corrected with Bazett Formula)</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">QRS wave Amplitude of V2 </span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">ST elevation 60ms after J point of V3</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">R wave amplitude of V4</span></p></body></html>"))
        self.V2QRSunit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ms</p></body></html>"))
        self.QTcunit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">mm</p></body></html>"))
        self.V3STE60unit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">mm</p></body></html>"))
        self.V4Runit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">mm</span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Automated Calculation</p></body></html>"))
        self.textBrowser_7.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Manual Calculation</p></body></html>"))
        self.draganddropplace.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Drag ECG file and drop here</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">or</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p></body></html>"))
        self.manual_calculation_button.setText(_translate("Form", "Calculate"))
        self.textBrowser_8.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#4a4a4a;\">Result Value</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "Description"))
    
class TransparentGraphicsView(QtWidgets.QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TransparentForMouseEvents, True)  # Make the widget ignore mouse events

    def dragEnterEvent(self, event):
        event.ignore()  # Ignore the event, allowing it to propagate to the parent

    def dragMoveEvent(self, event):
        event.ignore()  # Ignore the event, allowing it to propagate to the parent

    def dragLeaveEvent(self, event):
        event.ignore()  # Ignore the event, allowing it to propagate to the parent

    def dropEvent(self, event):
        event.ignore()  # Ignore the event, allowing it to propagate to the parent   

 
class DragDropTextBrowser(QtWidgets.QTextBrowser):
    def __init__(self,ui, parent=None):
        super().__init__(parent)
        self.ui = ui
        self.setAcceptDrops(True)
        self.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.setHtml("<p style='text-align:center; color:#ffffff;'>Drag ECG file and drop here</p>")
        self.setGeometry(QtCore.QRect(200, 90, 391, 121))
        self.setStyleSheet("border: 2px dashed white;\n"
                           "background:rgb(20, 20, 20);\n"
                           "border-radius: 5px;\n"
                           "padding: 4px;\n")
        
        # Initialize QGraphicsView but keep it hidden initially
        self.graphicsView = TransparentGraphicsView(self)
        self.graphicsScene = QtWidgets.QGraphicsScene(self.graphicsView)
        self.graphicsView.setScene(self.graphicsScene)
        self.graphicsView.hide()  # Hide the graphics view by default

        # Load an icon or image to display
        self.icon = QtGui.QPixmap("/Users/huangliangjun/Desktop/ECGproject/20240210GUI/upload.png")
        scaled_icon = self.icon.scaled(50, 50, QtCore.Qt.AspectRatioMode.KeepAspectRatio)  # Adjust 200, 200 to your desired size
        self.graphicsView.setGeometry(120,-10,150,150)  # Match the geometry of the QTextBrowser
        self.graphicsScene.addPixmap(scaled_icon)
        self.graphicsView.raise_()
        self.graphicsView.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing, True)
        self.graphicsView.setRenderHint(QtGui.QPainter.RenderHint.SmoothPixmapTransform, True)

        self.graphicsView.setStyleSheet("background: transparent; border: none;")  # Make background transparent


    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            # Change the background color to indicate an active drag operation
            self.setStyleSheet("border: 2px dashed white;\n"
                               "background-color: rgb(50, 50, 50);\n"  # Darker shade when dragging over
                               "border-radius: 5px;\n"
                               "padding: 4px;\n")
            self.graphicsView.show()



    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
            
    def dragLeaveEvent(self, event):
        # Revert the background color when the drag operation leaves the widget
        self.setStyleSheet("border: 2px dashed white;\n"
                           "background:rgb(20, 20, 20);\n"
                           "border-radius: 5px;\n"
                           "padding: 4px;\n")
        self.graphicsView.hide()  
    
    
    def dropEvent(self, event):
        files = [url.toLocalFile() for url in event.mimeData().urls()]
        self.setHtml("<p style='text-align:center; color:#ffffff;'>Drag ECG file and drop here</p>")
        # Here you can add what you want to do with the files, e.g., processing them
        if files:
                self.filePath = files[0]
                main = mainprocessor(self.filePath)
                resultlist = main.mainprocessor()
                resultlist = [round(i,2) for i in resultlist]
                if len(resultlist) >= 4:  # Check to avoid index errors
                        self.ui.QTcvalue.setText(str(resultlist[0]))
                        self.ui.V2QRSvalue.setText(str(resultlist[1]))
                        self.ui.V3STE60value.setText(str(resultlist[2]))
                        self.ui.V4Rvalue.setText(str(resultlist[3]))
                        self.ui.ResultValue.setText(str(resultlist[4]))
                        if resultlist[4] > 18.2:
                                self.ui.ResultValue.setStyleSheet("QLabel { color: red; }")
                                self.ui.label_2.setText("This ECG value indicates that patient is <br>more likely to have Anterior STEMI.")
                        else:
                                self.ui.ResultValue.setStyleSheet("QLabel { color: white; }")
                                self.ui.label_2.setText("This ECG value suggests that patient <br>may be Benign Early Repolarization.")
        self.setStyleSheet("border: 2px dashed white;\n"
                           "background:rgb(20, 20, 20);\n"
                           "border-radius: 5px;\n"
                           "padding: 4px;\n")
        self.graphicsView.hide()
        
        
        
                                
class MyApplication(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Correctly activate drag-and-drop
        self.draganddropplace = DragDropTextBrowser(self.ui, parent=self)

        # Connect the calculate button's clicked signal to the calculateResults method
        self.ui.manual_calculation_button.clicked.connect(self.calculateResults)

    def calculate_ecg_value(self, qtc, v2, v3, v4):
        """Calculates the ECG value based on inputs."""
        # It's assumed that the inputs are already converted to float and validated
        return qtc * 0.052 - v2 * 0.151 + v3 * 1.062 - v4 * 0.268

    def calculateResults(self):
        # Correctly access the manual inputs
        inputs = [self.ui.manualQTc.toPlainText(), self.ui.manualV2.toPlainText(),
                  self.ui.manualV3.toPlainText(), self.ui.manualV4.toPlainText()]
        try:
            float_inputs = [float(input_text) for input_text in inputs]
        except ValueError:
            # Update UI to alert the user about the invalid input
            self.ui.label_2.setText("Invalid input detected. Please enter numeric values only.")
            return

        qtc, v2, v3, v4 = float_inputs
        calculated_value = self.calculate_ecg_value(qtc, v2, v3, v4)

        # Update QLabel with the calculated value
        self.ui.ResultValue.setText(f"{calculated_value:.2f}")

        if calculated_value > 18.2:
            self.ui.ResultValue.setStyleSheet("QLabel { color: red; }")
            self.ui.label_2.setText("This ECG value indicates that the patient is <br>more likely to have Anterior STEMI.")
        else:
            self.ui.ResultValue.setStyleSheet("QLabel { color: white; }")
            self.ui.label_2.setText("This ECG value suggests that the patient <br>may have Benign Early Repolarization.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Instantiate MyApplication instead of setting up UI_Form directly
    myApp = MyApplication()

    myApp.show()
    sys.exit(app.exec())
