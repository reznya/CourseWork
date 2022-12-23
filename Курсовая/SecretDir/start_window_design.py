# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_window_design.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import resources

class Ui_StartWindow(object):
    def setupUi(self, StartWindow):
        if not StartWindow.objectName():
            StartWindow.setObjectName(u"StartWindow")
        StartWindow.resize(396, 175)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StartWindow.sizePolicy().hasHeightForWidth())
        StartWindow.setSizePolicy(sizePolicy)
        StartWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #143944;\n"
"    color: #9ecedd;\n"
"    font-family: Verdana;\n"
"    font-size: 16pt;\n"
"    margin: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: #9ecedd;\n"
"    border: 2px solid #9ecedd;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton#btn_lower,\n"
"#btn_upper,\n"
"#btn_digits,\n"
"#btn_special {\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    color:#0ba5d3;\n"
"    border-color: #0ba5d3;;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 4px solid #0ba5d3;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #0ba5d3;\n"
"    border-color: #0ba5d3;\n"
"}\n"
"")
        self.centralwidget = QWidget(StartWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.enterBtn = QPushButton(self.centralwidget)
        self.enterBtn.setObjectName(u"enterBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.enterBtn.sizePolicy().hasHeightForWidth())
        self.enterBtn.setSizePolicy(sizePolicy1)
        self.enterBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.enterBtn, 1, 0, 1, 1)

        self.cancelBtn = QPushButton(self.centralwidget)
        self.cancelBtn.setObjectName(u"cancelBtn")
        sizePolicy1.setHeightForWidth(self.cancelBtn.sizePolicy().hasHeightForWidth())
        self.cancelBtn.setSizePolicy(sizePolicy1)
        self.cancelBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.cancelBtn, 1, 1, 1, 1)

        self.frameKey = QFrame(self.centralwidget)
        self.frameKey.setObjectName(u"frameKey")
        self.frameKey.setCursor(QCursor(Qt.PointingHandCursor))
        self.frameKey.setStyleSheet(u"QFrame {\n"
"    color: #9ecedd;\n"
"    border: 2px solid #9ecedd;\n"
"    border-radius: 5px;\n"
"    margin-right: 0;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    border-color: #26acd5;\n"
"}\n"
"")
        self.frameKey.setFrameShape(QFrame.StyledPanel)
        self.frameKey.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frameKey)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.entryKey = QLineEdit(self.frameKey)
        self.entryKey.setObjectName(u"entryKey")
        self.entryKey.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.entryKey.sizePolicy().hasHeightForWidth())
        self.entryKey.setSizePolicy(sizePolicy2)
        self.entryKey.setBaseSize(QSize(0, 0))
        self.entryKey.setStyleSheet(u"QLineEdit {\n"
"    border: none;\n"
"    margin: 0;\n"
"    font-size: 20pt;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.entryKey, 0, 0, 1, 1)

        self.visibilityBtn = QPushButton(self.frameKey)
        self.visibilityBtn.setObjectName(u"visibilityBtn")
        sizePolicy.setHeightForWidth(self.visibilityBtn.sizePolicy().hasHeightForWidth())
        self.visibilityBtn.setSizePolicy(sizePolicy)
        self.visibilityBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.visibilityBtn.setStyleSheet(u"QPushButton {\n"
"    border: none;\n"
"    margin: 0;\n"
"    background-color: transparent;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/invisible.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/icons/icons/visible.svg", QSize(), QIcon.Normal, QIcon.On)
        self.visibilityBtn.setIcon(icon)
        self.visibilityBtn.setIconSize(QSize(30, 30))
        self.visibilityBtn.setCheckable(True)
        self.visibilityBtn.setChecked(True)

        self.gridLayout_2.addWidget(self.visibilityBtn, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frameKey, 0, 0, 1, 2)

        StartWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(StartWindow)

        self.visibilityBtn.setDefault(False)


        QMetaObject.connectSlotsByName(StartWindow)
    # setupUi

    def retranslateUi(self, StartWindow):
        StartWindow.setWindowTitle(QCoreApplication.translate("StartWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043b\u044e\u0447", None))
        self.enterBtn.setText(QCoreApplication.translate("StartWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438", None))
#if QT_CONFIG(shortcut)
        self.enterBtn.setShortcut(QCoreApplication.translate("StartWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.cancelBtn.setText(QCoreApplication.translate("StartWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.visibilityBtn.setText("")
    # retranslateUi

