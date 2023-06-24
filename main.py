from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QLineEdit,QLabel,QRadioButton
import sys
from ftp import ftpConnect

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple FTP")
        self.setFixedSize(QtCore.QSize(720,480))

        self.connectButton = QPushButton("Connect",self)
        self.connectButton.move(450,30)
        #self.connectButton.clicked.connect(sendLoginData())
    
        #host input
        self.hostInput = QLineEdit(self).move(10,30)
        self.hostLabel = QLabel("Host", self).move(15,5)
        #user input
        self.userInput = QLineEdit(self).move(120,30)
        self.userLabel = QLabel("User", self).move(125,5)
        #password input
        self.passwordInput = QLineEdit(self)
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.move(230,30)
        self.passwordLabel = QLabel("Password", self).move(235,5)
        #port input
        self.portInput = QLineEdit(self).move(10,100)
        self.portLabel = QLabel("Port",self).move(15,75)
        #radio input
        self.passiveRadio = QRadioButton(self).move(120,90)
        self.passiveLabel = QLabel("Passive",self).move(140, 87)
        self.activeRadio = QRadioButton(self).move(120,110)
        self.activeLabel = QLabel("Active",self).move(140, 107)

        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
