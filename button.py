import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot

class submitButton(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("submit")
        my_button = QPushButton("Submit", self)
        my_button.clicked.connect(self.on_click)
        self.show()

    #  pyqtSlot() function decorator to create a Qt slot
    @pyqtSlot()
    def on_click(self):
        button = self.sender()
        print("Button Clicked!!!")
        #print(f"{button.text()} clicked!")


my_app = QApplication(sys.argv)
a_window = submitButton()
sys.exit(my_app.exec_())
