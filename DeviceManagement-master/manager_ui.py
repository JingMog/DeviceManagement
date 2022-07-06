from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem,QPushButton,QAbstractItemView,QMenu
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPalette,QBrush,QPixmap,QFont,QPainter,QPainterPath
from PyQt5.QtCore import Qt
import sys
import qtawesome
import time
import manager

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
 
        self.left_label_1 = QtWidgets.QPushButton("申请处理")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("统计信息")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("数据管理")
        self.left_label_3.setObjectName('left_label')
 
        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.tasks',color='white'),"借用申请")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.wrench',color='white'),"维修申请")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.edit',color='white'),"违规统计")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.bar-chart',color='white'),"借用统计")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.exchange',color='white'),"维修统计")
        self.left_button_5.setObjectName('left_button')
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.folder-open',color='white'),"设备信息")
        self.left_button_6.setObjectName('left_button')
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.list-ol',color='white'),"我的通过")
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
        self.recommend_button_1.setIcon(QtGui.QIcon('pics/panda1.jpg')) # 设置按钮图标
        self.recommend_button_1.setIconSize(QtCore.QSize(150,150)) # 设置图标大小
        self.recommend_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon) # 设置按钮形式为上图下文
 
        self.recommend_button_2 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.recommend_button_2.setFont(font)
        self.recommend_button_2.setText("设备2")
        self.recommend_button_2.setIcon(QtGui.QIcon('pics/panda2.jpg'))
        self.recommend_button_2.setIconSize(QtCore.QSize(150, 150))
        self.recommend_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.recommend_button_3 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.recommend_button_3.setFont(font)
        self.recommend_button_3.setText("设备3")
        self.recommend_button_3.setIcon(QtGui.QIcon('pics/panda1.jpg'))
        self.recommend_button_3.setIconSize(QtCore.QSize(150, 150))
        self.recommend_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.recommend_button_4 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.recommend_button_4.setFont(font)
        self.recommend_button_4.setText("设备4")
        self.recommend_button_4.setIcon(QtGui.QIcon('pics/panda2.jpg'))
        self.recommend_button_4.setIconSize(QtCore.QSize(150, 150))
        self.recommend_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.recommend_button_5 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.recommend_button_5.setFont(font)
        self.recommend_button_5.setText("设备5")
        self.recommend_button_5.setIcon(QtGui.QIcon('pics/panda1.jpg'))
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
        self.recommend_button_6.setIcon(QtGui.QIcon('pics/panda2.jpg')) # 设置按钮图标
        self.recommend_button_6.setIconSize(QtCore.QSize(150,150)) # 设置图标大小
        self.recommend_button_6.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon) # 设置按钮形式为上图下文
 
        self.recommend_button_7 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.recommend_button_7.setFont(font)
        self.recommend_button_7.setText("设备7")
        self.recommend_button_7.setIcon(QtGui.QIcon('pics/panda1.jpg'))
        self.recommend_button_7.setIconSize(QtCore.QSize(150, 150))
        self.recommend_button_7.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.recommend_button_8 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.recommend_button_8.setFont(font)
        self.recommend_button_8.setText("设备8")
        self.recommend_button_8.setIcon(QtGui.QIcon('pics/panda2.jpg'))
        self.recommend_button_8.setIconSize(QtCore.QSize(150, 150))
        self.recommend_button_8.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.recommend_button_9 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.recommend_button_9.setFont(font)
        self.recommend_button_9.setText("设备9")
        self.recommend_button_9.setIcon(QtGui.QIcon('pics/panda1.jpg'))
        self.recommend_button_9.setIconSize(QtCore.QSize(150, 150))
        self.recommend_button_9.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
 
        self.recommend_button_10 = QtWidgets.QToolButton()
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(18)
        self.recommend_button_10.setFont(font)
        self.recommend_button_10.setText("设备10")
        self.recommend_button_10.setIcon(QtGui.QIcon('pics/panda2.jpg'))
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
            background:rgb(167, 196, 149);
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
        the_window1 = manage_borrow(self.user_id)
        self.windowList.append(the_window1)   
        ##注：没有这句，是不打开另一个主界面的！
        self.close()
        the_window1.show()
 
    def on_left_button_2_clicked(self):
        the_window2 = manage_repair(self.user_id)
        self.windowList.append(the_window2)   
        self.close()
        the_window2.show()

    def on_left_button_3_clicked(self):
        the_window2 = wrong_return(self.user_id)
        self.windowList.append(the_window2)   
        self.close()
        the_window2.show()

    def on_left_button_4_clicked(self):
        the_window3 = statistics_borrow_all(self.user_id)
        self.windowList.append(the_window3)   
        self.close()
        the_window3.show()

    def on_left_button_5_clicked(self):
        the_window5 = statistcis_repair(self.user_id)
        self.windowList.append(the_window5)   
        self.close()
        the_window5.show()

    def on_left_button_6_clicked(self):
        the_window3 = equip_information(self.user_id)
        self.windowList.append(the_window3)   
        self.close()
        the_window3.show()

    def on_left_button_7_clicked(self):
        the_window7 = my_data(self.user_id)
        self.windowList.append(the_window7)   
        self.close()
        the_window7.show()

    def on_left_button_8_clicked(self):
        the_window8 = user_information(self.user_id)
        self.windowList.append(the_window8)   
        self.close()
        the_window8.show()

    # 关闭按钮动作函数
    def close_window(self):
        self.close()



class manage_borrow(QtWidgets.QMainWindow):
    user_id = ''
    manager_x = ''

    def __init__(self,user_id):
        self.user_id = user_id
        self.manager_x = manager.manager(self.user_id)
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setObjectName("manage_borrow_table")
        self.setFixedSize(1200,600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.table_unused_tablewidget = QtWidgets.QTableWidget(self.centralwidget)
        self.table_unused_tablewidget.setGeometry(QtCore.QRect(50, 40, 1100, 500))
        self.table_unused_tablewidget.setObjectName("tableView")
        self.table_unused_tablewidget.setColumnCount(7)
        self.table_unused_tablewidget.setHorizontalHeaderLabels(['借用编号','设备名', '设备ID', '申请人姓名','申请人ID','借用日期','预估时间'])
        self.table_unused_tablewidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table_unused_tablewidget.horizontalHeader().setMinimumHeight(50)
        self.table_unused_tablewidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(185, 209, 163);font:24pt '华文仿宋';color: black;};")
        self.table_unused_tablewidget.verticalHeader().setVisible(False)
        self.table_unused_tablewidget.setFont(QFont("STFangsong", 18))
        self.table_unused_tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.get_data()

        self.setCentralWidget(self.centralwidget)
        self.draw()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.table_unused_tablewidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table_unused_tablewidget.customContextMenuRequested.connect(self.show_menu)

    def show_menu(self,pos):
        for i in self.table_unused_tablewidget.selectionModel().selection().indexes():
            rowNum = i.row()
        menu = QMenu()
        item1 = menu.addAction("同意")
        screenPos = self.table_unused_tablewidget.mapToGlobal(pos)
        action = menu.exec(screenPos)
        # 获取use_id
        record = self.manager_x.sql_unapprove_record()
        use_id = record[rowNum][0]
        if action == item1:
            self.slot_1(use_id=use_id)
        else:
            return


    def get_data(self):
        useabledevice = self.manager_x.sql_unapprove_record()
        i=-1
        for row_item in useabledevice:
            i=i+1
            self.table_unused_tablewidget.setRowCount(i+1)
            self.table_unused_tablewidget.setItem(i,0,QTableWidgetItem(str(row_item[0])))
            self.table_unused_tablewidget.setItem(i,1,QTableWidgetItem(str(row_item[1])))
            self.table_unused_tablewidget.setItem(i,2,QTableWidgetItem(str(row_item[2])))
            self.table_unused_tablewidget.setItem(i,3,QTableWidgetItem(str(row_item[4])))
            self.table_unused_tablewidget.setItem(i,4,QTableWidgetItem(str(row_item[3])))
            self.table_unused_tablewidget.setItem(i,5,QTableWidgetItem(str(row_item[5])))
            self.table_unused_tablewidget.setItem(i,6,QTableWidgetItem(str(row_item[6])))
            for j in range(0,7):
                self.table_unused_tablewidget.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_unused_tablewidget.setRowHeight(i,40)

    def slot_1(self,use_id):
        button = self.sender()
        if button:
        	# 确定位置的时候这里是关键
            row = self.table_unused_tablewidget.indexAt(button.parent().pos()).row() 
            print(row)
        If_agree = self.manager_x.deal_use_apply(use_id)
        if(If_agree==False):
            QMessageBox.warning(self,"提示","处理失败!该设备不存在借用情况或已被批准",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        if(If_agree==True):
            QMessageBox.information(self,"提示","处理成功!",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        
        # 批准一个记录之后重新显示表格
        self.get_data()



           
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "借用申请"))

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic004.JPG")))
        self.setPalette(self.palette)

    windowList = []
    def closeEvent(self, event):
        the_window3 = MainUi(self.user_id)
        self.windowList.append(the_window3)  ##注：没有这句，是不打开另一个主界面的！
        the_window3.show()
        event.accept()

    





class manage_repair(QtWidgets.QMainWindow):
    user_id = ''
    manager_x = ''

    def __init__(self,user_id):
        self.user_id = user_id
        self.manager_x = manager.manager(self.user_id)
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setObjectName("manage_repair_table")
        self.setFixedSize(1200,600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.table_unused_tablewidget = QtWidgets.QTableWidget(self.centralwidget)
        self.table_unused_tablewidget.setGeometry(QtCore.QRect(50, 40, 1100, 500))
        self.table_unused_tablewidget.setObjectName("tableView")
        self.table_unused_tablewidget.setColumnCount(4)
        self.table_unused_tablewidget.setHorizontalHeaderLabels(['维修编号','设备ID', '申请人姓名','申请人ID'])
        self.table_unused_tablewidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table_unused_tablewidget.horizontalHeader().setMinimumHeight(50)
        self.table_unused_tablewidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(185, 209, 163);font:24pt '华文仿宋';color: black;};")
        self.table_unused_tablewidget.verticalHeader().setVisible(False)
        self.table_unused_tablewidget.setFont(QFont("STFangsong", 18))
        self.table_unused_tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.table_unused_tablewidget.Readonly

        self.get_data()

        self.setCentralWidget(self.centralwidget)
        self.draw()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.table_unused_tablewidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table_unused_tablewidget.customContextMenuRequested.connect(self.show_menu)

    def show_menu(self,pos):
        for i in self.table_unused_tablewidget.selectionModel().selection().indexes():
            rowNum = i.row()
        menu = QMenu()
        item1 = menu.addAction("同意")
        screenPos = self.table_unused_tablewidget.mapToGlobal(pos)
        action = menu.exec(screenPos)
        # 获取use_id
        record = self.manager_x.sql_unrepair_record()
        use_id = record[rowNum][0]
        if action == item1:
            # print("同意")
            self.slot_1(use_id=use_id)
        else:
            return

    def get_data(self):
        useabledevice = self.manager_x.sql_unrepair_record()
        i=-1
        for row_item in useabledevice:
            i=i+1
            self.table_unused_tablewidget.setRowCount(i+1)
            self.table_unused_tablewidget.setItem(i,0,QTableWidgetItem(str(row_item[0])))
            self.table_unused_tablewidget.setItem(i,1,QTableWidgetItem(str(row_item[1])))
            self.table_unused_tablewidget.setItem(i,2,QTableWidgetItem(str(row_item[3])))
            self.table_unused_tablewidget.setItem(i,3,QTableWidgetItem(str(row_item[4])))
            for j in range(0,4):
                self.table_unused_tablewidget.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_unused_tablewidget.setRowHeight(i,40)

    def slot_1(self,use_id):
        button = self.sender()
        if button:
        	# 确定位置的时候这里是关键
            row = self.table_unused_tablewidget.indexAt(button.parent().pos()).row() 
        If_agree = self.manager_x.deal_repair_apply(use_id)
        if(If_agree==False):
            QMessageBox.warning(self,"提示","处理失败!该设备不存在维修情况或已被维修",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        else:
            QMessageBox.information(self,"提示","处理成功!",QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        
        # 批准一个记录之后重新显示表格
        self.get_data()
     
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "维修申请"))

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic004.JPG")))
        self.setPalette(self.palette)

    windowList = []
    def closeEvent(self, event):
        the_window3 = MainUi(self.user_id)
        self.windowList.append(the_window3)  ##注：没有这句，是不打开另一个主界面的！
        the_window3.show()
        event.accept()








class wrong_return(QtWidgets.QMainWindow):
    user_id = ''
    manager_x = ''

    def __init__(self,user_id):
        self.user_id = user_id
        self.manager_x = manager.manager(self.user_id)
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setObjectName("wrong_return")
        self.setFixedSize(1430,600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.table_unused_tablewidget = QtWidgets.QTableWidget(self.centralwidget)
        self.table_unused_tablewidget.setGeometry(QtCore.QRect(50, 40, 1340, 500))
        self.table_unused_tablewidget.setObjectName("tableView")
        self.table_unused_tablewidget.setColumnCount(9)
        self.table_unused_tablewidget.setHorizontalHeaderLabels(['借用编号', '设备名', '设备ID','借用人','借用时间','预计使用时间','归还时间','归还状态','是否超时','批准人'])
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
        wrong_returned = self.manager_x.sql_all_violate()
        i=-1
        for row_item in wrong_returned:
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
        MainWindow.setWindowTitle(_translate("MainWindow", "违规统计"))

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic006.JPG")))
        self.setPalette(self.palette)

    windowList = []
    def closeEvent(self, event):
        the_window3 = MainUi(self.user_id)
        self.windowList.append(the_window3)  ##注：没有这句，是不打开另一个主界面的！
        the_window3.show()
        event.accept()









class statistics_borrow_all(QtWidgets.QMainWindow):
    user_id = ''
    manager_x = ''

    def __init__(self,user_id):
        self.user_id = user_id
        self.manager_x = manager.manager(self.user_id)
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setObjectName("statistics_borrow_all")
        self.setFixedSize(1457, 951)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.all_borrowed = QtWidgets.QTableWidget(self.centralwidget)
        self.all_borrowed.setGeometry(QtCore.QRect(70, 50, 1311, 401))
        self.all_borrowed.setObjectName("all_borrowed")
        self.all_borrowed.setColumnCount(8)
        self.all_borrowed.setHorizontalHeaderLabels(['借用编号','设备名', '借用人姓名','借用日期','归还日期','归还状态','是否超时','批准人'])
        self.all_borrowed.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.all_borrowed.horizontalHeader().setMinimumHeight(50)
        self.all_borrowed.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(185, 209, 163);font:24pt '华文仿宋';color: black;};")
        self.all_borrowed.verticalHeader().setVisible(False)
        self.all_borrowed.setFont(QFont("STFangsong", 18))
        self.all_borrowed.setEditTriggers(QAbstractItemView.NoEditTriggers)



        self.havent_returned = QtWidgets.QTableWidget(self.centralwidget)
        self.havent_returned.setGeometry(QtCore.QRect(70, 510, 1011, 331))
        self.havent_returned.setObjectName("havent_returned")
        self.havent_returned.setColumnCount(6)
        self.havent_returned.setHorizontalHeaderLabels(['借用编号','设备名', '借用人姓名','借用日期','使用时间','批准人'])
        self.havent_returned.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.havent_returned.horizontalHeader().setMinimumHeight(50)
        self.havent_returned.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(185, 209, 163);font:24pt '华文仿宋';color: black;};")
        self.havent_returned.verticalHeader().setVisible(False)
        self.havent_returned.setFont(QFont("STFangsong", 18))
        self.havent_returned.setEditTriggers(QAbstractItemView.NoEditTriggers)



        self.equip_lend = QtWidgets.QTableWidget(self.centralwidget)
        self.equip_lend.setGeometry(QtCore.QRect(1100, 510, 291, 331))
        self.equip_lend.setObjectName("equip_lend")
        self.equip_lend.setColumnCount(2)
        self.equip_lend.setHorizontalHeaderLabels(['设备类型','借用次数'])
        self.equip_lend.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.equip_lend.horizontalHeader().setMinimumHeight(50)
        self.equip_lend.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(185, 209, 163);font:24pt '华文仿宋';color: black;};")
        self.equip_lend.verticalHeader().setVisible(False)
        self.equip_lend.setFont(QFont("STFangsong", 18))
        self.equip_lend.setEditTriggers(QAbstractItemView.NoEditTriggers)



        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(620, 10, 201, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 470, 201, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1145, 470, 201, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.setCentralWidget(self.centralwidget)

        self.label.setText("已完成的借用记录")
        self.label_2.setText("未归还的借用记录")
        self.label_3.setText("设备借用情况统计")

        self.get_data()
        self.draw()
        self.retranslateUi(self)

    def get_data(self):
        all_borrow = self.manager_x.sql_use_record()
        i=-1
        for row_item in all_borrow:
            i=i+1
            self.all_borrowed.setRowCount(i+1)
            self.all_borrowed.setItem(i,0,QTableWidgetItem(str(row_item[0])))
            self.all_borrowed.setItem(i,1,QTableWidgetItem(str(row_item[1])))
            self.all_borrowed.setItem(i,2,QTableWidgetItem(str(row_item[2])))
            self.all_borrowed.setItem(i,3,QTableWidgetItem(str(row_item[4])))
            self.all_borrowed.setItem(i,4,QTableWidgetItem(str(row_item[5])))
            self.all_borrowed.setItem(i,5,QTableWidgetItem(str(row_item[6])))
            self.all_borrowed.setItem(i,6,QTableWidgetItem(str(row_item[7])))
            self.all_borrowed.setItem(i,7,QTableWidgetItem(str(row_item[8])))
            # self.table_unused_tablewidget.setItem(i,8,QTableWidgetItem(str(row_item[8])))
            for j in range(0,8):
                self.all_borrowed.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
            self.all_borrowed.setRowHeight(i,40)

        havent_return = self.manager_x.sql_unreturn_record()
        i=-1
        for row_item in havent_return:
            i=i+1
            self.havent_returned.setRowCount(i+1)
            self.havent_returned.setItem(i,0,QTableWidgetItem(str(row_item[0])))
            self.havent_returned.setItem(i,1,QTableWidgetItem(str(row_item[1])))
            self.havent_returned.setItem(i,2,QTableWidgetItem(str(row_item[4])))
            self.havent_returned.setItem(i,3,QTableWidgetItem(str(row_item[5])))
            self.havent_returned.setItem(i,4,QTableWidgetItem(str(row_item[6])))
            self.havent_returned.setItem(i,5,QTableWidgetItem(str(row_item[7])))
            for j in range(0,6):
                self.havent_returned.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
            self.havent_returned.setRowHeight(i,40)

        equip_lend = self.manager_x.device_use_statistics()
        i=-1
        for row_item in equip_lend:
            i=i+1
            self.equip_lend.setRowCount(i+1)
            self.equip_lend.setItem(i,0,QTableWidgetItem(str(row_item[0])))
            self.equip_lend.setItem(i,1,QTableWidgetItem(str(row_item[1])))
            for j in range(0,2):
                self.equip_lend.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
            self.equip_lend.setRowHeight(i,40)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "借用统计"))

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic006.JPG")))
        self.setPalette(self.palette)

    windowList = []
    def closeEvent(self, event):
        the_window3 = MainUi(self.user_id)
        self.windowList.append(the_window3)  ##注：没有这句，是不打开另一个主界面的！
        the_window3.show()
        event.accept()








class statistcis_repair(QtWidgets.QMainWindow):
    user_id = ''
    manager_x = ''

    def __init__(self,user_id):
        self.user_id = user_id
        self.manager_x = manager.manager(self.user_id)
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setObjectName("MainWindow")
        self.resize(1141, 887)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        self.repaired_equip = QtWidgets.QTableWidget(self.centralwidget)
        self.repaired_equip.setGeometry(QtCore.QRect(50, 70, 1031, 331))
        self.repaired_equip.setObjectName("repaired_equip")
        self.repaired_equip.setColumnCount(7)
        self.repaired_equip.setHorizontalHeaderLabels(['维修编号','设备名','设备ID','申请人','维修人','维修日期','维修结果'])
        self.repaired_equip.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.repaired_equip.horizontalHeader().setMinimumHeight(50)
        self.repaired_equip.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(185, 209, 163);font:24pt '华文仿宋';color: black;};")
        self.repaired_equip.verticalHeader().setVisible(False)
        self.repaired_equip.setFont(QFont("STFangsong", 18))
        self.repaired_equip.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.equip_repaired = QtWidgets.QTableWidget(self.centralwidget)
        self.equip_repaired.setGeometry(QtCore.QRect(170, 460, 331, 331))
        self.equip_repaired.setObjectName("equip_repaired")
        self.equip_repaired.setColumnCount(2)
        self.equip_repaired.setHorizontalHeaderLabels(['设备类型','维修次数'])
        self.equip_repaired.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.equip_repaired.horizontalHeader().setMinimumHeight(50)
        self.equip_repaired.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(185, 209, 163);font:24pt '华文仿宋';color: black;};")
        self.equip_repaired.verticalHeader().setVisible(False)
        self.equip_repaired.setFont(QFont("STFangsong", 18))
        self.equip_repaired.setEditTriggers(QAbstractItemView.NoEditTriggers)


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(490, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 420, 201, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")


        self.repair_person = QtWidgets.QTableWidget(self.centralwidget)
        self.repair_person.setGeometry(QtCore.QRect(660, 460, 331, 331))
        self.repair_person.setObjectName("repair_person")
        self.repair_person.setColumnCount(2)
        self.repair_person.setHorizontalHeaderLabels(['维修人员姓名','维修次数'])
        self.repair_person.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.repair_person.horizontalHeader().setMinimumHeight(50)
        self.repair_person.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:rgb(185, 209, 163);font:24pt '华文仿宋';color: black;};")
        self.repair_person.verticalHeader().setVisible(False)
        self.repair_person.setFont(QFont("STFangsong", 18))
        self.repair_person.setEditTriggers(QAbstractItemView.NoEditTriggers)



        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(680, 420, 291, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.setCentralWidget(self.centralwidget)

        self.label_2.setText("已完成维修记录")
        self.label_3.setText("设备维修情况统计")
        self.label_4.setText("维修工作人员维修情况统计")

        self.get_data()
        self.draw()
        self.retranslateUi(self)


    def get_data(self):
        euip_repaired = self.manager_x.sql_repair_record()
        i=-1
        for row_item in euip_repaired:
            i=i+1
            self.repaired_equip.setRowCount(i+1)
            self.repaired_equip.setItem(i,0,QTableWidgetItem(str(row_item[0])))
            self.repaired_equip.setItem(i,1,QTableWidgetItem(str(row_item[1])))
            self.repaired_equip.setItem(i,2,QTableWidgetItem(str(row_item[2])))
            self.repaired_equip.setItem(i,3,QTableWidgetItem(str(row_item[7])))
            self.repaired_equip.setItem(i,4,QTableWidgetItem(str(row_item[3])))
            self.repaired_equip.setItem(i,5,QTableWidgetItem(str(row_item[4])))
            self.repaired_equip.setItem(i,6,QTableWidgetItem(str(row_item[5])))
            for j in range(0,7):
                self.repaired_equip.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
            self.repaired_equip.setRowHeight(i,40)

        repair_data = self.manager_x.device_repair_statistics()
        i=-1
        for row_item in repair_data:
            i=i+1
            self.equip_repaired.setRowCount(i+1)
            self.equip_repaired.setItem(i,0,QTableWidgetItem(str(row_item[0])))
            self.equip_repaired.setItem(i,1,QTableWidgetItem(str(row_item[1])))
            for j in range(0,2):
                self.equip_repaired.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
            self.equip_repaired.setRowHeight(i,40)

        repair_person = self.manager_x.repair_person_statistics()
        i=-1
        for row_item in repair_person:
            i=i+1
            self.repair_person.setRowCount(i+1)
            self.repair_person.setItem(i,0,QTableWidgetItem(str(row_item[0])))
            self.repair_person.setItem(i,1,QTableWidgetItem(str(row_item[1])))
            for j in range(0,2):
                self.repair_person.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
            self.repair_person.setRowHeight(i,40)




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "维修统计"))

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic006.JPG")))
        self.setPalette(self.palette)

    windowList = []
    def closeEvent(self, event):
        the_window3 = MainUi(self.user_id)
        self.windowList.append(the_window3)  ##注：没有这句，是不打开另一个主界面的！
        the_window3.show()
        event.accept()







class equip_information(QtWidgets.QMainWindow):
    user_id = ''
    manager_x = ''

    def __init__(self,user_id):
        self.user_id = user_id
        self.manager_x = manager.manager(self.user_id)
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
        device_infor = self.manager_x.sql_device()
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
        MainWindow.setWindowTitle(_translate("MainWindow", "设备信息"))

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic006.JPG")))
        self.setPalette(self.palette)

    windowList = []
    def closeEvent(self, event):
        the_window3 = MainUi(self.user_id)
        self.windowList.append(the_window3)  ##注：没有这句，是不打开另一个主界面的！
        the_window3.show()
        event.accept()



class my_data(QtWidgets.QMainWindow):
    user_id = ''
    manager_x = ''

    def __init__(self,user_id):
        self.user_id = user_id
        self.manager_x = manager.manager(self.user_id)
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setObjectName("my_data")
        self.setFixedSize(1400,600)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.table_unused_tablewidget = QtWidgets.QTableWidget(self.centralwidget)
        self.table_unused_tablewidget.setGeometry(QtCore.QRect(50, 40, 1300, 500))
        self.table_unused_tablewidget.setObjectName("tableView")
        self.table_unused_tablewidget.setColumnCount(8)
        self.table_unused_tablewidget.setHorizontalHeaderLabels(['借用编号', '设备名', '设备ID','借用人','借用日期','预估使用时间','归还日期','是否超时'])
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
        device_infor = self.manager_x.sql_all_del_record()
        i=-1
        for row_item in device_infor:
            i=i+1
            self.table_unused_tablewidget.setRowCount(i+1)
            self.table_unused_tablewidget.setItem(i,0,QTableWidgetItem(str(row_item[0])))
            self.table_unused_tablewidget.setItem(i,1,QTableWidgetItem(str(row_item[1])))
            self.table_unused_tablewidget.setItem(i,2,QTableWidgetItem(str(row_item[2])))
            self.table_unused_tablewidget.setItem(i,3,QTableWidgetItem(str(row_item[3])))
            self.table_unused_tablewidget.setItem(i,4,QTableWidgetItem(str(row_item[4])))
            self.table_unused_tablewidget.setItem(i,5,QTableWidgetItem(str(row_item[5])))
            self.table_unused_tablewidget.setItem(i,6,QTableWidgetItem(str(row_item[6])))
            self.table_unused_tablewidget.setItem(i,7,QTableWidgetItem(str(row_item[7])))
            # self.table_unused_tablewidget.setItem(i,8,QTableWidgetItem(str(row_item[8])))
            for j in range(0,8):
                self.table_unused_tablewidget.item(i,j).setTextAlignment(QtCore.Qt.AlignCenter)
            self.table_unused_tablewidget.setRowHeight(i,40)# 设置table表格第4行的高度
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "我的通过"))

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic006.JPG")))
        self.setPalette(self.palette)

    windowList = []
    def closeEvent(self, event):
        the_window3 = MainUi(self.user_id)
        self.windowList.append(the_window3)  ##注：没有这句，是不打开另一个主界面的！
        the_window3.show()
        event.accept()





class user_information(QtWidgets.QMainWindow):
    user_id = ''
    manager_x = ''

    def __init__(self,user_id):
        self.user_id = user_id
        self.manager_x = manager.manager(self.user_id)
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
        self.label_2.setGeometry(QtCore.QRect(80, 145, 131, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(80, 180, 131, 31))
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

        self.department = QtWidgets.QLabel(self.groupBox)
        self.department.setGeometry(QtCore.QRect(230, 260, 161, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.department.setFont(font)
        self.department.setObjectName("power")

        self.telephone = QtWidgets.QLabel(self.groupBox)
        self.telephone.setGeometry(QtCore.QRect(230, 220, 161, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.telephone.setFont(font)
        self.telephone.setObjectName("department")

        self.user_name = QtWidgets.QLabel(self.groupBox)
        self.user_name.setGeometry(QtCore.QRect(230, 180, 161, 31))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self.user_name.setFont(font)
        self.user_name.setObjectName("user_id")

        self._user_id = QtWidgets.QLabel(self.groupBox)
        self._user_id.setGeometry(QtCore.QRect(230, 150, 161, 21))
        font = QtGui.QFont()
        font.setFamily("STFangsong")
        font.setPointSize(24)
        self._user_id.setFont(font)
        self._user_id.setObjectName("user_name")
        self.setCentralWidget(self.centralwidget)


        self.label.setText("TextLabel")
        self.label_2.setText("管理员姓名：")
        self.label_3.setText("管理员ID：")
        self.label_4.setText("联系方式：")
        self.label_5.setText("所属部门：")

        self.get_user_information()
        self.draw()
        self._plain_pic()

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        

    def get_user_information(self):
        information = self.manager_x.get_person_info()
        self.department.setText(str(information[3]))
        self.telephone.setText(str(information[2]))
        self._user_id.setText(str(information[1]))
        self.user_name.setText(str(information[0]))

    def draw(self):
        self.palette = QPalette()
        self.palette.setBrush(QPalette.Background, QBrush(QPixmap("pics/pic004.JPG")))
        self.setPalette(self.palette)

    def _plain_pic(self):
        pixmapa = QPixmap("pics/picpanda.png")
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
        the_window = MainUi(self.user_id)
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        the_window.show()
        event.accept()


 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi("manager001")
    gui.show()
    sys.exit(app.exec_())