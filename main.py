from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QLineEdit,QLabel,QRadioButton,QDialog
from PyQt5.QtGui import QIntValidator
import sys
from ftp import ftpConnect

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #main windows properties
        self.setWindowTitle("Simple FTP")
        self.setFixedSize(QtCore.QSize(720,480))

        #connect button
        self.connectButton = QPushButton("Connect",self)
        self.connectButton.move(450,30)
        self.connectButton.clicked.connect(self.sendLoginData)
        #host input
        self.hostInput = QLineEdit(self)
        self.hostInput.move(10,30)
        self.hostLabel = QLabel("Host", self)
        self.hostLabel.move(15,5)
        #user input
        self.userInput = QLineEdit(self)
        self.userInput.move(120,30)
        self.userLabel = QLabel("User", self)
        self.userLabel.move(125,5)
        #password input
        self.passwordInput = QLineEdit(self)
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.move(230,30)
        self.passwordLabel = QLabel("Password", self)
        self.passwordLabel.move(235,5)
        #port input
        self.portInput = QLineEdit(self)
        self.portInput.move(10,100)
        portRange = QIntValidator()
        portRange.setRange(0, 65535)
        self.portInput.setValidator(portRange)
        self.portLabel = QLabel("Port",self)
        self.portLabel.move(15,75)
        #radio input
        self.passiveRadio = QRadioButton(self)
        self.passiveRadio.move(120,90)
        self.passiveRadio.setChecked(True)
        self.passiveLabel = QLabel("Passive",self)
        self.passiveLabel.move(140, 87)
        self.activeRadio = QRadioButton(self)
        self.activeRadio.move(120,110)
        self.activeLabel = QLabel("Active",self)
        self.activeLabel.move(140, 107)

        #ftp connection
    def sendLoginData(self):
        host = self.hostInput.text()
        user = self.userInput.text()
        password = self.passwordInput.text()
        port = self.portInput.text()
        radioMode = self.passiveRadio.isChecked()
        ftpConnect(host,user,password,port,radioMode)


        
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
