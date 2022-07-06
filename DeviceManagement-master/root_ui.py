from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem,QPushButton,QAbstractItemView
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPalette,QBrush,QPixmap,QFont,QPainter,QPainterPath
import sys
import qtawesome
import time
import root

class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
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
 
        self.left_label_1 = QtWidgets.QPushButton("管理统计")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("设备供应")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("数据管理")
        self.left_label_3.setObjectName('left_label')
 
        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.tasks',color='white'),"请求批准")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.wrench',color='white'),"设备动态")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.edit',color='white'),"人员管理")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.bar-chart',color='white'),"厂商信息")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.exchange',color='white'),"供应信息")
        self.left_button_5.setObjectName('left_button')
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.folder-open',color='white'),"设备情况")
        self.left_button_6.setObjectName('left_button')
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.list-ol',color='white'),"添加设备")
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
        # self.recommend_button_1.setIcon(QtGui.QIcon('/Users/magica/Desktop/panda1.jpg')) # 设置按钮图标
        self.recommend_button_1.setIcon(QtGui.QIcon('pics/pice.JPG')) # 设置按钮图标
        self.recommend_button_1.setIconSize(QtCore.QSize(150,150)) # 设置图标大小
        self.recommend_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon) # 设置按钮形式为上图下文
 
        self.recommend_button_2 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.recommend_button_2.setFont(font)
        self.recommend_button_2.setText("设备2")
        self.recommend_button_2.setIcon(QtGui.QIcon('pics/picq.JPG'))
        self.recommend_button_2.setIconSize(QtCore.QSize(150, 150))
        self.recommend_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.recommend_button_3 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.recommend_button_3.setFont(font)
        self.recommend_button_3.setText("设备3")
        self.recommend_button_3.setIcon(QtGui.QIcon('pics/picu.JPG'))
        self.recommend_button_3.setIconSize(QtCore.QSize(150, 150))
        self.recommend_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.recommend_button_4 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.recommend_button_4.setFont(font)
        self.recommend_button_4.setText("设备4")
        self.recommend_button_4.setIcon(QtGui.QIcon('pics/pici.JPG'))
        self.recommend_button_4.setIconSize(QtCore.QSize(150, 150))
        self.recommend_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.recommend_button_5 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.recommend_button_5.setFont(font)
        self.recommend_button_5.setText("设备5")
        self.recommend_button_5.setIcon(QtGui.QIcon('pics/picp.JPG'))
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
        self.recommend_button_6.setIcon(QtGui.QIcon('pics/picm.JPG')) # 设置按钮图标
        self.recommend_button_6.setIconSize(QtCore.QSize(150,150)) # 设置图标大小
        self.recommend_button_6.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon) # 设置按钮形式为上图下文
 
        self.recommend_button_7 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.recommend_button_7.setFont(font)
        self.recommend_button_7.setText("设备7")
        self.recommend_button_7.setIcon(QtGui.QIcon('pics/pice.JPG'))
        self.recommend_button_7.setIconSize(QtCore.QSize(150, 150))
        self.recommend_button_7.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.recommend_button_8 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.recommend_button_8.setFont(font)
        self.recommend_button_8.setText("设备8")
        self.recommend_button_8.setIcon(QtGui.QIcon('pics/picn.JPG'))
        self.recommend_button_8.setIconSize(QtCore.QSize(150, 150))
        self.recommend_button_8.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.recommend_button_9 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.recommend_button_9.setFont(font)
        self.recommend_button_9.setText("设备9")
        self.recommend_button_9.setIcon(QtGui.QIcon('pics/pict.JPG'))
        self.recommend_button_9.setIconSize(QtCore.QSize(150, 150))
        self.recommend_button_9.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.recommend_button_10 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.recommend_button_10.setFont(font)
        self.recommend_button_10.setText("设备10")
        self.recommend_button_10.setIcon(QtGui.QIcon('pics/pics.JPG'))
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
            background:rgb(27, 76, 148);
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
        the_window1 = request_statisfied()
        self.windowList.append(the_window1)   
        ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window1.show()
 
    def on_left_button_2_clicked(self):
        the_window2 = equipment_states()
        self.windowList.append(the_window2)   
        self.close()
        the_window2.show()

    def on_left_button_3_clicked(self):
        the_window2 = people_management()
        self.windowList.append(the_window2)   
        self.close()
        the_window2.show()

    def on_left_button_4_clicked(self):
        the_window3 = supplier_information()
        self.windowList.append(the_window3)   
        self.close()
        the_window3.show()

    def on_left_button_5_clicked(self):
        the_window5 = supplier_equip_info()
        self.windowList.append(the_window5)   
        self.close()
        the_window5.show()

    def on_left_button_6_clicked(self):
        the_window3 = equip_information()
        self.windowList.append(the_window3)   
        self.close()
        the_window3.show()

    def on_left_button_7_clicked(self):
        the_window7 = add_equipment()
        self.windowList.append(the_window7)   
        self.close()
        the_window7.show()

    def on_left_button_8_clicked(self):
        the_window8 = user_information()
        self.windowList.append(the_window8)   
        self.close()
        the_window8.show()

    # 关闭按钮动作函数
    def close_window(self):
        self.close()




class request_statisfied(QtWidgets.QMainWindow):
    root = root.root()

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setObjectName("request_statisfied")
        self.setFixedSize(800,500)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.table_unused_tablewidget = QtWidgets.QTableWidget(self.centralwidget)
        self.table_unused_tablewidget.setGeometry(QtCore.QRect(90, 50, 600, 380))
        self.table_unused_tablewidget.setObjectName("tableView")
        self.table_unused_tablewidget.setColumnCount(3)
        self.table_unused_tablewidget.setHorizontalHeaderLabels(['管理员姓名', '管理员ID', '批准设备数'])
        self.table_unused_tablewidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table_unused_tablewidget.horizontalHeader().setMinimumHeight(50)
        self.table_unused_tablewidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(96, 163, 230);font:24pt '华文仿宋';color: black;};")
        self.table_unused_tablewidget.verticalHeader().setVisible(False)
        self.table_unused_tablewidget.setFont(QFont("STFangsong", 18))
        self.table_unused_tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.get_data()

        self.setCentralWidget(self.centralwidget)
        self.draw()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def get_data(self):
        useabledevice = self.root.manager_statistics()
        i=-1
        for row_item in useabledevice:
            i=i+1
            self.table_unused_tablewidget.setRowCount(i+1)
            self.table_unused_tablewidget.setItem(i,0,QTableWidgetItem(str(row_item[0])))
            self.table_unused_tablewidget.setItem(i,1,QTableWidgetItem(str(row_item[1])))
            self.table_unused_tablewidget.setItem(i,2,QTableWidgetItem(str(row_item[2])))
            for j in range(0,3):
                self.table_unused_tablewidget.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_unused_tablewidget.setRowHeight(i,40)# 设置table表格第4行的高度
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "请求批准"))

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic101.JPG")))
        self.setPalette(self.palette)

    windowList = []
    def closeEvent(self, event):
        the_window3 = MainUi()
        self.windowList.append(the_window3)  ##注：没有这句，是不打开另一个主界面的！
        the_window3.show()
        event.accept()







class equipment_states(QtWidgets.QMainWindow):
    root = root.root()

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setObjectName("MainWindow")
        self.setFixedSize(895, 715)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(350, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.information_table = QtWidgets.QTableWidget(self.centralwidget)
        self.information_table.setGeometry(QtCore.QRect(70, 60, 751, 291))
        self.information_table.setObjectName("information_table")
        self.information_table.setColumnCount(5)
        self.information_table.setHorizontalHeaderLabels(['管理员姓名', '管理员ID', '设备类型','设备名称','设备ID'])
        self.information_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.information_table.horizontalHeader().setMinimumHeight(50)
        self.information_table.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(96, 163, 230);font:24pt '华文仿宋';color: black;};")
        self.information_table.verticalHeader().setVisible(False)
        self.information_table.setFont(QFont("STFangsong", 18))
        self.information_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.number_table = QtWidgets.QTableWidget(self.centralwidget)
        self.number_table.setGeometry(QtCore.QRect(230, 410, 391, 192))
        self.number_table.setObjectName("number_table")
        self.number_table.setColumnCount(3)
        self.number_table.setHorizontalHeaderLabels(['管理员姓名', '管理员ID', '设备总数'])
        self.number_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.number_table.horizontalHeader().setMinimumHeight(50)
        self.number_table.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(96, 163, 230);font:24pt '华文仿宋';color: black;};")
        self.number_table.verticalHeader().setVisible(False)
        self.number_table.setFont(QFont("STFangsong", 18))
        self.number_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 370, 251, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.setCentralWidget(self.centralwidget)

        self.label_2.setText("管理员设备信息表")
        self.label_3.setText("管理员设备数量信息表")

        self.get_unused_device()

        self.setCentralWidget(self.centralwidget)
        self.draw()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def get_unused_device(self):
        information = self.root.manager_respon_device()
        i=-1
        for row_item in information:
            i=i+1
            self.information_table.setRowCount(i+1)
            self.information_table.setItem(i,0,QTableWidgetItem(str(row_item[0])))
            self.information_table.setItem(i,1,QTableWidgetItem(str(row_item[1])))
            self.information_table.setItem(i,2,QTableWidgetItem(str(row_item[4])))
            self.information_table.setItem(i,3,QTableWidgetItem(str(row_item[3])))
            self.information_table.setItem(i,4,QTableWidgetItem(str(row_item[2])))
            for j in range(0,5):
                self.information_table.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
            self.information_table.setRowHeight(i,40)# 设置table表格第4行的高度

        number = self.root.manager_person_device_statistics()
        i=-1
        for row_item in number:
            i=i+1
            self.number_table.setRowCount(i+1)
            self.number_table.setItem(i,0,QTableWidgetItem(str(row_item[0])))
            self.number_table.setItem(i,1,QTableWidgetItem(str(row_item[1])))
            self.number_table.setItem(i,2,QTableWidgetItem(str(row_item[2])))
            # self.number_table.setItem(i,3,QTableWidgetItem(str(row_item[3])))
            # self.number_table.setItem(i,4,QTableWidgetItem(str(row_item[2])))
            for j in range(0,3):
                self.number_table.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
            self.number_table.setRowHeight(i,40)# 设置table表格第4行的高度
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "设备动态"))

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic101.JPG")))
        self.setPalette(self.palette)

    windowList = []
    def closeEvent(self, event):
        the_window3 = MainUi()
        self.windowList.append(the_window3)  ##注：没有这句，是不打开另一个主界面的！
        the_window3.show()
        event.accept()




class people_management(QtWidgets.QMainWindow):
    root = root.root()

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setObjectName("people_management")
        self.setFixedSize(600,400)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.table_unused_tablewidget = QtWidgets.QTableWidget(self.centralwidget)
        self.table_unused_tablewidget.setGeometry(QtCore.QRect(90, 50, 400, 280))
        self.table_unused_tablewidget.setObjectName("tableView")
        self.table_unused_tablewidget.setColumnCount(2)
        self.table_unused_tablewidget.setHorizontalHeaderLabels(['部门名称', '部门人数'])
        self.table_unused_tablewidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table_unused_tablewidget.horizontalHeader().setMinimumHeight(50)
        self.table_unused_tablewidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(96, 163, 230);font:24pt '华文仿宋';color: black;};")
        self.table_unused_tablewidget.verticalHeader().setVisible(False)
        self.table_unused_tablewidget.setFont(QFont("STFangsong", 18))
        self.table_unused_tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.get_data()

        self.setCentralWidget(self.centralwidget)
        self.draw()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def get_data(self):
        useabledevice = self.root.department_stastics()
        i=-1
        for row_item in useabledevice:
            i=i+1
            self.table_unused_tablewidget.setRowCount(i+1)
            self.table_unused_tablewidget.setItem(i,0,QTableWidgetItem(str(row_item[0])))
            self.table_unused_tablewidget.setItem(i,1,QTableWidgetItem(str(row_item[1])))
            # self.table_unused_tablewidget.setItem(i,2,QTableWidgetItem(str(row_item[2])))
            for j in range(0,2):
                self.table_unused_tablewidget.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_unused_tablewidget.setRowHeight(i,40)# 设置table表格第4行的高度
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "人员管理"))

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic101.JPG")))
        self.setPalette(self.palette)

    windowList = []
    def closeEvent(self, event):
        the_window3 = MainUi()
        self.windowList.append(the_window3)  ##注：没有这句，是不打开另一个主界面的！
        the_window3.show()
        event.accept()






class supplier_information(QtWidgets.QMainWindow):
    root = root.root()

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setObjectName("supplier_information")
        self.setFixedSize(1160,700)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.table_unused_tablewidget = QtWidgets.QTableWidget(self.centralwidget)
        self.table_unused_tablewidget.setGeometry(QtCore.QRect(70, 50, 1000, 600))
        self.table_unused_tablewidget.setObjectName("tableView")
        self.table_unused_tablewidget.setColumnCount(4)
        self.table_unused_tablewidget.setHorizontalHeaderLabels(['供应商编号', '供应商名称','供应商电话','供应商邮箱'])
        self.table_unused_tablewidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table_unused_tablewidget.horizontalHeader().setMinimumHeight(50)
        self.table_unused_tablewidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(96, 163, 230);font:24pt '华文仿宋';color: black;};")
        self.table_unused_tablewidget.verticalHeader().setVisible(False)
        self.table_unused_tablewidget.setFont(QFont("STFangsong", 18))
        self.table_unused_tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.get_data()

        self.setCentralWidget(self.centralwidget)
        self.draw()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def get_data(self):
        useabledevice = self.root.sql_all_supplier_info()
        i=-1
        for row_item in useabledevice:
            i=i+1
            self.table_unused_tablewidget.setRowCount(i+1)
            self.table_unused_tablewidget.setItem(i,0,QTableWidgetItem(str(row_item[0])))
            self.table_unused_tablewidget.setItem(i,1,QTableWidgetItem(str(row_item[1])))
            self.table_unused_tablewidget.setItem(i,2,QTableWidgetItem(str(row_item[2])))
            self.table_unused_tablewidget.setItem(i,3,QTableWidgetItem(str(row_item[3])))
            for j in range(0,4):
                self.table_unused_tablewidget.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_unused_tablewidget.setRowHeight(i,40)# 设置table表格第4行的高度
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "厂商信息"))

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic101.JPG")))
        self.setPalette(self.palette)

    windowList = []
    def closeEvent(self, event):
        the_window3 = MainUi()
        self.windowList.append(the_window3)  ##注：没有这句，是不打开另一个主界面的！
        the_window3.show()
        event.accept()







class supplier_equip_info(QtWidgets.QMainWindow):
    root = root.root()

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setObjectName("supplier_information")
        self.setObjectName("MainWindow")
        self.resize(980, 746)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 20, 221, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.equip_infor = QtWidgets.QTableWidget(self.centralwidget)
        self.equip_infor.setGeometry(QtCore.QRect(50, 60, 881, 291))
        self.equip_infor.setObjectName("equip_infor")
        self.equip_infor.setColumnCount(5)
        self.equip_infor.setHorizontalHeaderLabels(['供应商编号', '供应商名称','供应设备名','供应设备类型','设备价格'])
        self.equip_infor.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.equip_infor.horizontalHeader().setMinimumHeight(50)
        self.equip_infor.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(96, 163, 230);font:24pt '华文仿宋';color: black;};")
        self.equip_infor.verticalHeader().setVisible(False)
        self.equip_infor.setFont(QFont("STFangsong", 18))
        self.equip_infor.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.equip_number = QtWidgets.QTableWidget(self.centralwidget)
        self.equip_number.setGeometry(QtCore.QRect(290, 410, 441, 291))
        self.equip_number.setObjectName("equip_number")
        self.equip_number.setColumnCount(3)
        self.equip_number.setHorizontalHeaderLabels(['供应商编号', '供应商名称','供应设备总数'])
        self.equip_number.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.equip_number.horizontalHeader().setMinimumHeight(50)
        self.equip_number.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(96, 163, 230);font:24pt '华文仿宋';color: black;};")
        self.equip_number.verticalHeader().setVisible(False)
        self.equip_number.setFont(QFont("STFangsong", 18))
        self.equip_number.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 370, 221, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.setCentralWidget(self.centralwidget)

        self.label_2.setText("供应商供应设备信息")
        self.label_3.setText("供应商供应数量信息")

        self.get_data()

        self.setCentralWidget(self.centralwidget)
        self.draw()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def get_data(self):
        equip_info = self.root.sql_supplier_info()
        i=-1
        for row_item in equip_info:
            i=i+1
            self.equip_infor.setRowCount(i+1)
            self.equip_infor.setItem(i,0,QTableWidgetItem(str(row_item[0])))
            self.equip_infor.setItem(i,1,QTableWidgetItem(str(row_item[1])))
            self.equip_infor.setItem(i,2,QTableWidgetItem(str(row_item[2])))
            self.equip_infor.setItem(i,3,QTableWidgetItem(str(row_item[3])))
            self.equip_infor.setItem(i,4,QTableWidgetItem(str(row_item[4])))
            for j in range(0,5):
                self.equip_infor.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
            self.equip_infor.setRowHeight(i,40)# 设置table表格第4行的高度

        equip_numbers = self.root.supplier_statistics()
        i=-1
        for row_item in equip_numbers:
            i=i+1
            self.equip_number.setRowCount(i+1)
            self.equip_number.setItem(i,0,QTableWidgetItem(str(row_item[0])))
            self.equip_number.setItem(i,1,QTableWidgetItem(str(row_item[1])))
            self.equip_number.setItem(i,2,QTableWidgetItem(str(row_item[2])))
            # self.equip_number.setItem(i,3,QTableWidgetItem(str(row_item[3])))
            # self.equip_number.setItem(i,4,QTableWidgetItem(str(row_item[4])))
            for j in range(0,3):
                self.equip_number.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
            self.equip_number.setRowHeight(i,40)# 设置table表格第4行的高度
            
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "供应信息"))

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic101.JPG")))
        self.setPalette(self.palette)

    windowList = []
    def closeEvent(self, event):
        the_window3 = MainUi()
        self.windowList.append(the_window3)  ##注：没有这句，是不打开另一个主界面的！
        the_window3.show()
        event.accept()





class equip_information(QtWidgets.QMainWindow):
    root = root.root()

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setObjectName("equip_information")
        self.setFixedSize(1400,600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.table_unused_tablewidget = QtWidgets.QTableWidget(self.centralwidget)
        self.table_unused_tablewidget.setGeometry(QtCore.QRect(50, 40, 1300, 500))
        self.table_unused_tablewidget.setObjectName("tableView")
        self.table_unused_tablewidget.setColumnCount(9)
        self.table_unused_tablewidget.setHorizontalHeaderLabels(['设备ID', '设备名', '设备类型','重要等级','设备价格','设备负责人','设备状态','设备属性','设备供应商'])
        self.table_unused_tablewidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table_unused_tablewidget.horizontalHeader().setMinimumHeight(50)
        self.table_unused_tablewidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(96, 163, 230);font:24pt '华文仿宋';color: black;};")
        self.table_unused_tablewidget.verticalHeader().setVisible(False)
        self.table_unused_tablewidget.setFont(QFont("STFangsong", 18))
        self.table_unused_tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.get_unused_device()

        self.setCentralWidget(self.centralwidget)
        self.draw()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def get_unused_device(self):
        device_infor = self.root.sql_device_info()
        i=-1
        for row_item in device_infor:
            i=i+1
            self.table_unused_tablewidget.setRowCount(i+1)
            self.table_unused_tablewidget.setItem(i,0,QTableWidgetItem(str(row_item[0])))
            self.table_unused_tablewidget.setItem(i,1,QTableWidgetItem(str(row_item[2])))
            self.table_unused_tablewidget.setItem(i,2,QTableWidgetItem(str(row_item[1])))
            self.table_unused_tablewidget.setItem(i,3,QTableWidgetItem(str(row_item[3])))
            self.table_unused_tablewidget.setItem(i,4,QTableWidgetItem(str(row_item[4])))
            self.table_unused_tablewidget.setItem(i,5,QTableWidgetItem(str(row_item[5])))
            self.table_unused_tablewidget.setItem(i,6,QTableWidgetItem(str(row_item[6])))
            self.table_unused_tablewidget.setItem(i,7,QTableWidgetItem(str(row_item[7])))
            self.table_unused_tablewidget.setItem(i,8,QTableWidgetItem(str(row_item[8])))
            for j in range(0,9):
                self.table_unused_tablewidget.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_unused_tablewidget.setRowHeight(i,40)# 设置table表格第4行的高度
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "设备情况"))

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic101.JPG")))
        self.setPalette(self.palette)

    windowList = []
    def closeEvent(self, event):
        the_window3 = MainUi()
        self.windowList.append(the_window3)  ##注：没有这句，是不打开另一个主界面的！
        the_window3.show()
        event.accept()






class add_equipment(QtWidgets.QMainWindow):
    root = root.root()

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):  
        self.setObjectName("MainWindow")
        self.setObjectName("MainWindow")
        self.resize(634, 354)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 30, 221, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 80, 231, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 130, 221, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 180, 251, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 230, 221, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.equip_type = QtWidgets.QLineEdit(self.centralwidget)
        self.equip_type.setGeometry(QtCore.QRect(300, 30, 251, 31))
        self.equip_type.setObjectName("equip_type")

        self.safety = QtWidgets.QLineEdit(self.centralwidget)
        self.safety.setGeometry(QtCore.QRect(300, 80, 251, 31))
        self.safety.setObjectName("safety")

        self.price = QtWidgets.QLineEdit(self.centralwidget)
        self.price.setGeometry(QtCore.QRect(300, 130, 251, 31))
        self.price.setObjectName("price")

        self.manager_name = QtWidgets.QLineEdit(self.centralwidget)
        self.manager_name.setGeometry(QtCore.QRect(300, 180, 251, 31))
        self.manager_name.setObjectName("manager_name")

        self.supplier_name = QtWidgets.QLineEdit(self.centralwidget)
        self.supplier_name.setGeometry(QtCore.QRect(300, 230, 251, 31))
        self.supplier_name.setObjectName("supplier_name")
        self.setCentralWidget(self.centralwidget)

        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(360, 300, 121, 41))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.cancel.setFont(font)
        self.cancel.setObjectName("cancel")
        self.OK = QtWidgets.QPushButton(self.centralwidget)
        self.OK.setGeometry(QtCore.QRect(510, 300, 121, 41))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.OK.setFont(font)
        self.OK.setObjectName("OK")

        self.OK.clicked.connect(self.message_1)

        self.label_2.setText("请输入设备类型：")
        self.label_3.setText("请输入设备重要等级：")
        self.label_4.setText("请输入设备价格：")
        self.label_5.setText("请输入设备负责人姓名：")
        self.label_6.setText("请输入供应商名：")
        self.cancel.setText("取消")
        self.OK.setText("确认")

        self.setCentralWidget(self.centralwidget)
        self.draw()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def message_1(self):
        equip_type_x = self.equip_type.text() 
        safety_x = self.safety.text()
        price_x = self.price.text()
        manager_name_x = self.manager_name.text()
        supplier_name_x = self.supplier_name.text()
        If_add =True
        If_add = self.root.add_device(str(equip_type_x),str(safety_x),str(price_x),str(manager_name_x),str(supplier_name_x))
        if(If_add==False):
            QMessageBox.warning(self,"提示","添加失败！",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        else:
            QMessageBox.information(self,"提示","添加成功!",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "添加设备"))

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic101.JPG")))
        self.setPalette(self.palette)

    windowList = []
    def closeEvent(self, event):
        the_window3 = MainUi()
        self.windowList.append(the_window3)  ##注：没有这句，是不打开另一个主界面的！
        the_window3.show()
        event.accept()





class user_information(QtWidgets.QMainWindow):
    def __init__(self):
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

        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(155, 180, 175, 65))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(68)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.setCentralWidget(self.centralwidget)

        self.label.setText("TextLabel")
        self.label_3.setText("root")

        self.draw()
        self._plain_pic()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic101.JPG")))
        self.setPalette(self.palette)

    def _plain_pic(self):
        pixmapa = QPixmap("pics/pic105.png")
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
        the_window = MainUi()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        the_window.show()
        event.accept()








def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()
