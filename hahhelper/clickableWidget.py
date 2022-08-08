from PyQt5 import QtCore, QtGui, QtWidgets
import resources.resource


class CW(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.clickable_widget = QtWidgets.QWidget()
        self.clickable_widget.setMinimumSize(351, 80)
        self.clickable_widget.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.clickable_widget.setGeometry(QtCore.QRect(130, 130, 351, 80))
        self.clickable_widget.setStyleSheet("QWidget {\n"
                                            "    border-radius: 10px;\n"
                                            "    border: 1px solid black;\n"
                                            "    background-image: url(:/wood/bg_list.png);\n"
                                            "}\n"
                                            "QWidget::hover {\n"
                                            "    background-image: url(:/wood/bg_list1.png);\n"
                                            "    background-color: rgb(199, 112, 57);\n"
                                            "}\n"
                                            "")
        self.clickable_widget.setObjectName("clickable_widget")
        self.name = QtWidgets.QLabel(self.clickable_widget)
        self.name.setGeometry(QtCore.QRect(80, 10, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Vin Slab Pro")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.name.setFont(font)
        self.name.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.name.setAutoFillBackground(False)
        self.name.setStyleSheet("QLabel {\n"
                                "    background-image: None;\n"
                                "    background: None;\n"
                                "    border: None;\n"
                                "}\n"
                                "")
        self.name.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.name.setWordWrap(False)
        self.name.setObjectName("name")
        self.icnwidget = QtWidgets.QWidget(self.clickable_widget)
        self.icnwidget.setGeometry(QtCore.QRect(10, 10, 61, 61))
        self.icnwidget.setStyleSheet("QWidget {\n"
                                     "    border: 1px solid black;\n"
                                     "    background: None;\n"
                                     "    background-color: rgb(255, 255, 255);\n"
                                     "\n"
                                     "}\n"
                                     "")
        self.icnwidget.setObjectName("icnwidget")
        self.icnlabel = QtWidgets.QLabel(self.icnwidget)
        self.icnlabel.setGeometry(QtCore.QRect(5, 5, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Vin Slab Pro")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.icnlabel.setFont(font)
        self.icnlabel.setStyleSheet("QLabel {\n"
                                    "    background: None;\n"
                                    "    border: None;\n"
                                    "    background-color: rgb(255, 255, 255);\n"
                                    "}")
        self.icnlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.icnlabel.setObjectName("icnlabel")

