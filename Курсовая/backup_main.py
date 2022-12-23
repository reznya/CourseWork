import sys, os, subprocess
import usb.core
import usb.util
from Crypto.Cipher import DES
from crc64iso.crc64iso import crc64
from appscript import mactypes as mt
# from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale, 
    QMetaObject, QObject, QPoint, QRect, 
    QSize, QTime, QUrl, Qt, QDir)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QShortcut)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,QDialog,
    QVBoxLayout, QWidget, QFileSystemModel, QMenu, QWidgetAction, QMessageBox, QGraphicsDropShadowEffect)
from main_design import Ui_MainWindow
from key_form import Ui_KeyForm

def check_flash():
        USB_I_PRODUCT = ' SanDisk 3.2Gen1'
        USB_I_SERIAL_NUMBER = '0101ee0d9f826beb78a17113e022ebcf29d23b6b86e8444ec6dcd7e46515aee2e49a0000000000000000000030e6ef26001e2e00ab5581073e2a87d2'
        usb_dict = {}
        for dev in usb.core.find(find_all=True):
            for cfg in dev:
                intf = usb.util.find_descriptor(cfg, bInterfaceClass=0x8)
                if intf is not None:
                    usb_dict[usb.util.get_string(dev, dev.iProduct)] = usb.util.get_string(dev, dev.iSerialNumber)
        if USB_I_PRODUCT in usb_dict:
            if usb_dict[USB_I_PRODUCT] == USB_I_SERIAL_NUMBER:
                return True
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText("Неверная конфигурация аутентификатора")
                msg.setIcon(QMessageBox.Critical)
                msg.exec()
                sys.exit()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Вставьте аутентификатор!")
            msg.setIcon(QMessageBox.Critical)
            msg.exec()
            sys.exit()
class EnterKeyWindow(QDialog):
    def __init__(self):
        HASHES_PATH = '5 курс/Курсач/Курсовая/hashes'
        if check_flash():
            super(EnterKeyWindow, self).__init__()
            # self.show()
            self.ui = Ui_KeyForm()
            self.ui.setupUi(self)
            self.ui.enterBtn.clicked.connect(self.show_new_window)
            self.ui.visibilityBtn.clicked.connect(self.change_password_visibility)
            # self.ui.enterBtn.clicked.connect(self.auth)
            self.ui.cancelBtn.clicked.connect(self.get_out)

            # self.master = master

    def auth(self):
        self.key = self.ui.entryKey.text()
        if self.key == 'xd':
            self.show_new_window()
        # super().auth()
    def get_out(self):
        sys.exit()
    
    def show_new_window(self):
        if check_flash():
            # xd = MainApp()
            main_window.show()
            self.hide()
            # del self
        
    def change_password_visibility(self):
        if check_flash():
            if self.ui.visibilityBtn.isChecked():
                self.ui.entryKey.setEchoMode(QLineEdit.Password)
            else:
                self.ui.entryKey.setEchoMode(QLineEdit.Normal)
    
    def __del__(self):
        print('im dead')

class MainApp(QMainWindow, EnterKeyWindow):
    def __init__(self):
        # auth_form = EnterKeyWindow(self)
        # auth_form.exec()
        # print(self.key)
        # if self.key == 'xd':
        #     self.show()
        #     del auth_form
        # auth_form.show()
        # print(self.key)
            if check_flash():
                # print(self.key)
                super(MainApp, self).__init__()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self)
                self.populate()
                self.ui.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
                self.ui.treeView.customContextMenuRequested.connect(self.openMenu)
    @staticmethod
    def __append_last_bytes(text):
        length = 8 - len(text) % 8
        text = text.ljust(len(text) + length, length.to_bytes(1, 'big'))
        return text

    @staticmethod
    def __delete_last_bytes(text):
        length = text[-1]
        if length > 8:
            
            raise Exception()
        return text[:-length]

    def openMenu(self, point):
        try:
            if check_flash():
                i = self.ui.treeView.selectedIndexes()[0]
                # print(i.model())
                file_to_show = [i.model().filePath(i), i.model().isDir(i)]

                menu = QMenu()
                menu.setGraphicsEffect(QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0, color=QColor(234, 221, 186, 100)))
                crypt_option = menu.addAction('Зашифровать файл')
                decrypt_option = menu.addAction('Расшифровать файл')
                exit_option = menu.addAction('Показать в Finder')

                crypt_option.triggered.connect(lambda: self.crypt_file(file_to_show))
                decrypt_option.triggered.connect(lambda: self.decrypt_file(file_to_show))
                exit_option.triggered.connect(lambda: subprocess.call(["open", "-R",file_to_show[0]]))
                # self.cr_shrt = QShortcut(QKeySequence('Command+O'), self)
                # self.cr_shrt.activated.connect(lambda: subprocess.call(["open", "-R",file_to_show]))

                menu.exec(self.mapToGlobal(point))
        except:
            pass
    def populate(self):
        if check_flash():
            path = "/Users/nikita/Desktop"
            self.model = QFileSystemModel()
            self.model.setRootPath(path)
            self.ui.treeView.setModel(self.model)
        # self.ui.treeView.doubleClicked.connect(self.test)

    def crypt_file(self, file_to_show):
        # if file_to_show.isDir():
        if check_flash():
            if not file_to_show[1]:
                xd = []
                with open(file_to_show[0], 'rb') as f:
                    enc_file1 = f.read()
                xd.append(file_to_show[0])
                enc_file = self.__append_last_bytes(enc_file1)
                des = DES.new(bytes.fromhex(crc64(str('xddxddxdd'))), DES.MODE_CFB)
                encrypted_data = des.encrypt(enc_file)
                with open(f"{file_to_show[0]}.enc", 'wb') as f:
                    f.write(encrypted_data)
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText("Вы не можете зашифровать папку!")
                msg.setIcon(QMessageBox.Warning)
                msg.exec()
            
    def decrypt_file(self, file_to_show):
        if check_flash():
            if not file_to_show[1]:
                xd = []
                xd.append(file_to_show[0])                              
                if file_to_show[0].split('/')[-1].split('.')[-1] != 'enc':
                    msg = QMessageBox()
                    msg.setWindowTitle("Ошибка")
                    msg.setText("Файл имеет неверное расширение.")
                    msg.setIcon(QMessageBox.Warning)
                    msg.exec()
                with open(file_to_show[0], 'rb') as f:
                    dec_file = f.read()         
                des = DES.new(bytes.fromhex(crc64(str('xddxddxdd'))), DES.MODE_CFB)
                decrypted_data = des.decrypt(dec_file)
                d1 = self.__delete_last_bytes(decrypted_data)
                f_name_to_decode = '.'.join(['.'.join(file_to_show[0][:-4].split('.')[:-1])+'_decoded', file_to_show[0][:-4].split('.')[-1]])
                with open(f"{f_name_to_decode}", 'wb') as f:
                    f.write(d1)
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText("Вы не можете расшифровать папку!")
                msg.setIcon(QMessageBox.Warning)
                msg.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EnterKeyWindow()
    window.show()
    main_window = MainApp()
    main_window.hide()
    sys.exit(app.exec()) 