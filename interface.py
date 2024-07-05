#create the Easy Editor photo editor here!
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, 
    QVBoxLayout, QLabel, QPushButton, QListWidget)

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

app.exec_()