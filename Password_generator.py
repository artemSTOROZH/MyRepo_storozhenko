import sys
import cmath
import random
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
import pyperclip

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.setWindowTitle("Password Generator")
    window.setWindowIcon(QtGui.QIcon("icon.jpg"))
    label_1 = QtWidgets.QLabel("Number_of_characters")
    button = QtWidgets.QPushButton("Get password")
    spinbox = QtWidgets.QSpinBox()
    spinbox.setMinimum(8)
    spinbox.setMaximum(30)
    text = QtWidgets.QLineEdit()
    grid = QtWidgets.QGridLayout()
    window.setLayout(grid)
    grid.addWidget(label_1, 0, 0, Qt.AlignVCenter)
    grid.addWidget(spinbox, 0, 1, Qt.AlignVCenter)
    spinbox.setAlignment(Qt.AlignHCenter)
    grid.addWidget(button, 1, 0, Qt.AlignVCenter)
    grid.addWidget(text, 1, 1, Qt.AlignVCenter)
    text.setAlignment(Qt.AlignHCenter)


    def generatePassword(self):
        password = ""
        for i in range(1, spinbox.value()):
            k = round(random.random() * 91) + 35
            char = chr(k)
            password += char
        text.setText(password)
        pyperclip.copy(password)

    button.clicked.connect(generatePassword)
    window.resize(360, 100)
    window.show()
    sys.exit(app.exec())