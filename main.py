
# TDM HELPER - A SMALL TOOL TO HELP MY WIFE WITH HER DAILY TASKS AT WORK

from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QComboBox, QPushButton
from PyQt5 import uic
import sys
from linearfootage import LinearFootageWindow
from margintool import MarginToolWindow

class MainWindow(QMainWindow):

    def __init__(self):

        super(MainWindow, self).__init__()

        # LINK GUI PIECES
        uic.loadUi('tdmhelpergui.ui', self)
        self.tool_selection_label = self.findChild(QLabel, 'toolselectionlabel')
        self.tool_selection_box = self.findChild(QComboBox, 'toolselectionbox')
        self.ok_button = self.findChild(QPushButton, 'okbutton')
        self.close_button = self.findChild(QPushButton, 'exitbutton')

        # NEW WINDOW REFERENCES
        self.linearfootage = None
        self.margintool = None

        # BUTTON ACTIONS
        self.ok_button.clicked.connect(self.comboboxupdate)
        self.close_button.clicked.connect(self.closeapp)

        # SHOW APP
        self.show()

    # COMBOBOX SELECTION
    def comboboxselection(self):

        self.tool_selection_box.currentTextChanged.connect(self.comboboxupdate)

    # OPEN TOOL WINDOWS BASED ON COMBOBOX SELECTION
    def comboboxupdate(self):

        if self.tool_selection_box.currentText() == 'Linear Footage Calculator':
            self.linearfootage = LinearFootageWindow()
            self.linearfootage.show()
        elif self.tool_selection_box.currentText() == 'Margins Tool':
            self.margintool = MarginToolWindow()
            self.margintool.show()

    # EXIT APPLICATION
    def closeapp(self):

        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    UIMain = MainWindow()
    app.exec_()
