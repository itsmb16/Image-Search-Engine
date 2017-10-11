# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ISE.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt

my_list = ["Sepia", "Negative", "Grayscale", "Thumbnail","None"]

class Ui_ImageSearchEngine(object):
    def setupUi(self, ImageSearchEngine):
        ImageSearchEngine.setObjectName("ImageSearchEngine")
        ImageSearchEngine.resize(439, 360)
        
        
        self.centralwidget = QtWidgets.QWidget(ImageSearchEngine)
        self.centralwidget.setObjectName("centralwidget")
        
        #Combobox
        self.Style = QtWidgets.QComboBox(self.centralwidget)
        self.Style.setGeometry(QtCore.QRect(264, 60, 131, 41))
        self.Style.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.Style.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Style.setObjectName("Style")
        
        self.Style.addItems(my_list)
        #self.Style.currentIndexChanged.connect(self.update_style)
        
        #Button
        self.Submit = QtWidgets.QPushButton(self.centralwidget)
        self.Submit.setGeometry(QtCore.QRect(160, 190, 111, 41))
        self.Submit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.Submit.setToolTipDuration(11)
        self.Submit.setObjectName("Submit")
        
        #self.setWindowTitle("submit")
        #my_button = QPushButton("Submit", self)
        #self.Submit.clicked.connect(self.sender())
        #self.show()
        #print("Submitted");

    #  pyqtSlot() function decorator to create a Qt slot
    #@pyqtSlot()
    #def on_click(self):
        #button = self.sender()
        #print("Button Clicked!!!")
        #print(f"{button.text()} clicked!")
        
        #TextBox
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 70, 131, 31))
        self.lineEdit.setObjectName("lineEdit")
        
        #Tag Lebel
        self.Tag = QtWidgets.QLabel(self.centralwidget)
        self.Tag.setGeometry(QtCore.QRect(90, 40, 67, 17))
        self.Tag.setObjectName("Tag")
        
        #label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(290, 30, 67, 17))
        self.label.setObjectName("label")
        ImageSearchEngine.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ImageSearchEngine)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 439, 25))
        self.menubar.setObjectName("menubar")
        self.menuImage_Search_Engine = QtWidgets.QMenu(self.menubar)
        self.menuImage_Search_Engine.setObjectName("menuImage_Search_Engine")
        ImageSearchEngine.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ImageSearchEngine)
        self.statusbar.setObjectName("statusbar")
        ImageSearchEngine.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuImage_Search_Engine.menuAction())

        self.retranslateUi(ImageSearchEngine)
        QtCore.QMetaObject.connectSlotsByName(ImageSearchEngine)

    def retranslateUi(self, ImageSearchEngine):
        _translate = QtCore.QCoreApplication.translate
        ImageSearchEngine.setWindowTitle(_translate("ImageSearchEngine", "Image Search Engine"))
        self.Submit.setText(_translate("ImageSearchEngine", "Submit"))
        self.Tag.setText(_translate("ImageSearchEngine", "Tag"))
        self.label.setText(_translate("ImageSearchEngine", "Style"))
        self.menuImage_Search_Engine.setTitle(_translate("ImageSearchEngine", "Image Search Engine"))
        
    ##@pyqtSlot()
    ##def update_style(self.Style):
    	##my_text = self.Style.currentText()
    	##print(my_text)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ImageSearchEngine = QtWidgets.QMainWindow()
    ui = Ui_ImageSearchEngine()
    ui.setupUi(ImageSearchEngine)
    ImageSearchEngine.show()
    sys.exit(app.exec_())

