import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot

my_list = ["None", "Sepia", "Negative", "Grayscale", "Thumbnail"]

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.my_combo_box = QComboBox()
        self.my_combo_box.addItems(my_list)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.my_combo_box)

        self.setLayout(h_layout)

        self.my_combo_box.currentIndexChanged.connect(self.update_ui)

        self.setWindowTitle("Window layout")

    @pyqtSlot()
    def update_ui(self):
        style = self.my_combo_box.currentText()
        print(style)

app = QApplication(sys.argv)
main = Window()
main.show()
sys.exit(app.exec_())
