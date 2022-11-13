
# MARGAIN TOOL

from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QWidget, QMessageBox
from PyQt5 import uic

class MarginToolWindow(QWidget):

    def __init__(self):

        super(MarginToolWindow, self).__init__()

        # LINK GUI PIECES
        uic.loadUi('marginui.ui', self)
        self.price_label = self.findChild(QLabel, 'pricelabel')
        self.price_input = self.findChild(QLineEdit, 'priceuser')
        self.margin_label = self.findChild(QLabel, 'marginlabel')
        self.margin_user = self.findChild(QLineEdit, 'marginuser')
        self.go_button = self.findChild(QPushButton, 'gobutton')

        self.go_button.clicked.connect(self.margin)

    def margin(self):

        try:
            margin_percent = float(self.margin_user.text()) / 100
            result = float(self.price_input.text()) / (1 - margin_percent)
            QMessageBox.about(self, 'Result', '${:0.2f}'.format(result))
        except:
            QMessageBox.about(self, 'Oops!', 'Please use numbers only! Do not include money signs.')
