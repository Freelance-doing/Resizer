import sys
from PySide6 import QtCore, QtWidgets, QtGui
from os import listdir, remove, mkdir
from os.path import exists
from PIL import Image
import resources


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.square = False
        self.converter = False

        self.text = QtWidgets.QLabel()
        self.text.setStyleSheet(
            "font-family: times; "
            "font-size: 30px;"
        )
        self.text.setText("Welcome to the universal image resizer!")
        self.text.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)

        self.main_button = QtWidgets.QPushButton("RESIZE")
        self.main_button.setStyleSheet(
            "background-color: RED; "
            "font-family: times; "
            "font-size: 20px;"
        )

        self.pbr = QtWidgets.QProgressBar(self)
        self.pbr.setStyleSheet(
            "font-family: times; "
            "font-size: 20px;"
        )
        self.pbr.setAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.pbr.setValue(0)

        self.timer = QtCore.QTimer()

        self.list_edit_1 = QtWidgets.QLineEdit()
        self.list_edit_1.setStyleSheet(
            "font-family: times; "
            "font-size: 15px;"
        )
        self.label_1 = QtWidgets.QLabel("Width: ")
        self.label_1.setStyleSheet(
            "font-family: times; "
            "font-size: 15px;"
        )
        self.edit_1 = QtWidgets.QLabel("0")
        self.edit_1.setStyleSheet(
            "font-family: times; "
            "font-size: 15px;"
        )
        self.enter_1 = QtWidgets.QPushButton("Enter")
        self.enter_1.setStyleSheet(
            "font-family: times; "
            "font-size: 15px;"
        )
        self.list_edit_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        self.list_edit_2 = QtWidgets.QLineEdit()
        self.list_edit_2.setStyleSheet(
            "font-family: times; "
            "font-size: 15px;"
        )
        self.label_2 = QtWidgets.QLabel("Height: ")
        self.label_2.setStyleSheet(
            "font-family: times; "
            "font-size: 15px;"
        )
        self.edit_2 = QtWidgets.QLabel("0")
        self.edit_2.setStyleSheet(
            "font-family: times; "
            "font-size: 15px;"
        )
        self.enter_2 = QtWidgets.QPushButton("Enter")
        self.enter_2.setStyleSheet(
            "font-family: times; "
            "font-size: 15px;"
        )
        self.list_edit_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        self.button = QtWidgets.QPushButton("Choose the directory where your images are: ")
        self.button.setStyleSheet(
            "font-family: times; "
            "font-size: 15px;"
        )
        self.last_button = QtWidgets.QPushButton("Choose the directory where you want to move the resized result: ")
        self.last_button.setStyleSheet(
            "font-family: times; "
            "font-size: 15px;"
        )

        self.label_dir_1 = QtWidgets.QLabel("None")
        self.label_dir_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)
        self.label_dir_1.setStyleSheet(
            "font-family: times; "
            "font-size: 15px;"
        )
        self.label_dir_2 = QtWidgets.QLabel("None")
        self.label_dir_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)
        self.label_dir_2.setStyleSheet(
            "font-family: times; "
            "font-size: 15px;"
        )

        self.base_path = QtWidgets.QFileDialog()
        self.last_path = QtWidgets.QFileDialog()

        self.btn = QtWidgets.QCheckBox("Squared")
        self.btn.setStyleSheet(
            "font-family: times; "
            "font-size: 15px;"
        )
        self.cb = QtWidgets.QCheckBox("PNG to JPG")
        self.cb.setStyleSheet(
            "font-family: times; "
            "font-size: 15px;"
        )

        self.layout_label = QtWidgets.QVBoxLayout(self)
        self.layout_label.addWidget(self.text)

        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.setSpacing(10)
        self.layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify)

        self.layout_checkboxes = QtWidgets.QHBoxLayout(self)
        self.layout_checkboxes.setSpacing(100)
        self.layout_checkboxes.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom)

        self.layout_main = QtWidgets.QVBoxLayout(self)
        self.layout_main.setAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter)

        self.layout_main.addWidget(self.main_button)
        self.layout_main.addWidget(self.pbr)

        self.layout_le_1 = QtWidgets.QHBoxLayout(self)
        self.layout_le_1.setSpacing(10)
        self.layout_le_1.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify)

        self.layout_le_1.addWidget(self.label_1)
        self.layout_le_1.addWidget(self.edit_1)
        self.layout_le_1.addWidget(self.list_edit_1)
        self.layout_le_1.addWidget(self.enter_1)

        self.layout_le_2 = QtWidgets.QHBoxLayout(self)
        self.layout_le_2.setSpacing(10)
        self.layout_le_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignJustify)

        self.layout_le_2.addWidget(self.label_2)
        self.layout_le_2.addWidget(self.edit_2)
        self.layout_le_2.addWidget(self.list_edit_2)
        self.layout_le_2.addWidget(self.enter_2)

        self.layout_checkboxes.addWidget(self.label_dir_1)
        self.layout_checkboxes.addWidget(self.btn)
        self.layout_checkboxes.addWidget(self.cb)
        self.layout_checkboxes.addWidget(self.label_dir_2)

        self.layout.addWidget(self.button)
        self.layout.addWidget(self.last_button)

        self.layout_label.addLayout(self.layout_main)
        self.layout_label.addLayout(self.layout_le_1)
        self.layout_label.addLayout(self.layout_le_2)
        self.layout_label.addLayout(self.layout)
        self.layout_label.addLayout(self.layout_checkboxes)

        self.setLayout(self.layout_label)

        self.button.clicked.connect(self.file_browser)
        self.last_button.clicked.connect(self.file_browser)
        self.btn.stateChanged.connect(self.check)
        self.enter_1.clicked.connect(self.get_width)
        self.enter_2.clicked.connect(self.get_height)
        self.main_button.clicked.connect(self.resize_img)
        self.timer.timeout.connect(self.resize_img)

    @QtCore.Slot()
    def resize_img(self):
        if isinstance(self.base_path, str) and isinstance(self.last_path, str) \
                and self.edit_1.text().isdigit() and self.edit_2.text().isdigit():
            if self.cb.isChecked():
                for i in listdir(f'{self.base_path}'):
                    if ".png" in i:
                        im1 = Image.open(f'{self.base_path}' + f'{i}')
                        rgb_im = im1.convert('RGB')
                        rgb_im.save(f'{self.base_path}' + f'{i.replace(".png", ".jpg")}')
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Attention!")
                msg.setText("Firstly, we converted your png images to jpg images, now you can press the button RESIZE!")
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.exec_()
                self.cb.click()
            elif len(listdir(self.base_path)) == 0:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Attention!")
                msg.setText("Your base path is empty, make sure you've chosen the correct one, then click the button RESIZE!")
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.exec_()
            else:
                temp = list()
                self.pbr.setValue(0)
                count = 0
                width_desired = int(self.edit_1.text())
                height_desired = int(self.edit_2.text())
                for i in listdir(f'{self.base_path}'):
                    count += 1
                    temp.append(i)
                self.timer.start(1000)
                value = self.pbr.value()
                for i in range(len(temp)):
                    if self.square:
                        image = Image.open(f'{self.base_path}/{temp[i]}', 'r')
                        width = image.width
                        height = image.height
                        big_side = width if width > height else height
                        other_side = int(big_side * 1)
                        background = Image.new('RGB', (other_side, big_side), (255, 255, 255, 255))
                        offset = (int(round(((big_side - width) / 2), 0)), int(round(((big_side - height) / 2), 0)))
                        background.paste(image, offset)
                        background.save(f'{self.last_path}/{temp[i]}')
                        image = Image.open(f'{self.last_path}/{temp[i]}', 'r')
                        new_image = image.resize((width_desired, height_desired))
                        image.close()
                        remove(f'{self.base_path}/{temp[i]}')
                        new_image.save(f'{self.last_path}/{temp[i]}')
                    else:
                        image = Image.open(f'{self.base_path}/{temp[i]}', 'r')
                        new_image = image.resize((width_desired, height_desired))
                        image.close()
                        remove(f'{self.base_path}/{temp[i]}')
                        new_image.save(f'{self.last_path}/{temp[i]}')
                    value += 100 / count
                    self.pbr.setValue(round(value))
                self.timer.stop()

    @QtCore.Slot()
    def get_width(self):
        if self.list_edit_1.text().isdigit():
            self.edit_1.setText(self.list_edit_1.text())
            self.list_edit_1.clear()
        else:
            self.list_edit_1.clear()

    @QtCore.Slot()
    def get_height(self):
        if self.list_edit_2.text().isdigit():
            self.edit_2.setText(self.list_edit_2.text())
            self.list_edit_2.clear()
        else:
            self.list_edit_2.clear()

    @QtCore.Slot()
    def file_browser(self):
        sender = self.sender()
        if sender.text == self.button.text:
            self.base_path = QtWidgets.QFileDialog.getExistingDirectory(self, QtCore.QFile.tr("Open Directory"),
                                                                        "/",
                                                                        QtWidgets.QFileDialog.ShowDirsOnly
                                                                        | QtWidgets.QFileDialog.DontResolveSymlinks)
            self.label_dir_1.setText(f'{self.base_path}')
        elif sender.text == self.last_button.text:
            self.last_path = QtWidgets.QFileDialog.getExistingDirectory(self, QtCore.QFile.tr("Open Directory"),
                                                                        "/",
                                                                        QtWidgets.QFileDialog.ShowDirsOnly
                                                                        | QtWidgets.QFileDialog.DontResolveSymlinks)
            self.label_dir_2.setText(f'{self.last_path}')

    @QtCore.Slot()
    def check(self):
        if self.btn.isChecked():
            self.square = True
            if self.edit_1.text() > self.edit_2.text():
                self.edit_2.setText(self.edit_1.text())
            else:
                self.edit_1.setText(self.edit_2.text())
        elif not self.btn.isChecked():
            self.square = False


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    app.setWindowIcon(QtGui.QIcon(":/icons/icon.ico"))

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()
    widget.setWindowTitle('Resizer')

    sys.exit(app.exec())
