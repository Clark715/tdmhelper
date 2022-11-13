
# SQUARE FOOTAGE CALCULATOR

from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QWidget, QMessageBox
from PyQt5 import uic

class LinearFootageWindow(QWidget):

    def __init__(self):

        super(LinearFootageWindow, self).__init__()

        # LINK GUI PIECES
        uic.loadUi('linearfootageui.ui', self)
        self.length_label = self.findChild(QLabel, 'lengthlabel')
        self.width_label = self.findChild(QLabel, 'widthlabel')
        self.length_user = self.findChild(QLineEdit, 'lengthuser')
        self.width_user = self.findChild(QLineEdit, 'widthuser')
        self.go_button = self.findChild(QPushButton, 'gobutton')

        # BUTTON ACTIONS
        self.go_button.clicked.connect(self.sqfoot)


    def sqfoot(self):

        length = self.length_user.text()
        width = self.width_user.text()

        try:
            result = float(length) * float(width)
            QMessageBox.about(self, 'Result ', str(result) + ' Linear Footage')
        except:
            QMessageBox.about(self, 'Oops!', 'Please use numbers only!')



