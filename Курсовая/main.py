import sys, os, subprocess, json, usb.core, usb.util, hashlib, resources, yadisk
from Crypto.Cipher import DES
from crc64iso.crc64iso import crc64
from appscript import mactypes as mt
from PySide6.QtCore import (Qt,QAbstractTableModel,QModelIndex)
from PySide6.QtGui import (QBrush, QColor, QStandardItemModel, QStandardItem,)
from PySide6.QtWidgets import (QApplication, QLineEdit, QMainWindow,
     QDialog, QFileSystemModel, QMenu, QMessageBox, QHeaderView)
from main_design import Ui_MainWindow
from key_form import Ui_KeyForm
from datetime import datetime #'генерация ключа производителем'
from json_helper import FilesModel, FilesEncoder

class Variables:
    auth_key_hash = ""
    login_window = None
    main_window = None
    usb_id_product_hash = ""
    disk = yadisk.YaDisk(token = 'y0_AgAAAAAjaLh8AAjklAAAAADXIucEEugnEiGdRmawo04eu9Dra4Vl94c')

def init_main_window():
    Variables.main_window = MainApp()
    Variables.main_window.show()
    del Variables.login_window

def check_flash():
        usb_serial_n_hash = ''
        with open(f"{os.path.dirname(os.path.abspath(__file__))}/hashes/flash_hash.json", "r") as f:
            usb_dict = json.load(f)
        for dev in usb.core.find(find_all=True):
            for cfg in dev:
                intf = usb.util.find_descriptor(cfg, bInterfaceClass=0x8)       
                if intf is not None:
                    usb_serial_n_hash = hashlib.sha1(str.encode(usb.util.get_string(dev, dev.iSerialNumber))).hexdigest()
                    Variables.usb_id_product_hash = hashlib.sha1(str.encode(usb.util.get_string(dev, dev.iProduct))).hexdigest()

        if Variables.usb_id_product_hash in usb_dict:
            if usb_dict[Variables.usb_id_product_hash] == usb_serial_n_hash:
                return True
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText("Неверная конфигурация аутентификатора")
                msg.setIcon(QMessageBox.Critical)
                msg.exec()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Вставьте аутентификатор!")
            msg.setIcon(QMessageBox.Critical)
            msg.exec()
            sys.exit()
def get_model_from_path(path):

    files_model = []
    if os.path.isdir(path):
        for (dirpath, dirnames, filenames) in os.walk(path):
            for file in filenames:
                if os.path.exists(os.path.join(dirpath, file)):
                    ts = int(os.path.getmtime(os.path.join(dirpath, file)))
                    modified_date = str(datetime.fromtimestamp(int(ts)))
                    model = FilesModel(os.path.join(dirpath, file), hashlib.sha1(open(os.path.join(dirpath, file), 'rb').read()).hexdigest(), modified_date)
                    files_model.append(model)
                else:
                    break
    else:
        files_model = [FilesModel(path, hashlib.sha1(open(path, 'rb').read()).hexdigest(), str(datetime.fromtimestamp(int(os.path.getmtime(path)))))]
    return files_model
class EnterKeyWindow(QDialog):
    def __init__(self):
        super(EnterKeyWindow, self).__init__()
        if check_flash():
            self.ui = Ui_KeyForm()
            self.ui.setupUi(self)

            self.ui.visibilityBtn.clicked.connect(self.change_password_visibility)
            self.ui.enterBtn.clicked.connect(self.accept)
            self.ui.cancelBtn.clicked.connect(self.get_out)

    def accept(self):
        if check_flash():
            with open(f"{os.path.dirname(os.path.abspath(__file__))}/hashes/passwd.json", "r") as f:
                psswd_dict = json.load(f)
            auth_key = self.ui.entryKey.text()
            Variables.auth_key_hash = hashlib.sha1(str.encode(auth_key)).hexdigest()
            if Variables.usb_id_product_hash in psswd_dict:
                if Variables.auth_key_hash == psswd_dict[Variables.usb_id_product_hash]:
                    init_main_window()
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Ошибка")
                    msg.setText("Неверный пароль!")
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText("Неверный аутентификатор!")
                msg.setIcon(QMessageBox.Critical)
                msg.exec()      # sys.exit()

    def get_out(self):
        sys.exit()
    
    def change_password_visibility(self):
        if check_flash():
            if self.ui.visibilityBtn.isChecked():
                self.ui.entryKey.setEchoMode(QLineEdit.Password)
            else:
                self.ui.entryKey.setEchoMode(QLineEdit.Normal)

class MainApp(QMainWindow):
    def __init__(self):
        if check_flash():
            super(MainApp, self).__init__()
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.treeView.setContextMenuPolicy(Qt.CustomContextMenu)
            self.ui.treeView.customContextMenuRequested.connect(self.openMenu)
            self.ui.treeView.setColumnWidth(1, 300)
            self.init_table_view()
            
            self.ui.tableView.doubleClicked[QModelIndex].connect(self.table_menu)
            self.ui.backup_btn.clicked.connect(self.ydisk_backup)
            self.ui.hashes_to_file_btn.clicked.connect(self.write_to_json)
            self.ui.check_integrity_btn.clicked.connect(lambda: self.init_table_view(True))

            self.populate()
            self.write_logs("Произведен вход")
        else:
            self.write_logs(f"Был извлечен аутентификатор!")

    def write_to_json(self):
        data_to_write = []
        col_ind = 0
        for row in range(self.table_model.rowCount()):
            name = self.table_model.index(row, col_ind)
            hash = self.table_model.index(row, col_ind+1)
            data = self.table_model.index(row, col_ind+2)
            data_to_write.append({'name':(str(self.table_model.data(name))), 'hash':str(self.table_model.data(hash)), 'date':str(self.table_model.data(data))})
            col_ind = 0

        with open(f"{os.path.dirname(os.path.abspath(__file__))}/hashes/files_hashes.json", "w") as f:
            json.dump(data_to_write, f, indent=4)

    def ydisk_backup(self):
        Variables.disk.upload(f"{os.path.dirname(os.path.abspath(__file__))}/logs/logs.txt", "/logs.txt", overwrite = True)
        Variables.disk.upload(f"{os.path.dirname(os.path.abspath(__file__))}/hashes/files_hashes.json", "/backup_hashes.json", overwrite = True)
        self.write_logs('Было произведено резервное копирование')

    def init_table_view(self, need_to_check_hash = False):
        table_data = []
        with open(f"{os.path.dirname(os.path.abspath(__file__))}/hashes/files_hashes.json", "r+") as f:
            data = json.loads(f.read())
        for el in data:
            if os.path.exists(el['name']):
                table_data.append([*el.values()])
            
        self.table_model = QStandardItemModel(len(table_data), 3)
        for row in range(0, self.table_model.rowCount()):
            need_to_colorize = False
            for column in range(0, self.table_model.columnCount()):
                item = QStandardItem(f"{table_data[row][column]}")
                self.table_model.setItem(row, column, item)
                index = self.table_model.indexFromItem(item)

                if need_to_check_hash and os.path.exists(item.text()):
                    hash_old = table_data[row][column+1]
                    need_to_colorize = self.check_hash(index, [True, hash_old])  
                if need_to_colorize:
                    self.table_model.setData(self.table_model.index(row, column), QBrush(QColor(210, 98, 101, 100)), Qt.BackgroundRole)
        self.table_model.setHorizontalHeaderLabels(['Файл', 'Хэш', 'Дата изменения'])

        self.ui.tableView.setProperty("class", "tview")

        with open(f"{os.path.dirname(os.path.abspath(__file__))}/css/main.css","r") as file:
            self.ui.tableView.setStyleSheet(file.read())

        self.ui.tableView.setModel(self.table_model)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            
    def table_menu(self, index):
        item = self.table_model.itemFromIndex(index)
        selected_item = item.text()
        if os.path.exists(selected_item):
            self.check_hash(index)
        else:
            sibl_ind = index.siblingAtColumn(0)
            self.check_hash(sibl_ind)

    def check_hash(self, index, prev_hash = [False, '']):
        cur_hash = hashlib.sha1(open(self.table_model.itemFromIndex(index).text(), 'rb').read()).hexdigest()
        if not prev_hash[0]:
            sibl_ind = index.siblingAtColumn(1)
            sibl_item = self.table_model.itemFromIndex(sibl_ind)
            old_hash = sibl_item.text()
        else:
            old_hash = prev_hash[1]
        if cur_hash != old_hash:

            self.table_model.setData(index, QBrush(QColor(210, 98, 101, 100)), Qt.BackgroundRole)
            self.table_model.setData(index.siblingAtColumn(1), QBrush(QColor(210, 98, 101, 100)), Qt.BackgroundRole)
            self.table_model.setData(index.siblingAtColumn(2), QBrush(QColor(210, 98, 101, 100)), Qt.BackgroundRole)
            self.write_logs(f"Целостность файла {self.table_model.itemFromIndex(index).text()} была нарушена")
            return True
        elif not prev_hash[0]:
            msg = QMessageBox()
            msg.setWindowTitle("Проверка целостности")
            msg.setText("Целостность не нарушена.")
            msg.setIcon(QMessageBox.Information)
            msg.exec()
            return False

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

                file_to_show = [i.model().filePath(i), i.model().isDir(i)]
                menu = QMenu()
                menu.setProperty("class", "xdmenu")

                with open(f"{os.path.dirname(os.path.abspath(__file__))}/css/main.css","r") as file:
                    menu.setStyleSheet(file.read())

                crypt_option = menu.addAction('Зашифровать файл')
                decrypt_option = menu.addAction('Расшифровать файл')
                
                if file_to_show[1]:
                    crypt_option.setDisabled(True)
                    decrypt_option.setDisabled(True)

                menu.addSeparator()

                exit_option = menu.addAction('Показать в Finder')
                
                menu.addSeparator()

                add_to_hash_db_opt = menu.addAction('Добавить файл в базу хэшей') if not file_to_show[1] else menu.addAction('Добавить директорию в базу хэшей')
                # check_opt = menu.addAction('Проверить целостность файла') if not file_to_show[1] else menu.addAction('Проверить целостность файлов в директории')

                crypt_option.triggered.connect(lambda: self.crypt_file(file_to_show))
                decrypt_option.triggered.connect(lambda: self.decrypt_file(file_to_show))
                exit_option.triggered.connect(lambda: subprocess.call(["open", "-R",file_to_show[0]]))
                
                add_to_hash_db_opt.triggered.connect(lambda: self.add_to_hashes_db(file_to_show))
                # check_opt.triggered.connect(lambda: self.check_hash) 

                menu.exec(self.mapToGlobal(point))
            else:
                self.write_logs(f"Был извлечен аутентификатор!")
        except Exception as e:
            print(e)
    def populate(self):
        if check_flash():
            path = "/Users/nikita/Desktop"
            self.model = QFileSystemModel()
            self.model.setRootPath(path)
            self.ui.treeView.setModel(self.model)
            head = self.ui.treeView.header()
                # self.ui.treeView.header().setSectionResizeMode(QHeaderView.ResizeToContents)
            head.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        else:
            self.write_logs(f"Был извлечен аутентификатор!")

    def crypt_file(self, file_to_show):
        if check_flash():
            if not file_to_show[1]:
                xd = []
                with open(file_to_show[0], 'rb') as f:
                    enc_file1 = f.read()
                xd.append(file_to_show[0])
                enc_file = self.__append_last_bytes(enc_file1)
                des = DES.new(bytes.fromhex(crc64(str(Variables.auth_key_hash))), DES.MODE_ECB)
                encrypted_data = des.encrypt(enc_file)
                with open(f"{file_to_show[0]}.enc", 'wb') as f:
                    f.write(encrypted_data)
                self.write_logs(f"Совершена успешная попытка шифрования файла {file_to_show[0]}")
                
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText("Вы не можете зашифровать папку!")
                msg.setIcon(QMessageBox.Warning)
                msg.exec()
        else:
            self.write_logs(f"Был извлечен аутентификатор!")



    def add_to_hashes_db(self, file):
        f_hashes_old = ''
        f_hashes_new = ''
        file_models = get_model_from_path(file[0])

        add_to_json = []
        with open(f"{os.path.dirname(os.path.abspath(__file__))}/hashes/files_hashes.json", "r+") as f:
            f_hashes_old = json.loads(f.read())
        with open(f"{os.path.dirname(os.path.abspath(__file__))}/hashes/files_hashes.json", "r+") as f:

            f_hashes_new1 = json.loads(f.read())

            f_hashes_new = [el for el in f_hashes_new1 if os.path.exists(el['name'])]

            ind = 0
            for file_model in file_models:
                flag = True
                for file_from_json in f_hashes_old:
                    obj = FilesModel(**file_from_json)

                    if file_model.name == obj.name:
                        if file_model.hash != obj.hash:
                            f_hashes_new[ind]['hash'] = file_model.hash
                            f_hashes_new[ind]['date'] = file_model.date
                        flag = False
                        break
                    
                if flag:
                    f_hashes_new.append(file_model)
                ind+=1
            f.seek(0)
            f.truncate()
            json.dump(f_hashes_new, f, cls=FilesEncoder, indent=4)
        self.write_logs(f"{'Директория' if file[1] else 'Файл'} {file[0]} был{'а' if file[1] else ''} добавлен{'а' if file[1] else ''} в базу хэшей!")
        self.init_table_view(need_to_check_hash=True)

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
                des = DES.new(bytes.fromhex(crc64(str(Variables.auth_key_hash))), DES.MODE_ECB)
                decrypted_data = des.decrypt(dec_file)
                d1 = self.__delete_last_bytes(decrypted_data)
                f_name_to_decode = '.'.join(['.'.join(file_to_show[0][:-4].split('.')[:-1])+'_decoded', file_to_show[0][:-4].split('.')[-1]])
                with open(f"{f_name_to_decode}", 'wb') as f:
                    f.write(d1)
                self.write_logs(f"Совершена успешная попытка расшифрования файла {file_to_show[0]}")

            else:
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText("Вы не можете расшифровать папку!")
                msg.setIcon(QMessageBox.Warning)
                msg.exec()
        else:
            self.write_logs(f"Был извлечен аутентификатор!")

    def write_logs(self, action):
        tm = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.now())
        self.ui.logs_TextEdit.insertPlainText(
            f"{tm}: {action}\n"
        )
    def closeEvent(self, *args, **kwargs):
        super(QMainWindow, self).closeEvent(*args, **kwargs)
        logs = self.ui.logs_TextEdit.toPlainText()
        with open(f'{os.path.dirname(os.path.abspath(__file__))}/logs/logs.txt', 'a') as f:
            f.write(logs)

        Variables.disk.upload(f"{os.path.dirname(os.path.abspath(__file__))}/logs/logs.txt", "/logs.txt", overwrite = True)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    Variables.login_window = EnterKeyWindow()
    Variables.login_window.show()
    app.exec()