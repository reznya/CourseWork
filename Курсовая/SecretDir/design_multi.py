# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test_multi_windows.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(432, 163)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    color: white;\n"
"    background-color: cadetblue;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pushButton)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

class Ui_SecondaryWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(100, 100)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    color: white;\n"
"    background-color: cadetblue;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        # self.centralwidget.setObjectName(u"centralwidget")
        # self.verticalLayout = MainWindow(self.centralwidget)
        # self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)

        # self.verticalLayout.addWidget(self.btn_1)

        # MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        # QVBoxLayout.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"btn_1", None))
    # retranslateUi

