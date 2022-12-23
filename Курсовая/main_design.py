# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_design.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableView, QTreeView,
    QVBoxLayout, QWidget)
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
            MainWindow.resize(1278, 660)
        MainWindow.setStyleSheet(u"@import url('https://fonts.googleapis.com/css2family=Roboto:ital,wght@0,300;0,400;1,300&display=swap');\n"
"QWidget {    \n"
"background-color: #2d2c3a;\n"
"color: #e8e8e8;    \n"
"font-family: Roboto;    \n"
"font-weight: 400;    \n"
"font-size: 16pt;\n"
"}\n"
"QTabBar::tab {\n"
"    background: #6B7581;\n"
"    border: 2px solid #747282;\n"
"    border-top-left-radius: 2px;\n"
"    border-top-right-radius: 2px;\n"
"    min-width: 5ex;\n"
"    margin-left: 5px; \n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background-color: #404049;\n"
"    color: #89beb3;\n"
"    border-color: #89beb3;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 4px;\n"
"    margin-left: 4px;\n"
"    margin-right: 4px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    margin-left: 4px;\n"
"    margin-right: 4px;\n"
"}\n"
"QTabBar::tab:first:selected {\n"
"    margin-left: 0; \n"
"    margin-right: 4; \n"
"}\n"
"\n"
"QTabBar::tab:last:selected {\n"
"    margin-right: ; \n"
"    margin-left: 4; \n"
""
                        "}\n"
"\n"
"QTabBar::tab:only-one {\n"
"    margin: 0; \n"
"}\n"
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget.setStyleSheet(u"QTreeView::item:selected{\n"
"    background-color: #89beb3;\n"
"    color: #2d2c3a;\n"
"}\n"
"QTabWidget {\n"
"color: black;\n"
"}\n"
"QHeaderView::section {\n"
"    background-color: #718F89;\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"border-color: #89beb3;\n"
"}\n"
"\n"
"QHeaderView::section:checked\n"
"{\n"
"    background-color: #747282;\n"
"}\n"
"")
        self.files_tab = QWidget()
        self.files_tab.setObjectName(u"files_tab")
        self.verticalLayout = QVBoxLayout(self.files_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.treeView = QTreeView(self.files_tab)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setStyleSheet(u"QTreeView::item:selected{\n"
"    background-color: #718F89;\n"
"}\n"
"QMenu {\n"
"    background-color: white;\n"
"    margin: 2px; /* some spacing around the menu */\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 2px 25px 2px 20px;\n"
"    border: 1px solid transparent; /* reserve space for selection border */\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    border-color: darkblue;\n"
"    background: #89beb3;\n"
"}\n"
"\n"
"QMenu::icon:checked { /* appearance of a 'checked' icon */\n"
"    background: gray;\n"
"    border: 1px inset gray;\n"
"    position: absolute;\n"
"    top: 1px;\n"
"    right: 1px;\n"
"    bottom: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    height: 2px;\n"
"    background: lightblue;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QMenu::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"}")
        self.treeView.header().setDefaultSectionSize(140)

        self.gridLayout_2.addWidget(self.treeView, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)

        self.tabWidget.addTab(self.files_tab, "")
        self.data_integer_tab = QWidget()
        self.data_integer_tab.setObjectName(u"data_integer_tab")
        self.gridLayout_4 = QGridLayout(self.data_integer_tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.backup_btn = QPushButton(self.data_integer_tab)
        self.backup_btn.setObjectName(u"backup_btn")
        self.backup_btn.setCursor(QCursor(Qt.PointingHandCursor))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backup_btn.sizePolicy().hasHeightForWidth())
        self.backup_btn.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.backup_btn, 2, 1, 1, 1)

        self.hashes_to_file_btn = QPushButton(self.data_integer_tab)
        self.hashes_to_file_btn.setObjectName(u"hashes_to_file_btn")
        self.hashes_to_file_btn.setCursor(QCursor(Qt.PointingHandCursor))

        sizePolicy.setHeightForWidth(self.hashes_to_file_btn.sizePolicy().hasHeightForWidth())
        self.hashes_to_file_btn.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.hashes_to_file_btn, 0, 1, 1, 1)

        self.check_integrity_btn = QPushButton(self.data_integer_tab)
        self.check_integrity_btn.setObjectName(u"check_integrity_btn")
        self.check_integrity_btn.setCursor(QCursor(Qt.PointingHandCursor))

        sizePolicy.setHeightForWidth(self.check_integrity_btn.sizePolicy().hasHeightForWidth())
        self.check_integrity_btn.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.check_integrity_btn, 4, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.tableView = QTableView(self.data_integer_tab)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout_4.addWidget(self.tableView, 0, 0, 5, 1)

        self.tabWidget.addTab(self.data_integer_tab, "")
        self.logs_tab = QWidget()
        self.logs_tab.setObjectName(u"logs_tab")
        self.gridLayout_5 = QGridLayout(self.logs_tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.logs_frame = QFrame(self.logs_tab)
        self.logs_frame.setObjectName(u"logs_frame")
        self.logs_frame.setStyleSheet(u"QFrame {\n"
"    color: #747282;\n"
"    border: 2px solid #747282;\n"
"    border-radius: 5px;\n"
"}\n"
"QFrame:hover {\n"
"    border-color: #89beb3;\n"
"}")
        self.logs_frame.setFrameShape(QFrame.StyledPanel)
        self.logs_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.logs_frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.logs_TextEdit = QPlainTextEdit(self.logs_frame)
        self.logs_TextEdit.setObjectName(u"logs_TextEdit")
        self.logs_TextEdit.setStyleSheet(u"QPlainTextEdit {\n"
"    border: none;\n"
"    margin: 0;\n"
"    font-size: 14pt;\n"
"    font-family: Roboto;\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.logs_TextEdit.setReadOnly(False)
        self.logs_TextEdit.setBackgroundVisible(False)

        self.gridLayout_6.addWidget(self.logs_TextEdit, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.logs_frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.logs_tab, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0435", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.files_tab), QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b\u044b", None))
        self.backup_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0440\u0435\u0437\u0435\u0440\u0432\u043d\u043e\u0435 \u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.hashes_to_file_btn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u044c \u0434\u0430\u043d\u043d\u044b\u0445 \u043e \u0446\u0435\u043b\u043e\u0441\u0442\u043d\u043e\u0441\u0442\u0438 \u0432 \u0444\u0430\u0439\u043b", None))
        self.check_integrity_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u0432\u0441\u0435 \u0444\u0430\u0439\u043b\u044b \u043d\u0430 \u0446\u0435\u043b\u043e\u0441\u0442\u043d\u043e\u0441\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.data_integer_tab), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u043a\u0430 \u0446\u0435\u043b\u043e\u0441\u0442\u043d\u043e\u0441\u0442\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.logs_tab), QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438", None))
    # retranslateUi

