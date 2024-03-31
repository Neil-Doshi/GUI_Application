import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt,QSize
import sys

class MainWindow(QMainWindow):
    
    def __init__(self,*args,**kwargs):
        super(MainWindow, self).__init__(*args,**kwargs)
        self.setWindowTitle("My Awesome App")
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        
        self.setCentralWidget(button)
        
    def the_button_was_clicked(self):
        print("Clicked!!!!")


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()