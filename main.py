import sys
from random import randint

from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor

a = 10
b = 50
aa = 5
bb = 10


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.drawCircleBtn = QtWidgets.QPushButton(self.centralwidget)
        self.drawCircleBtn.setObjectName("drawCircleBtn")

        self.gridLayout.addWidget(self.drawCircleBtn, 1, 0, 1, 1)
        self.canvas = QtWidgets.QLabel(self.centralwidget)
        self.canvas.setText("")
        self.canvas.setObjectName("canvas")
        self.gridLayout.addWidget(self.canvas, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow",
                                             "прога"))
        self.drawCircleBtn.setText(_translate("MainWindow", "PushButton"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        self.do_paint = False
        self.drawCircleBtn.clicked.connect(self.paint)

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paintEvent(self, event: QtGui.QPaintEvent):
        if self.do_paint:
            painter = QPainter()
            painter.begin(self)
            self.drawCircle(painter)
            painter.end()

    def drawCircle(self, qp: QPainter):
        colored = QColor(0xffff00)
        qp.setPen(colored)
        qp.setBrush(colored)

        for i in range(randint(aa, bb)):
            w, h = self.canvas.width(), self.canvas.height()
            r = randint(a, b)
            qp.drawEllipse(randint(0, w - r), randint(0, h - r), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
