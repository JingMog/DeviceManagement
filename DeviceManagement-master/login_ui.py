from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem,QAbstractItemView
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPalette,QBrush,QPixmap,QFont,QPainter,QPainterPath
import sys
import time
import signin

import common_user_ui
import manager_ui
import root_ui


class log_in(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
 
    def init_ui(self):
        self.setObjectName("MainWindow")
        self.resize(617, 408)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.setFont(font)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 531, 61))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 130, 191, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 180, 71, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 230, 71, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.selectbox = QtWidgets.QComboBox(self.centralwidget)
        self.selectbox.addItem("普通用户")
        self.selectbox.addItem("管理员")
        self.selectbox.addItem("超级用户")
        self.selectbox.setObjectName(u"selectbox")
        self.selectbox.setGeometry(QtCore.QRect(300, 130, 151, 41))
        font5 = QFont()
        font5.setFamily(u"Adobe Devanagari")
        font5.setPointSize(18)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.selectbox.setFont(font5)
        
        
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.account = QtWidgets.QLineEdit(self.centralwidget)
        self.account.setGeometry(QtCore.QRect(130, 180, 261, 31))
        self.account.setObjectName("account")

        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(130, 230, 261, 31))
        self.password.setObjectName("password")

        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(250, 290, 121, 51))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.login.setFont(font)
        self.login.setObjectName("login")

        self.signin = QtWidgets.QPushButton(self.centralwidget)
        self.signin.setGeometry(QtCore.QRect(390, 290, 141, 51))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.signin.setFont(font)
        self.signin.setObjectName("signin")
        self.setCentralWidget(self.centralwidget)

        self.label.setText("欢迎使用盒子剧场设备管理系统！")
        self.label_2.setText("请选择工作身份：")
        self.label_3.setText("账号：")
        self.label_4.setText("密码：")
        self.login.setText("点击登陆")
        self.signin.setText("注册普通用户")

        # self.login.clicked.connect(self.message)

        self.setCentralWidget(self.centralwidget)
        self.draw()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.login.clicked.connect(self.message_1)
        self.signin.clicked.connect(self.on_OK_clicked)

    windowList = []
    def message_1(self):
        user_account = self.account.text()
        password = self.password.text()
        user_type = self.selectbox.currentText()
        if(user_type=="普通用户"):
            If_login = signin.signin_common_user(user_account,password)
        elif(user_type == "管理员"):
            If_login = signin.signin_manager(user_account,password)
        else:
            If_login = False
            if(user_account == "root" and password == "root"):
                If_login = True
        if(If_login==False):
            QMessageBox.warning(self,"提示","登陆失败！",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        elif(If_login==True):
            QMessageBox.information(self,"提示","登陆成功!",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        # 展示登录界面
        if If_login == True:
            if(user_type=="普通用户"):
                the_window6 = common_user_ui.MainUi(user_account)
            elif(user_type == "管理员"):
                the_window6 = manager_ui.MainUi(user_account)
            else:
                the_window6 = root_ui.MainUi()
            self.windowList.append(the_window6)   
            self.close()
            the_window6.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "登陆"))

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic201.JPG")))
        self.setPalette(self.palette)

    windowList = []
    def on_OK_clicked(self):
        the_window5 = register()
        self.windowList.append(the_window5)   
        self.close()
        the_window5.show()



class register(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
 
    def init_ui(self):
        self.setObjectName("MainWindow")
        self.resize(615, 348)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 50, 141, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 161, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 141, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.account_re = QtWidgets.QLineEdit(self.centralwidget)
        self.account_re.setGeometry(QtCore.QRect(230, 50, 261, 31))
        self.account_re.setObjectName("account_re")

        self.username_re = QtWidgets.QLineEdit(self.centralwidget)
        self.username_re.setGeometry(QtCore.QRect(230, 100, 261, 31))
        self.username_re.setObjectName("username_re")

        self.password_re = QtWidgets.QLineEdit(self.centralwidget)
        self.password_re.setGeometry(QtCore.QRect(230, 150, 261, 31))
        self.password_re.setObjectName("password_re")

        self.cancel_re = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_re.setGeometry(QtCore.QRect(310, 220, 121, 41))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.cancel_re.setFont(font)
        self.cancel_re.setObjectName("cancel_re")

        self.OK_re = QtWidgets.QPushButton(self.centralwidget)
        self.OK_re.setGeometry(QtCore.QRect(450, 220, 121, 41))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.OK_re.setFont(font)
        self.OK_re.setObjectName("OK_re")

        self.label.setText("请输入账号：")
        self.label_2.setText("请输入手机号：")
        self.label_3.setText("请输入密码：")
        self.cancel_re.setText("取消")
        self.OK_re.setText("确认")

        

        self.setCentralWidget(self.centralwidget)
        self.draw()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.OK_re.pressed.connect(self.on_OK_re_clicked)


    windowList = []
    
    def on_OK_re_clicked(self):
        account = self.account_re.text()
        phone = self.username_re.text()
        password = self.password_re.text()
        # print(account,phone,password)
        IF_sign = signin.register(account,password,phone)
        if(IF_sign==True):
            QMessageBox.information(self,"提示","注册成功!",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        elif(IF_sign==False):
            QMessageBox.warning(self,"提示","注册失败！",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        the_window5 = log_in()
        self.windowList.append(the_window5)   
        self.close()
        the_window5.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "注册"))

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic201.JPG")))
        self.setPalette(self.palette)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = log_in()
    gui.show()
    sys.exit(app.exec_())