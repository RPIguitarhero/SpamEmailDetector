'''
Author:Kai Kang
Description:GUI element for the email spam detection program
'''

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI,self).__init__()
        self.setGeometry(0,0,900,900)
        self.setWindowTitle("email spam detection")
        self.initUI()
    
    def initUI(self):
        #labels
        self.label1=QtWidgets.QLabel(self)
        self.label1.setText("step1")
        self.label1.move(0,10)
        self.label2=QtWidgets.QLabel(self)
        self.label2.setText("step2")
        self.label2.move(0,50)
        self.label3=QtWidgets.QLabel(self)
        self.label3.setText("step3")
        self.label3.move(0,90)
        self.prompt_label=QtWidgets.QLabel(self)
        self.prompt_label.setText("")
        self.prompt_label.move(500,500)
        self.text_box=QtWidgets.QTextBrowser(self)
        self.text_box.setText("hello world")
        self.text_box.move(100,500)
        #buttons
        self.b1=QtWidgets.QPushButton(self)
        self.b1.setGeometry(50,10,200,20)
        self.b1.setText("load training dataset")
        self.b1.clicked.connect(self.b1_onClick)

    def b1_onClick(self):
        self.text_box.setText("proceed")
        self.update()
        
    def update(self):
        self.text_box.adjustSize()




def window():
    app=QApplication(sys.argv)
    win=MyGUI()
    win.show()
    sys.exit(app.exec_())

window()    

print('done')