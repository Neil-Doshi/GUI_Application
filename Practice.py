# import PyQt5
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import Qt,QSize
# import sys

# class MainWindow(QMainWindow):
    
#     def __init__(self,*args,**kwargs):
#         super(MainWindow, self).__init__(*args,**kwargs)
#         self.setWindowTitle("My Awesome App")
#         button = QPushButton("Press Me!")
#         button.setCheckable(True)
#         button.clicked.connect(self.the_button_was_clicked)
        
#         self.setCentralWidget(button)
        
#     def the_button_was_clicked(self):
#         print("Clicked!!!!")


# app = QApplication(sys.argv)

# window = MainWindow()
# window.show()
# app.exec_()


x = [(0, 0, 0), (0, 0, 1), (3, 0, 0), (3, 0, 1), (3, 0, 2), (3, 0, 3), (3, 0, 4), (3, 0, 5), (6, 0, 0), (6, 2, 0), (7, 0, 0), (7, 1, 0), (8, 0, 0), (8, 1, 0), (9,0, 0), (9, 1, 0), (10, 0, 0), (10, 1, 0), (11, 0, 0), (11, 1, 0), (12, 0, 0), (12, 1, 0), (13, 0, 0), (13, 1, 0), (14, 0, 0), (14, 1, 0), (15, 0, 0), (15, 1, 0), (16, 0, 0), (16, 1, 0), (17, 0, 0), (17, 1, 0), (0, 0, 0), (0, 0, 1), (3, 0, 0), (3, 0, 1), (3, 0, 2), (3, 0, 3), (3, 0, 4), (3, 0, 5), (5, 0, 0), (5, 1, 0), (6, 0, 0), (6, 1, 0), (7, 0, 0), (7, 1, 0), (8, 0, 0), (8, 1, 0), (8, 1, 1), (0, 0, 0)]
j = []
# for i in range(len(x) - 1):
#     if x[i] > x[i + 1]:
#         j.append(i)

j += [i for i in range(len(x) - 1) if x[i] > x[i + 1]]

print(j)