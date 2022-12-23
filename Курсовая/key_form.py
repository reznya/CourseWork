# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'key_form.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QWidget)
import resources

class Ui_KeyForm(object):
    def setupUi(self, KeyForm):
        if not KeyForm.objectName():
            KeyForm.setObjectName(u"KeyForm")
        KeyForm.resize(396, 137)
        font = QFont()
        font.setFamilies([u"Roboto"])
        font.setPointSize(16)
        font.setBold(False)
        KeyForm.setFont(font)
        KeyForm.setAcceptDrops(False)
        KeyForm.setWindowOpacity(1.000000000000000)
        KeyForm.setStyleSheet(u"@import url('https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,300;0,400;1,300&display=swap');\n"
"QWidget {\n"
"    background-color: #2d2c3a;\n"
"    color: #e8e8e8;\n"
"    font-family: Roboto;\n"
"    font-weight: 400;\n"
"    font-size: 16pt;\n"
"}\n"
"\n"
"QPushButton {\n"
"    color: #e8e8e8;\n"
"    border: 2px solid #747282;\n"
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
"    color: #89beb3;\n"
"    border-color: #89beb3;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 4px solid #89beb3;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #89beb3;\n"
"    border-color: #89beb3;\n"
"}\n"
"")
        self.gridLayout = QGridLayout(KeyForm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.cancelBtn = QPushButton(KeyForm)
        self.cancelBtn.setObjectName(u"cancelBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelBtn.sizePolicy().hasHeightForWidth())
        self.cancelBtn.setSizePolicy(sizePolicy)
        self.cancelBtn.setMinimumSize(QSize(181, 39))
        self.cancelBtn.setMaximumSize(QSize(181, 39))
        self.cancelBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.cancelBtn, 1, 1, 1, 1)

        self.enterBtn = QPushButton(KeyForm)
        self.enterBtn.setObjectName(u"enterBtn")
        sizePolicy.setHeightForWidth(self.enterBtn.sizePolicy().hasHeightForWidth())
        self.enterBtn.setSizePolicy(sizePolicy)
        self.enterBtn.setMinimumSize(QSize(181, 39))
        self.enterBtn.setMaximumSize(QSize(181, 39))
        self.enterBtn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout.addWidget(self.enterBtn, 1, 0, 1, 1)

        self.frameKey = QFrame(KeyForm)
        self.frameKey.setObjectName(u"frameKey")
        self.frameKey.setMinimumSize(QSize(372, 58))
        self.frameKey.setMaximumSize(QSize(372, 58))
        self.frameKey.setCursor(QCursor(Qt.PointingHandCursor))
        self.frameKey.setStyleSheet(u"QFrame {\n"
"    color: #747282;\n"
"    border: 2px solid #747282;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QFrame:hover {\n"
"    border-color: #89beb3;\n"
"}\n"
"")
        self.frameKey.setFrameShape(QFrame.StyledPanel)
        self.frameKey.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frameKey)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.entryKey = QLineEdit(self.frameKey)
        self.entryKey.setObjectName(u"entryKey")
        self.entryKey.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.entryKey.sizePolicy().hasHeightForWidth())
        self.entryKey.setSizePolicy(sizePolicy1)
        self.entryKey.setBaseSize(QSize(0, 0))
        self.entryKey.setStyleSheet(u"QLineEdit {\n"
"    border: none;\n"
"    margin: 0;\n"
"    font-size: 20pt;\n"
"}\n"
"")
        self.entryKey.setEchoMode(QLineEdit.Password)

        self.gridLayout_2.addWidget(self.entryKey, 0, 0, 1, 1)

        self.visibilityBtn = QPushButton(self.frameKey)
        self.visibilityBtn.setObjectName(u"visibilityBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.visibilityBtn.sizePolicy().hasHeightForWidth())
        self.visibilityBtn.setSizePolicy(sizePolicy2)
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


        self.retranslateUi(KeyForm)

        self.visibilityBtn.setDefault(False)


        QMetaObject.connectSlotsByName(KeyForm)
    # setupUi

    def retranslateUi(self, KeyForm):
        KeyForm.setWindowTitle(QCoreApplication.translate("KeyForm", u"\u0412\u0445\u043e\u0434", None))
        self.cancelBtn.setText(QCoreApplication.translate("KeyForm", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.enterBtn.setText(QCoreApplication.translate("KeyForm", u"\u0412\u0432\u0435\u0441\u0442\u0438", None))
#if QT_CONFIG(shortcut)
        self.enterBtn.setShortcut(QCoreApplication.translate("KeyForm", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.visibilityBtn.setText("")
#if QT_CONFIG(shortcut)
        self.visibilityBtn.setShortcut(QCoreApplication.translate("KeyForm", u"Ctrl+H", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

