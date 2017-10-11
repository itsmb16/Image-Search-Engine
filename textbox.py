import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QComboBox, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot


from image_information import *
from PIL import Image

my_list = ["None", "Sepia", "Negative", "Grayscale", "Thumbnail"]

#Negative
def negative ( picture ):
    new_list = []
    for p in picture . getdata ():
        temp = ( 255 - p [ 0 ], 255 - p [ 1 ], 255 - p [ 2 ])
        new_list . append ( temp )
    picture . putdata ( new_list )
    picture . save ( "images/negative.png" )
    
#Grayscale
def grayscale ( picture ):
    new_list = []
    for p in picture . getdata ():
        new_red = int ( p [ 0 ] * 0.299 )
        new_green = int ( p [ 1 ] * 0.587 )
        new_blue = int ( p [ 2 ] * 0.114 )
        luminance = new_red + new_green + new_blue
        temp = ( luminance , luminance , luminance )
        new_list . append ( temp )
    picture . putdata ( new_list )
    picture . save ( "images/grayscale.png" )
    

#Sepia

def grayscale_sepia ( picture ):
    new_list = []
    for p in picture . getdata ():
        new_red = int ( p [ 0 ] * 0.299 )
        new_green = int ( p [ 1 ] * 0.587 )
        new_blue = int ( p [ 2 ] * 0.114 )
        luminance = new_red + new_green + new_blue
        temp = ( luminance , luminance , luminance )
        new_list . append ( temp )
    return new_list
 
def sepia ( picture ):
    #print picture
    width , height = picture . size
    #print width,height
    mode = picture . mode
    temp_list = []
    pic_data = grayscale_sepia ( picture )
    for p in pic_data:
        #tint shadows
        if p [ 0 ] < 63 :
            red_val = int ( p [ 0 ] * 1.1 )
            green_val = p [ 1 ]
            blue_val = int ( p [ 2 ] * 0.9 )
        # tint midtones
        if p [ 0 ] > 62 and p [ 0 ] < 192 :
            red_val = int ( p [ 0 ] * 1.15 )
            green_val = p [ 1 ]
            blue_val = int ( p [ 2 ] * 0.85 )
        # tint highlights
        if p [ 0 ] > 191 :
            red_val = int ( p [ 0 ] * 1.08 )
            if red_val > 255 :
                red_val = 255
            green_val = p [ 1 ]
            blue_val = int ( p [ 2 ] * 0.5 )
        temp_list . append (( red_val , green_val , blue_val ))
    picture . putdata ( temp_list )
    picture . save ( "images/sepia.png" )

#Thumbnail
def thumbnail (picture):
    #pic = Image . open ( "images/"+picture+".jpg" )
    # destination image
    canvas = Image . new ( "RGB" , ( 640 , 480 ), "white" )
    target_x = 0
    for source_x in range ( 0 , picture . width , 2 ):
        target_y = 0
        for source_y in range ( 0 , picture . height , 2 ):
            color = picture . getpixel (( source_x , source_y ))
            canvas . putpixel (( target_x , target_y ), color )
            target_y += 1
        target_x += 1
    canvas . save ( "images/thumbnail.png" )



 
class App(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.title = 'Tag'
        self.left = 10
        self.top = 10
        self.width = 600
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)
        
        #CREATE COMBOBOX
        #self.Style = QtWidgets.QComboBox(self.centralwidget)
        self.Style = QComboBox()
        self.Style.setGeometry(QtCore.QRect(264, 60, 131, 41))
        self.Style.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.Style.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Style.setObjectName("Style")
        self.Style.addItems(my_list)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.Style)

        #self.setLayout(h_layout)

        #self.my_combo_box.currentIndexChanged.connect(self.update_ui)

        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20,80)
 
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()
 
    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        style = self.Style.currentText()
        #print(style)        
        QMessageBox.question(self, 'Message', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")
        l=len(image_info);
        #print l
        tag=textboxValue
        i=0
        while l:
        	l1=len(image_info[i]['tags'])
        	j=0
        	while l1:
        		if tag==image_info[i]['tags'][j]:
        			img_id=image_info[i]['id']
        			print (image_info[i]['id'])
        			break
        		j=j+1
        		l1=l1-1
        	im = Image . open ( "images/"+img_id+".jpg" )
        	pixel_list = list ( im . getdata ())
        	if style=="Sepia":
        		sepia(im)
        	elif style=="Negative":
        		negative(im)
        	elif style=="Thumbnail":
        		thumbnail(im)
        	elif style=="Grayscale":
        		grayscale(im)
        	i=i+1
        	l=l-1
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
