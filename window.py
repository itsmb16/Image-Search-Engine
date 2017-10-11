import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
 
class App(QWidget):
 
    def __init__(Window):
        super().__init__()
        Window.title = 'Image Search Engine'
        Window.left = 10
        Window.top = 10
        Window.width = 640
        Window.height = 480
        Window.initUI()
 
    def initUI(Window):
        Window.setWindowTitle(Window.title)
        Window.setGeometry(Window.left, Window.top, Window.width, Window.height)
        Window.show()
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
