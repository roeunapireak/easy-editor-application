import os
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, 
    QVBoxLayout, QLabel, QPushButton, QListWidget, QFileDialog)


app = QApplication([])

window = QWidget()
window.resize(700, 500)
window.setWindowTitle('Easy Editor')

# interface elements
label_image = QLabel("Image")
botton_folder = QPushButton("Folder")
list_files = QListWidget()

# properties of elements
botton_left = QPushButton("Left")
botton_right = QPushButton("Right")
botton_mirror = QPushButton("Mirror")
botton_sharpness = QPushButton("Sharpness")
botton_bw = QPushButton("B&W")


row1 = QHBoxLayout()
row2 = QHBoxLayout()
column1 = QVBoxLayout()
column2 = QVBoxLayout()

column1.addWidget(botton_folder)
column1.addWidget(list_files)

column2.addWidget(label_image)

row2.addWidget(botton_left)
row2.addWidget(botton_right)
row2.addWidget(botton_mirror)
row2.addWidget(botton_sharpness)
row2.addWidget(botton_bw)

column2.addLayout(row2)

row1.addLayout(column1)
row1.addLayout(column2)

window.setLayout(row1)


window.show()

folder = ''

def chooseFolder():
    global folder
    folder = QFileDialog.getExistingDirectory()

def filter(files, extensions):
    result = list()
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result

def showFilenameList():
    image_extensions = ['.jpg','.jpeg', '.png', '.gif', '.bmp']
    chooseFolder()
    file_names = filter(files=os.listdir(folder), extensions=image_extensions)

    list_files.clear()
    
    for file in file_names:
        list_files.addItem(file)

botton_folder.clicked.connect(showFilenameList)

from PIL import Image
from PyQt5.QtGui import QPixmap # screen-optimised

# needs a Qt.KeepAspectRatio constant to resize while maintaining proportions
from PyQt5.QtCore import Qt

class ImageProcessor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified/"

    # function to upload an image from the work folder
    def loadImage(self, dir, filename):
        '''When loading, remember the path and file name'''
        self.dir = dir
        self.filename = filename
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)

    # function to show a preview of the selected image
    def showImage(self, path):
        label_image.hide()

        '''Using the full path of the file, create a QPixmap object 
        specifically for displaying graphics in the UI.'''
        pixmapimage = QPixmap(path)

        # Find out the dimensions of the field for placing the image.
        w, h = label_image.width(), label_image.height()

        # Adapting the image according to the dimensions of the field.
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)

        # Posting the image in the label_image widget.
        label_image.setPixmap(pixmapimage)

        label_image.show()

workimage = ImageProcessor()

def showChosenImage():
   if list_files.currentRow() >= 0:
       filename = list_files.currentItem().text()
       workimage.loadImage(folder, filename)
       image_path = os.path.join(workimage.dir, workimage.filename)
       workimage.showImage(image_path)

list_files.currentRowChanged.connect(showChosenImage)

app.exec_()