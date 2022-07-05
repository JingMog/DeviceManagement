from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem,QAbstractItemView
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPalette,QBrush,QPixmap,QFont,QPainter,QPainterPath
import sys
import qtawesome
import time
import common_user

class MainUi(QtWidgets.QMainWindow):
    user_id = ''
    def __init__(self,user_id):
        self.user_id = user_id
        super().__init__()
        self.init_ui()
 
    def init_ui(self):
        self.setFixedSize(1200,800)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
 
        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout) # 设置左侧部件布局为网格
 
        self.right_widget = QtWidgets.QWidget() # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout) # 设置右侧部件布局为网格
 
        self.main_layout.addWidget(self.left_widget,0,0,12,2) # 左侧部件在第0行第0列，占12行2列
        self.main_layout.addWidget(self.right_widget,0,2,12,10) # 右侧部件在第0行第3列，占12行10列
        self.setCentralWidget(self.main_widget) # 设置窗口主部件
 
        # self.left_close = QtWidgets.QPushButton("") # 关闭按钮
        self.left_close =QtWidgets.QPushButton(qtawesome.icon('fa.times',color='white'),"")
        # self.left_visit = QtWidgets.QPushButton("") # 空白按钮
        self.left_visit = QtWidgets.QPushButton(qtawesome.icon('fa.repeat',color='white'),"")
        # self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮
        self.left_mini =QtWidgets.QPushButton(qtawesome.icon('fa.arrows-alt',color='white'),"")
        self.left_close.clicked.connect(self.close_window) #关联
 
        self.left_label_1 = QtWidgets.QPushButton("设备管理")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("维修管理")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("数据管理")
        self.left_label_3.setObjectName('left_label')
 
        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.gear',color='white'),"可用设备")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.edit',color='white'),"设备借用")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.arrow-circle-right',color='white'),"归还设备")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.gears',color='white'),"申请维修")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.file-text-o',color='white'),"已修记录")
        self.left_button_5.setObjectName('left_button')
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.hourglass-half',color='white'),"维修数据")
        self.left_button_6.setObjectName('left_button')
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.list-ol',color='white'),"我的数据")
        self.left_button_7.setObjectName('left_button')
        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.map',color='white'),"个人信息")
        self.left_button_8.setObjectName('left_button')
        self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.paper-plane',color='white'),"意见反馈")
        self.left_button_9.setObjectName('left_button')
        self.left_xxx = QtWidgets.QPushButton(" ")
 
        self.left_layout.addWidget(self.left_mini, 0, 0,1,1)
        self.left_layout.addWidget(self.left_close, 0, 2,1,1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
 
        self.left_layout.addWidget(self.left_label_1,1,0,1,3)
        self.left_layout.addWidget(self.left_button_1, 2, 0,1,3)
        self.left_layout.addWidget(self.left_button_2, 3, 0,1,3)
        self.left_layout.addWidget(self.left_button_3, 4, 0,1,3)
        self.left_layout.addWidget(self.left_label_2, 5, 0,1,3)
        self.left_layout.addWidget(self.left_button_4, 6, 0,1,3)
        self.left_layout.addWidget(self.left_button_5, 7, 0,1,3)
        self.left_layout.addWidget(self.left_button_6, 8, 0,1,3)
        self.left_layout.addWidget(self.left_label_3, 9, 0,1,3)
        self.left_layout.addWidget(self.left_button_7, 10, 0,1,3)
        self.left_layout.addWidget(self.left_button_8, 11, 0,1,3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)
 
        self.right_bar_widget = QtWidgets.QWidget() # 右侧顶部搜索框部件
        self.right_bar_layout = QtWidgets.QGridLayout() # 右侧顶部搜索框网格布局
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.search_icon = QtWidgets.QLabel(chr(0xf002) + ' '+'搜索  ')
        self.search_icon.setFont(qtawesome.font('fa', 16))
        self.right_bar_widget_search_input = QtWidgets.QLineEdit()
        self.right_bar_widget_search_input.setPlaceholderText("输入设备ID、设备名或设备类型")
 
        self.right_bar_layout.addWidget(self.search_icon,0,0,1,1)
        self.right_bar_layout.addWidget(self.right_bar_widget_search_input,0,1,1,8)

        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 2, 9)
  
        self.right_recommend_widget = QtWidgets.QWidget() # 推荐封面部件
        self.right_recommend_layout = QtWidgets.QGridLayout() # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.recommend_button_1 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.recommend_button_1.setFont(font)
        self.recommend_button_1.setText("设备1") # 设置按钮文本
        self.recommend_button_1.setIcon(QtGui.QIcon('pics/anna.JPG')) # 设置按钮图标
        self.recommend_button_1.setIconSize(QtCore.QSize(150,150)) # 设置图标大小
        self.recommend_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon) # 设置按钮形式为上图下文
 
        self.recommend_button_2 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.recommend_button_2.setFont(font)
        self.recommend_button_2.setText("设备2")
        self.recommend_button_2.setIcon(QtGui.QIcon('pics/elsa.JPG'))
        self.recommend_button_2.setIconSize(QtCore.QSize(150, 150))
        self.recommend_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.recommend_button_3 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.recommend_button_3.setFont(font)
        self.recommend_button_3.setText("设备3")
        self.recommend_button_3.setIcon(QtGui.QIcon('pics/anna.JPG'))
        self.recommend_button_3.setIconSize(QtCore.QSize(150, 150))
        self.recommend_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.recommend_button_4 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.recommend_button_4.setFont(font)
        self.recommend_button_4.setText("设备4")
        self.recommend_button_4.setIcon(QtGui.QIcon('pics/elsa.JPG'))
        self.recommend_button_4.setIconSize(QtCore.QSize(150, 150))
        self.recommend_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.recommend_button_5 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.recommend_button_5.setFont(font)
        self.recommend_button_5.setText("设备5")
        self.recommend_button_5.setIcon(QtGui.QIcon('pics/anna.JPG'))
        self.recommend_button_5.setIconSize(QtCore.QSize(150, 150))
        self.recommend_button_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.recommend_button_6 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.recommend_button_6.setFont(font)
        self.recommend_button_6.setText("设备6") # 设置按钮文本
        self.recommend_button_6.setIcon(QtGui.QIcon('pics/anna.JPG')) # 设置按钮图标
        self.recommend_button_6.setIconSize(QtCore.QSize(150,150)) # 设置图标大小
        self.recommend_button_6.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon) # 设置按钮形式为上图下文
 
        self.recommend_button_7 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.recommend_button_7.setFont(font)
        self.recommend_button_7.setText("设备7")
        self.recommend_button_7.setIcon(QtGui.QIcon('pics/elsa.JPG'))
        self.recommend_button_7.setIconSize(QtCore.QSize(150, 150))
        self.recommend_button_7.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.recommend_button_8 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.recommend_button_8.setFont(font)
        self.recommend_button_8.setText("设备8")
        self.recommend_button_8.setIcon(QtGui.QIcon('pics/anna.JPG'))
        self.recommend_button_8.setIconSize(QtCore.QSize(150, 150))
        self.recommend_button_8.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.recommend_button_9 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.recommend_button_9.setFont(font)
        self.recommend_button_9.setText("设备9")
        self.recommend_button_9.setIcon(QtGui.QIcon('pics/elsa.JPG'))
        self.recommend_button_9.setIconSize(QtCore.QSize(150, 150))
        self.recommend_button_9.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.recommend_button_10 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.recommend_button_10.setFont(font)
        self.recommend_button_10.setText("设备10")
        self.recommend_button_10.setIcon(QtGui.QIcon('pics/anna.JPG'))
        self.recommend_button_10.setIconSize(QtCore.QSize(150, 150))
        self.recommend_button_10.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.right_recommend_layout.addWidget(self.recommend_button_1,0,0)
        self.right_recommend_layout.addWidget(self.recommend_button_2,0,1)
        self.right_recommend_layout.addWidget(self.recommend_button_3, 0, 2)
        self.right_recommend_layout.addWidget(self.recommend_button_4, 0, 3)
        self.right_recommend_layout.addWidget(self.recommend_button_5, 0, 4)
        self.right_recommend_layout.addWidget(self.recommend_button_6,1,0)
        self.right_recommend_layout.addWidget(self.recommend_button_7,1,1)
        self.right_recommend_layout.addWidget(self.recommend_button_8, 1, 2)
        self.right_recommend_layout.addWidget(self.recommend_button_9, 1, 3)
        self.right_recommend_layout.addWidget(self.recommend_button_10, 1, 4)
 
        self.right_layout.addWidget(self.right_recommend_widget, 0, 0, 0, 9)

        self.left_close.setFixedSize(16,16) # 设置关闭按钮的大小
        self.left_visit.setFixedSize(16, 16)  # 设置按钮大小
        self.left_mini.setFixedSize(16, 16) # 设置最小化按钮大小
 
        self.left_close.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet('''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet('''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
 
        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
            QWidget#left_widget{
            background:rgb(108, 152, 204);
            border-top:1px solid white;
            border-bottom:1px solid white;
            border-left:1px solid white;
            border-top-left-radius:10px;
            border-bottom-left-radius:10px;
        }
        ''')
 
        self.right_bar_widget_search_input.setStyleSheet(
        '''QLineEdit{
                border:1px solid gray;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
        }''')
 
        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')
        self.right_recommend_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')
 
        self.setWindowOpacity(1) # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置窗口背景透明
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) # 隐藏边框

        self.main_layout.setSpacing(0)

        self.left_button_1.clicked.connect(self.on_left_button_1_clicked)
        self.left_button_2.clicked.connect(self.on_left_button_2_clicked)
        self.left_button_3.clicked.connect(self.on_left_button_3_clicked)
        self.left_button_4.clicked.connect(self.on_left_button_4_clicked)
        self.left_button_5.clicked.connect(self.on_left_button_5_clicked)
        self.left_button_6.clicked.connect(self.on_left_button_6_clicked)
        self.left_button_7.clicked.connect(self.on_left_button_7_clicked)
        self.left_button_8.clicked.connect(self.on_left_button_8_clicked)
 
    # 无边框的拖动
    def mouseMoveEvent(self, e: QtGui.QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)
 
    def mousePressEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = True
            self._startPos = QtCore.QPoint(e.x(), e.y())
 
    def mouseReleaseEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    windowList = []
    def on_left_button_1_clicked(self):
        the_window1 = table_unused_UI(self.user_id)
        self.windowList.append(the_window1)   
        ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window1.show()
 
    def on_left_button_2_clicked(self):
        the_window2 = equipment_borrow_UI(self.user_id)
        self.windowList.append(the_window2)   
        self.close()
        the_window2.show()

    def on_left_button_3_clicked(self):
        the_window2 = return_eqip_table(self.user_id)
        self.windowList.append(the_window2)   
        self.close()
        the_window2.show()

    def on_left_button_4_clicked(self):
        the_window3 = repair_request(self.user_id)
        self.windowList.append(the_window3)   
        self.close()
        the_window3.show()

    def on_left_button_5_clicked(self):
        the_window5 = repair_finished_data_UI(self.user_id)
        self.windowList.append(the_window5)   
        self.close()
        the_window5.show()

    def on_left_button_6_clicked(self):
        the_window3 = repair_data_UI(self.user_id)
        self.windowList.append(the_window3)   
        self.close()
        the_window3.show()

    def on_left_button_7_clicked(self):
        the_window7 = my_data_UI(self.user_id)
        self.windowList.append(the_window7)   
        self.close()
        the_window7.show()

    def on_left_button_8_clicked(self):
        print("button_8_clicked")
        print(self.user_id)
        the_window8 = user_information(self.user_id)
        self.windowList.append(the_window8)
        self.close()
        the_window8.show()

    # 关闭按钮动作函数
    def close_window(self):
        self.close()
 







 
class table_unused_UI(QtWidgets.QMainWindow):
    user_id = ''
    common_user_x = ''

    def __init__(self,user_id):
        self.user_id = user_id
        self.common_user_x = common_user.common_user(user_id)
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setObjectName("table_unused")
        self.setFixedSize(1200,800)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.table_unused_tablewidget = QtWidgets.QTableWidget(self.centralwidget)
        self.table_unused_tablewidget.setGeometry(QtCore.QRect(90, 40, 1000, 700))
        self.table_unused_tablewidget.setObjectName("tableView")
        self.table_unused_tablewidget.setColumnCount(5)
        self.table_unused_tablewidget.setHorizontalHeaderLabels(['设备名', '设备ID', '设备类型','故障','状态'])
        self.table_unused_tablewidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table_unused_tablewidget.horizontalHeader().setMinimumHeight(50)
        self.table_unused_tablewidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(158, 201, 209);font:24pt '华文仿宋';color: black;};")
        self.table_unused_tablewidget.verticalHeader().setVisible(False)
        self.table_unused_tablewidget.setFont(QFont("STFangsong", 18))
        self.table_unused_tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.get_unused_device()

        self.setCentralWidget(self.centralwidget)
        self.draw()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def get_unused_device(self):
        useabledevice = self.common_user_x.sql_all_useabledevice()
        i=-1
        for row_item in useabledevice:
            i=i+1
            self.table_unused_tablewidget.setRowCount(i+1)
            self.table_unused_tablewidget.setItem(i,0,QTableWidgetItem(str(row_item[1])))
            self.table_unused_tablewidget.setItem(i,1,QTableWidgetItem(str(row_item[0])))
            self.table_unused_tablewidget.setItem(i,2,QTableWidgetItem(str(row_item[2])))
            self.table_unused_tablewidget.setItem(i,3,QTableWidgetItem(str(row_item[3])))
            self.table_unused_tablewidget.setItem(i,4,QTableWidgetItem(str(row_item[4])))
            for j in range(0,5):
                self.table_unused_tablewidget.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_unused_tablewidget.setRowHeight(i,40)# 设置table表格第4行的高度
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "可用设备"))

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic1.JPG")))
        self.setPalette(self.palette)

    windowList = []
    def closeEvent(self, event):
        the_window3 = MainUi(self.user_id)
        self.windowList.append(the_window3)  ##注：没有这句，是不打开另一个主界面的！
        the_window3.show()
        event.accept()





class equipment_borrow_UI(QtWidgets.QMainWindow):
    user_id = ''
    common_user_x = ''

    def __init__(self,user_id):
        self.user_id = user_id
        self.common_user_x = common_user.common_user(user_id)
        super().__init__()
        self.init_ui()

    def init_ui(self):   
        self.setObjectName("equipment_borrow")
        self.setFixedSize(650,350)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 20, 600, 300))
        self.tableView.setObjectName("tableView")
        self.setCentralWidget(self.centralwidget)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 70, 201, 51))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 140, 201, 51))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lend_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lend_name.setGeometry(QtCore.QRect(280, 80, 221, 31))
        self.lend_name.setObjectName("lend_name")
        self.lend_time = QtWidgets.QLineEdit(self.centralwidget)
        self.lend_time.setGeometry(QtCore.QRect(280, 150, 221, 31))
        self.lend_time.setObjectName("lend_time")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(350, 220, 111, 41))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.OK = QtWidgets.QPushButton(self.centralwidget)
        self.OK.setGeometry(QtCore.QRect(480, 220, 111, 41))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.OK.setFont(font)
        self.OK.setObjectName("OK")

        self.label.setText("请输入待借设备ID:")
        self.label_2.setText("请输入借用时长:")
        self.cancel.setText("取消")
        self.OK.setText("确认")

        self.OK.clicked.connect(self.message_1)

        self.draw()
        self.tableView.setStyleSheet("#tableView{background:transparent}")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def message_1(self):
        device_id = self.lend_name.text() 
        lend_time = self.lend_time.text()
        If_useable =True
        If_useable = self.common_user_x.apply_use(device_id,lend_time)
        if(If_useable==True):
            the_window1 = borrow_successful(self.common_user_x.get_apply_use_result(), self)
            self.windowList.append(the_window1)   
            self.close()
            the_window1.show()

        elif(If_useable==False):
            QMessageBox.warning(self,"提示","该设备已借出!",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
            
            

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic1.JPG")))
        self.setPalette(self.palette)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "设备借用"))

    windowList = []
    def closeEvent(self, event):
        the_window = MainUi(self.user_id)
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        the_window.show()
        event.accept()

    # @QtCore.pyqtSlot()
    # def on_OK_clicked(self):
    #     print("我进来了")
        

    
        

        



class borrow_successful(QDialog):
    apply_use_info = []
    def __init__(self,apply_use_info,parent=None,):
        super(borrow_successful, self).__init__(parent)
        self.apply_use_info = apply_use_info
        self.init_ui()

    def init_ui(self):   
        self.setObjectName("borrow_successful")
        self.setFixedSize(650,450)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 121, 51))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 141, 51))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.user_name = QtWidgets.QLabel(self.centralwidget)
        self.user_name.setGeometry(QtCore.QRect(190, 90, 221, 31))
        self.user_name.setObjectName("user_name")
        self.user_name.setFont(font)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 141, 51))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self._user_id = QtWidgets.QLabel(self.centralwidget)
        self._user_id.setGeometry(QtCore.QRect(190, 140, 221, 31))
        self._user_id.setObjectName("user_id")
        self._user_id.setFont(font)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 180, 141, 51))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.equip_name = QtWidgets.QLabel(self.centralwidget)
        self.equip_name.setGeometry(QtCore.QRect(190, 190, 221, 31))
        self.equip_name.setObjectName("equip_name")
        self.equip_name.setFont(font)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 230, 141, 51))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.equip_id = QtWidgets.QLabel(self.centralwidget)
        self.equip_id.setGeometry(QtCore.QRect(190, 240, 221, 31))
        self.equip_id.setObjectName("equip_id")
        self.equip_id.setFont(font)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 280, 141, 51))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lend_time = QtWidgets.QLabel(self.centralwidget)
        self.lend_time.setGeometry(QtCore.QRect(190, 290, 221, 31))
        self.lend_time.setObjectName("lend_time")
        self.lend_time.setFont(font)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 330, 141, 51))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.return_time = QtWidgets.QLabel(self.centralwidget)
        self.return_time.setGeometry(QtCore.QRect(190, 340, 221, 31))
        self.return_time.setObjectName("return_time")
        self.return_time.setFont(font)

        self.label.setText("借用成功！")
        self.label_2.setText("借用人姓名：")
        self.label_3.setText("借用人工号：")
        self.label_4.setText("借用设备名：")
        self.label_5.setText("借用设备ID：")
        self.label_6.setText("借用时间：")
        self.label_7.setText("归还时间：")
        

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.draw()

        self.get_borrow_information()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "借用成功"))

    def get_borrow_information(self):
       nowtime = time.time()
       nowtime_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(nowtime))
       self.user_name.setText(self.apply_use_info[0])
       self._user_id.setText(self.apply_use_info[1])
       self.equip_name.setText(self.apply_use_info[2])
       self.equip_id.setText(self.apply_use_info[3])
       self.lend_time.setText(str(nowtime_str))
       self.return_time.setText(self.apply_use_info[4])

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic1.JPG")))
        self.setPalette(self.palette)







class return_eqip_table(QtWidgets.QMainWindow):
    user_id = ''
    common_user_x = ''

    def __init__(self,user_id):
        self.user_id = user_id
        self.common_user_x = common_user.common_user(user_id)
        super().__init__()
        self.init_ui()

    def init_ui(self):  
        self.setObjectName("return_equip")
        self.setFixedSize(1200,700)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.table_data_Widget = QtWidgets.QTableWidget(self.centralwidget)
        self.table_data_Widget.setGeometry(QtCore.QRect(50, 40, 1100, 500))
        self.table_data_Widget.setObjectName("tableWidget")

        self.table_data_Widget.setColumnCount(5)
        self.table_data_Widget.setHorizontalHeaderLabels(['借用记录号', '设备名', '设备ID','借用日期','预计归还时间'])
        self.table_data_Widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table_data_Widget.horizontalHeader().setMinimumHeight(50)
        self.table_data_Widget.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(158, 201, 209);font:24pt '华文仿宋';color: black;};")
        self.table_data_Widget.verticalHeader().setVisible(False)
        self.table_data_Widget.setFont(QFont("STFangsong", 18))
        self.table_data_Widget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.OK = QtWidgets.QPushButton(self.centralwidget)
        self.OK.setGeometry(QtCore.QRect(1000, 570, 111, 41))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.OK.setFont(font)
        self.OK.setObjectName("OK")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(850, 570, 111, 41))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.cancel.setText("取消")
        self.OK.setText("归还")

        self.OK.clicked.connect(self.message_1)

        self.get_used_data()
        self.draw()

        self.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    windowList = []
    def closeEvent(self, event):
        the_window3 = MainUi(self.user_id)
        self.windowList.append(the_window3)  ##注：没有这句，是不打开另一个主界面的！
        the_window3.show()
        event.accept()

    def get_used_data(self):
        used_data = self.common_user_x.get_unreturn_device()
        i=-1
        for row_item in used_data:
            i=i+1
            self.table_data_Widget.setRowCount(i+1)
            self.table_data_Widget.setItem(i,0,QTableWidgetItem(str(row_item[0])))
            self.table_data_Widget.setItem(i,1,QTableWidgetItem(str(row_item[1])))
            self.table_data_Widget.setItem(i,2,QTableWidgetItem(str(row_item[2])))
            self.table_data_Widget.setItem(i,3,QTableWidgetItem(str(row_item[3])))
            self.table_data_Widget.setItem(i,4,QTableWidgetItem(str(row_item[4])))
            for j in range(0,5):
                self.table_data_Widget.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_data_Widget.setRowHeight(i,40)# 设置table表格第4行的高度

    windowList = []
    def message_1(self):
        the_window1 = return_equip(self.user_id)
        self.windowList.append(the_window1)   
        ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window1.show()

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic1.JPG")))
        self.setPalette(self.palette)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "维修申请"))





class return_equip(QtWidgets.QMainWindow):
    user_id = ''
    common_user_x = ''

    def __init__(self,user_id):
        self.user_id = user_id
        self.common_user_x = common_user.common_user(user_id)
        super().__init__()
        self.init_ui()

    def init_ui(self):  
        self.setObjectName("MainWindow")
        self.setFixedSize(780,360)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 50, 231, 51))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.borrow_id = QtWidgets.QLineEdit(self.centralwidget)
        self.borrow_id.setGeometry(QtCore.QRect(330, 60, 341, 41))
        self.borrow_id.setObjectName("repari_eq_name")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 261, 51))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.equip_state = QtWidgets.QLineEdit(self.centralwidget)
        self.equip_state.setGeometry(QtCore.QRect(330, 130, 341, 41))
        self.equip_state.setObjectName("repair_eq_id")
        self.OK = QtWidgets.QPushButton(self.centralwidget)
        self.OK.setGeometry(QtCore.QRect(580, 220, 121, 41))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.OK.setFont(font)
        self.OK.setObjectName("OK")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(450, 220, 121, 41))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.cancel.raise_()
        self.label.raise_()
        # self.repari_eq_name.raise_()
        self.label_2.raise_()
        # self.repair_eq_id.raise_()
        self.OK.raise_()
        self.setCentralWidget(self.centralwidget)
        self.OK.clicked.connect(self.message_1)
        self.label.setText("请输入借用编号：")
        self.label_2.setText("设备状态为良好或损坏：")
        self.OK.setText("确认")
        self.cancel.setText("取消")
        self.draw()

    def message_1(self):
        borrow_id = self.borrow_id.text() 
        return_state = self.equip_state.text()
        If_return =True
        If_return = self.common_user_x.return_device(borrow_id,return_state)
        if(If_return==False):
            QMessageBox.warning(self,"提示","归还失败,未借用此设备!",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        else:
            QMessageBox.information(self,"提示","归还成功!",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic1.JPG")))
        self.setPalette(self.palette)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "归还设备"))

    windowList = []
    def closeEvent(self, event):
        the_window = return_eqip_table()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        the_window.show()
        event.accept()


class repair_request(QtWidgets.QMainWindow):
    user_id = ''
    common_user_x = ''

    def __init__(self,user_id):
        self.user_id = user_id
        self.common_user_x = common_user.common_user(user_id)
        super().__init__()
        self.init_ui()

    def init_ui(self):  
        self.setObjectName("repair_request")
        self.setFixedSize(660,300)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 20, 450, 250))
        self.tableView.setObjectName("tableView")
        self.setCentralWidget(self.centralwidget)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 70, 231, 51))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lend_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lend_name.setGeometry(QtCore.QRect(300, 80, 221, 31))
        self.lend_name.setObjectName("lend_name")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(360, 130, 111, 41))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.OK = QtWidgets.QPushButton(self.centralwidget)
        self.OK.setGeometry(QtCore.QRect(490, 130, 111, 41))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.OK.setFont(font)
        self.OK.setObjectName("OK")

        self.label.setText("请输入待维修设备ID:")
        self.cancel.setText("取消")
        self.OK.setText("确认")

        self.OK.clicked.connect(self.message_1)

        self.draw()
        self.tableView.setStyleSheet("#tableView{background:transparent}")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def message_1(self):
        device_id = self.lend_name.text() 
        If_repair =True
        If_repair = self.common_user_x.apply_repair(device_id)
        if(If_repair==False):
            QMessageBox.warning(self,"提示","该设备使用正常!",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        else:
            # QMessageBox.information(self,"提示","借用成功!",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
           self.OK.clicked.connect(self.on_OK_clicked)
           self.dialog = borrow_successful(self.common_user_x.get_apply_use_result(), self) # 实例化一个 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "维修申请"))

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic1.JPG")))
        self.setPalette(self.palette)

    @QtCore.pyqtSlot()
    def on_OK_clicked(self):
        print("创建之前",self.common_user_x.get_apply_use_result())
        the_window1 = request_successful(self.common_user_x.get_apply_repair_result())
        self.windowList.append(the_window1)   
        self.close()
        the_window1.show()

    windowList = []
    def closeEvent(self, event):
        the_window = MainUi(self.user_id)
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        the_window.show()
        event.accept()






#已维修的申请
class repair_finished_data_UI(QtWidgets.QMainWindow):
    user_id = ''
    common_user_x = ''

    def __init__(self,user_id):
        self.user_id = user_id
        self.common_user_x = common_user.common_user(user_id)
        super().__init__()
        self.init_ui()

    def init_ui(self):  
        self.setObjectName("repair_finished_data")
        self.setFixedSize(1200,600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.table_data_Widget = QtWidgets.QTableWidget(self.centralwidget)
        self.table_data_Widget.setGeometry(QtCore.QRect(50, 40, 1100, 500))
        self.table_data_Widget.setObjectName("tableWidget")
        self.table_data_Widget.setColumnCount(0)
        self.table_data_Widget.setRowCount(0)

        self.table_data_Widget.setColumnCount(6)
        self.table_data_Widget.setHorizontalHeaderLabels(['维修记录号', '设备ID', '设备名','维修时间','维修结果','维修人'])
        self.table_data_Widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table_data_Widget.horizontalHeader().setMinimumHeight(50)
        self.table_data_Widget.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(158, 201, 209);font:24pt '华文仿宋';color: black;};")
        self.table_data_Widget.verticalHeader().setVisible(False)
        self.table_data_Widget.setFont(QFont("STFangsong", 18))
        self.table_data_Widget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.get_used_data()
        self.draw()

        self.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    windowList = []
    def closeEvent(self, event):
        the_window3 = MainUi(self.user_id)
        self.windowList.append(the_window3)  ##注：没有这句，是不打开另一个主界面的！
        the_window3.show()
        event.accept()

    def get_used_data(self):
        used_data = self.common_user_x.sql_all_repair_record()
        i=-1
        for row_item in used_data:
            i=i+1
            self.table_data_Widget.setRowCount(i+1)
            self.table_data_Widget.setItem(i,0,QTableWidgetItem(str(row_item[0])))
            self.table_data_Widget.setItem(i,1,QTableWidgetItem(str(row_item[2])))
            self.table_data_Widget.setItem(i,2,QTableWidgetItem(str(row_item[1])))
            self.table_data_Widget.setItem(i,3,QTableWidgetItem(str(row_item[3])))
            self.table_data_Widget.setItem(i,4,QTableWidgetItem(str(row_item[4])))
            self.table_data_Widget.setItem(i,5,QTableWidgetItem(str(row_item[5])))
            for j in range(0,6):
                self.table_data_Widget.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_data_Widget.setRowHeight(i,40)# 设置table表格第4行的高度

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic1.JPG")))
        self.setPalette(self.palette)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "维修申请"))







class request_successful(QDialog):
    apply_use_info = []
    def __init__(self,apply_use_info,parent=None,):
        super(request_successful, self).__init__(parent)
        self.apply_use_info = apply_use_info
        self.init_ui()

    def init_ui(self):   
        self.setObjectName("request_successful")
        self.setFixedSize(650,450)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 121, 51))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 141, 51))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.user_name = QtWidgets.QLabel(self.centralwidget)
        self.user_name.setGeometry(QtCore.QRect(190, 90, 221, 31))
        self.user_name.setObjectName("user_name")
        self.user_name.setFont(font)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 141, 51))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self._user_id = QtWidgets.QLabel(self.centralwidget)
        self._user_id.setGeometry(QtCore.QRect(190, 140, 221, 31))
        self._user_id.setObjectName("user_id")
        self._user_id.setFont(font)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 180, 141, 51))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.repair_id = QtWidgets.QLabel(self.centralwidget)
        self.repair_id.setGeometry(QtCore.QRect(190, 190, 221, 31))
        self.repair_id.setObjectName("equip_name")
        self.repair_id.setFont(font)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 230, 141, 51))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.repair_device_id = QtWidgets.QLabel(self.centralwidget)
        self.repair_device_id.setGeometry(QtCore.QRect(190, 240, 221, 31))
        self.repair_device_id.setObjectName("equip_id")
        self.repair_device_id.setFont(font)


        self.label.setText("申请成功！")
        self.label_2.setText("申请人姓名：")
        self.label_3.setText("申请人工号：")
        self.label_4.setText("维修编号：")
        self.label_5.setText("维修设备ID：")
        
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.draw()

        self.get_repair_information()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "维修申请成功"))

    def get_repair_information(self):
       self.user_name.setText(self.apply_use_info[0])
       self._user_id.setText(self.apply_use_info[1])
       self.repair_id.setText(self.apply_use_info[2])
       self.repair_device_id.setText(self.apply_use_info[3])

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic1.JPG")))
        self.setPalette(self.palette)




#所有的维修申请,维修了和没维修的都有
class repair_data_UI(QtWidgets.QMainWindow):
    user_id = ''
    common_user_x = ''

    def __init__(self,user_id):
        self.user_id = user_id
        self.common_user_x = common_user.common_user(user_id)
        super().__init__()
        self.init_ui()

    def init_ui(self):  
        self.setObjectName("repair_finished_data")
        self.setFixedSize(1200,600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.table_data_Widget = QtWidgets.QTableWidget(self.centralwidget)
        self.table_data_Widget.setGeometry(QtCore.QRect(50, 40, 1100, 500))
        self.table_data_Widget.setObjectName("tableWidget")
        self.table_data_Widget.setColumnCount(0)
        self.table_data_Widget.setRowCount(0)

        self.table_data_Widget.setColumnCount(6)
        self.table_data_Widget.setHorizontalHeaderLabels(['维修记录号', '设备ID', '设备名','维修时间','维修结果','维修人'])
        self.table_data_Widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table_data_Widget.horizontalHeader().setMinimumHeight(50)
        self.table_data_Widget.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(158, 201, 209);font:24pt '华文仿宋';color: black;};")
        self.table_data_Widget.verticalHeader().setVisible(False)
        self.table_data_Widget.setFont(QFont("STFangsong", 18))
        self.table_data_Widget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.get_used_data()
        self.draw()

        self.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    windowList = []
    def closeEvent(self, event):
        the_window3 = MainUi(self.user_id)
        self.windowList.append(the_window3)  ##注：没有这句，是不打开另一个主界面的！
        the_window3.show()
        event.accept()

    def get_used_data(self):
        used_data = self.common_user_x.sql_all_repair_apply()
        i=-1
        for row_item in used_data:
            i=i+1
            self.table_data_Widget.setRowCount(i+1)
            self.table_data_Widget.setItem(i,0,QTableWidgetItem(str(row_item[0])))
            self.table_data_Widget.setItem(i,1,QTableWidgetItem(str(row_item[2])))
            self.table_data_Widget.setItem(i,2,QTableWidgetItem(str(row_item[1])))
            self.table_data_Widget.setItem(i,3,QTableWidgetItem(str(row_item[3])))
            self.table_data_Widget.setItem(i,4,QTableWidgetItem(str(row_item[4])))
            self.table_data_Widget.setItem(i,5,QTableWidgetItem(str(row_item[5])))
            for j in range(0,6):
                self.table_data_Widget.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_data_Widget.setRowHeight(i,40)# 设置table表格第4行的高度

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic1.JPG")))
        self.setPalette(self.palette)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "维修申请"))




class my_data_UI(QtWidgets.QMainWindow):
    user_id = ''
    common_user_x = ''

    def __init__(self,user_id):
        self.user_id = user_id
        self.common_user_x = common_user.common_user(user_id)
        super().__init__()
        self.init_ui()

    def init_ui(self):  
        self.setObjectName("my_data")
        self.setFixedSize(1500,700)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.table_data_Widget = QtWidgets.QTableWidget(self.centralwidget)
        self.table_data_Widget.setGeometry(QtCore.QRect(50, 40, 1400, 600))
        self.table_data_Widget.setObjectName("tableWidget")
        self.table_data_Widget.setColumnCount(0)
        self.table_data_Widget.setRowCount(0)

        self.table_data_Widget.setColumnCount(9)
        self.table_data_Widget.setHorizontalHeaderLabels(['借用记录号', '设备ID', '设备名','借用时间','使用时间','归还时间','归还状态','是否超时','批准人'])
        self.table_data_Widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table_data_Widget.horizontalHeader().setMinimumHeight(50)
        self.table_data_Widget.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(158, 201, 209);font:24pt '华文仿宋';color: black;};")
        self.table_data_Widget.verticalHeader().setVisible(False)
        self.table_data_Widget.setFont(QFont("STFangsong", 18))
        self.table_data_Widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.table_data_Widget.setStyleSheet("QWidget{border-top-left-radius:15px;border-top-right-radius:5px;}")
        # self.table_data_Widget.setStyleSheet('''
        #     QTableWidget#tableWidget{
        #         border-top-right-radius:10px;
        #         border-bottom-right-radius:10px;
        #     }
        # ''')

        self.get_used_data()
        self.draw()

        self.setCentralWidget(self.centralwidget)
        

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    windowList = []
    def closeEvent(self, event):
        the_window3 = MainUi(self.user_id)
        self.windowList.append(the_window3)  ##注：没有这句，是不打开另一个主界面的！
        the_window3.show()
        event.accept()

    def get_used_data(self):
        used_data = self.common_user_x.sql_use_record()
        i=-1
        for row_item in used_data:
            i=i+1
            self.table_data_Widget.setRowCount(i+1)
            self.table_data_Widget.setItem(i,0,QTableWidgetItem(str(row_item[0])))
            self.table_data_Widget.setItem(i,1,QTableWidgetItem(str(row_item[1])))
            self.table_data_Widget.setItem(i,2,QTableWidgetItem(str(row_item[2])))
            self.table_data_Widget.setItem(i,3,QTableWidgetItem(str(row_item[3])))
            self.table_data_Widget.setItem(i,4,QTableWidgetItem(str(row_item[4])))
            self.table_data_Widget.setItem(i,5,QTableWidgetItem(str(row_item[5])))
            self.table_data_Widget.setItem(i,6,QTableWidgetItem(str(row_item[6])))
            self.table_data_Widget.setItem(i,7,QTableWidgetItem(str(row_item[7])))
            self.table_data_Widget.setItem(i,8,QTableWidgetItem(str(row_item[8])))
            for j in range(0,9):
                self.table_data_Widget.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_data_Widget.setRowHeight(i,40)# 设置table表格第4行的高度

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic1.JPG")))
        self.setPalette(self.palette)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "我的数据"))







class user_information(QtWidgets.QMainWindow):
    use_id = ''
    common_user_x = ''

    def __init__(self,use_id):
        self.use_id = use_id
        print("======个人信息===")
        print(use_id)
        self.common_user_x = common_user.common_user(use_id)
        super().__init__()
        self.init_ui()

    def init_ui(self):  
        self.setObjectName("MainWindow")
        self.setFixedSize(550,500)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(60, 50, 431, 401))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")

        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(140, 17, 121, 121))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(80, 145, 81, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(80, 180, 91, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(80, 220, 111, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(80, 260, 131, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(80, 300, 141, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.integrity = QtWidgets.QLabel(self.groupBox)
        self.integrity.setGeometry(QtCore.QRect(230, 300, 161, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.integrity.setFont(font)
        self.integrity.setObjectName("integrity")
        self.power = QtWidgets.QLabel(self.groupBox)
        self.power.setGeometry(QtCore.QRect(230, 260, 161, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.power.setFont(font)
        self.power.setObjectName("power")
        self.department = QtWidgets.QLabel(self.groupBox)
        self.department.setGeometry(QtCore.QRect(230, 220, 161, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.department.setFont(font)
        self.department.setObjectName("department")
        self.user_id = QtWidgets.QLabel(self.groupBox)
        self.user_id.setGeometry(QtCore.QRect(230, 180, 161, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.user_id.setFont(font)
        self.user_id.setObjectName("user_id")
        self.user_name = QtWidgets.QLabel(self.groupBox)
        self.user_name.setGeometry(QtCore.QRect(230, 150, 161, 21))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.user_name.setFont(font)
        self.user_name.setObjectName("user_name")
        self.setCentralWidget(self.centralwidget)


        self.label.setText("TextLabel")
        self.label_2.setText("用户名：")
        self.label_3.setText("用户ID：")
        self.label_4.setText("所属部门：")
        self.label_5.setText("用户权限值：")
        self.label_6.setText("用户诚信值：")

        self.get_user_information()
        self.draw()
        self._plain_pic()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        

    def get_user_information(self):
        information = self.common_user_x.get_person_information()
        self.integrity.setText(str(information[4]))
        self.power.setText(str(information[3]))
        self.department.setText(str(information[2]))
        self.user_id.setText(str(information[1]))
        self.user_name.setText(str(information[0]))

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic1.JPG")))
        self.setPalette(self.palette)

    def _plain_pic(self):
        pixmapa = QPixmap("pics/pic11.png")
        pixmap = QPixmap(121,121)
        pixmap.fill(QtCore.Qt.transparent)
        painter = QPainter(pixmap)
        painter.begin(self) #要将绘制过程用begin(self)和end()包起来
        painter.setRenderHints(QPainter.Antialiasing |QPainter.SmoothPixmapTransform)       #一个是平滑，一个是缩放保持比例
        path = QPainterPath()
        path.addEllipse(0, 0, 121, 121);    #绘制椭圆
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, 121, 121, pixmapa)
        painter.end()
        self.label.setPixmap(pixmap)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "个人信息"))

    windowList = []
    def closeEvent(self, event):
        the_window = MainUi(self.use_id)
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        the_window.show()
        event.accept()





def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi("useperson001")
    gui.show()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()