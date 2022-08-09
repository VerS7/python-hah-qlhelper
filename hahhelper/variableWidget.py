from PyQt5 import QtCore, QtGui, QtWidgets
import resource


class VW(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.variables_widget = QtWidgets.QWidget()
        self.variables_widget.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.variables_widget.setGeometry(QtCore.QRect(210, 200, 301, 51))
        self.variables_widget.setMinimumSize(301, 51)
        self.variables_widget.setStyleSheet("QWidget {\n"
"    border-radius: 10px;\n"
"    border: 1px solid black;\n"
"    background-image: url(:/stone/stonepap.png);\n"
"}")
        self.variables_widget.setObjectName("variables_widget")
        self.enter = QtWidgets.QLineEdit(self.variables_widget)
        self.enter.setGeometry(QtCore.QRect(230, 6, 61, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(61)
        sizePolicy.setVerticalStretch(31)
        sizePolicy.setHeightForWidth(self.enter.sizePolicy().hasHeightForWidth())
        self.enter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Vin Slab Pro")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.enter.setFont(font)
        self.enter.setStyleSheet("QLineEdit {\n"
"    color: rgb(255, 255, 255);\n"
"    background-image: url(:/cloth/bgtex.png);\n"
"}\n"
"QLineEdit::hover {\n"
"    background-image: url(:/cloth/bgtex1.png);\n"
"}")
        self.enter.setAlignment(QtCore.Qt.AlignCenter)
        self.enter.setObjectName("enter")
        self.name = QtWidgets.QLabel(self.variables_widget)
        self.name.setGeometry(QtCore.QRect(10, 11, 220, 30))
        font = QtGui.QFont()
        font.setFamily("Vin Slab Pro")
        font.setPointSize(21)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setStyleSheet("QLabel {\n"
"    background: None;\n"
"    border: None;\n"
"}")
        self.name.setObjectName("name")
