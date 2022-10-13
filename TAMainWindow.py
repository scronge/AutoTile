# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TAMainWindow_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(781, 649)
        MainWindow.setStyleSheet("*{\n"
" border: none;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.slide_menu_container = QtWidgets.QFrame(self.centralwidget)
        self.slide_menu_container.setEnabled(True)
        self.slide_menu_container.setMinimumSize(QtCore.QSize(0, 0))
        self.slide_menu_container.setMaximumSize(QtCore.QSize(0, 16777215))
        self.slide_menu_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.slide_menu_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.slide_menu_container.setObjectName("slide_menu_container")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.slide_menu_container)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.slide_menu = QtWidgets.QFrame(self.slide_menu_container)
        self.slide_menu.setMinimumSize(QtCore.QSize(198, 0))
        self.slide_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.slide_menu.setObjectName("slide_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.slide_menu)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.slide_menu)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Logo_label = QtWidgets.QLabel(self.frame_4)
        self.Logo_label.setMaximumSize(QtCore.QSize(25, 25))
        self.Logo_label.setText("")
        self.Logo_label.setPixmap(QtGui.QPixmap("TileAutomataSimV1/Icons/Logo.png"))
        self.Logo_label.setScaledContents(True)
        self.Logo_label.setObjectName("Logo_label")
        self.horizontalLayout_5.addWidget(self.Logo_label)
        self.Title_label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Title_label.setFont(font)
        self.Title_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.Title_label.setObjectName("Title_label")
        self.horizontalLayout_5.addWidget(self.Title_label, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.verticalLayout_3.addWidget(self.frame_4, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.frame_5 = QtWidgets.QFrame(self.slide_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.toolBox = QtWidgets.QToolBox(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.toolBox.setFont(font)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 154, 430))
        self.page.setStyleSheet("")
        self.page.setObjectName("page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_6 = QtWidgets.QFrame(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.New_button = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.New_button.setFont(font)
        self.New_button.setStyleSheet("QPushButton::hover\n"
"  {\n"
"     background-color : lightblue;\n"
"   }")
        self.New_button.setIconSize(QtCore.QSize(16, 16))
        self.New_button.setObjectName("New_button")
        self.verticalLayout_6.addWidget(self.New_button)
        self.Load_button = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Load_button.setFont(font)
        self.Load_button.setStyleSheet("QPushButton::hover\n"
"  {\n"
"     background-color : lightblue;\n"
"   }")
        self.Load_button.setObjectName("Load_button")
        self.verticalLayout_6.addWidget(self.Load_button)
        self.seededLoadButton = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.seededLoadButton.setFont(font)
        self.seededLoadButton.setStyleSheet("QPushButton::hover\n"
"  {\n"
"     background-color : lightblue;\n"
"   }")
        self.seededLoadButton.setObjectName("seededLoadButton")
        self.verticalLayout_6.addWidget(self.seededLoadButton)
        self.SaveAs_button = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SaveAs_button.setFont(font)
        self.SaveAs_button.setStyleSheet("QPushButton::hover\n"
"  {\n"
"     background-color : lightblue;\n"
"   }")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("TileAutomataSimV1/Icons/save-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SaveAs_button.setIcon(icon)
        self.SaveAs_button.setIconSize(QtCore.QSize(18, 18))
        self.SaveAs_button.setObjectName("SaveAs_button")
        self.verticalLayout_6.addWidget(self.SaveAs_button)
        self.SaveHistory_Button = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SaveHistory_Button.setFont(font)
        self.SaveHistory_Button.setStyleSheet("QPushButton::hover\n"
"  {\n"
"     background-color : lightblue;\n"
"   }")
        self.SaveHistory_Button.setObjectName("SaveHistory_Button")
        self.verticalLayout_6.addWidget(self.SaveHistory_Button)
        self.LoadHistory_Button = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.LoadHistory_Button.setFont(font)
        self.LoadHistory_Button.setStyleSheet("QPushButton::hover\n"
"  {\n"
"     background-color : lightblue;\n"
"   }")
        self.LoadHistory_Button.setObjectName("LoadHistory_Button")
        self.verticalLayout_6.addWidget(self.LoadHistory_Button)
        self.verticalLayout_5.addWidget(self.frame_6, 0, QtCore.Qt.AlignTop)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("TileAutomataSimV1/Icons/document-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page, icon1, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 108, 179))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_7 = QtWidgets.QFrame(self.page_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Edit_button = QtWidgets.QPushButton(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Edit_button.setFont(font)
        self.Edit_button.setStyleSheet("QPushButton::hover\n"
"  {\n"
"     background-color : lightblue;\n"
"   }")
        self.Edit_button.setObjectName("Edit_button")
        self.verticalLayout_8.addWidget(self.Edit_button)
        self.Rotate_button = QtWidgets.QPushButton(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Rotate_button.setFont(font)
        self.Rotate_button.setStyleSheet("QPushButton::hover\n"
"  {\n"
"     background-color : lightblue;\n"
"   }")
        self.Rotate_button.setObjectName("Rotate_button")
        self.verticalLayout_8.addWidget(self.Rotate_button)
        self.Combine_button = QtWidgets.QPushButton(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Combine_button.setFont(font)
        self.Combine_button.setStyleSheet("QPushButton::hover\n"
"  {\n"
"     background-color : lightblue;\n"
"   }")
        self.Combine_button.setObjectName("Combine_button")
        self.verticalLayout_8.addWidget(self.Combine_button)
        self.X_reflect_button = QtWidgets.QPushButton(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.X_reflect_button.setFont(font)
        self.X_reflect_button.setStyleSheet("QPushButton::hover\n"
"  {\n"
"     background-color : lightblue;\n"
"   }")
        self.X_reflect_button.setObjectName("X_reflect_button")
        self.verticalLayout_8.addWidget(self.X_reflect_button)
        self.Y_reflect_button = QtWidgets.QPushButton(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Y_reflect_button.setFont(font)
        self.Y_reflect_button.setStyleSheet("QPushButton::hover\n"
"  {\n"
"     background-color : lightblue;\n"
"   }")
        self.Y_reflect_button.setObjectName("Y_reflect_button")
        self.verticalLayout_8.addWidget(self.Y_reflect_button)
        self.SlowMode_button = QtWidgets.QRadioButton(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SlowMode_button.setFont(font)
        self.SlowMode_button.setObjectName("SlowMode_button")
        self.verticalLayout_8.addWidget(self.SlowMode_button, 0, QtCore.Qt.AlignHCenter)
        self.sCRN_button = QtWidgets.QRadioButton(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sCRN_button.setFont(font)
        self.sCRN_button.setObjectName("sCRN_button")
        self.verticalLayout_8.addWidget(self.sCRN_button, 0, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.frame_7)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 75))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 75))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_8.addWidget(self.label_3)
        self.verticalLayout_7.addWidget(self.frame_7)
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.page_3.setObjectName("page_3")
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.page_4.setObjectName("page_4")
        self.GenShape_Box = QtWidgets.QComboBox(self.page_4)
        self.GenShape_Box.setGeometry(QtCore.QRect(0, 94, 155, 18))
        self.GenShape_Box.setEditable(False)
        self.GenShape_Box.setObjectName("GenShape_Box")
        self.ExampleButton = QtWidgets.QPushButton(self.page_4)
        self.ExampleButton.setGeometry(QtCore.QRect(0, 240, 161, 21))
        self.ExampleButton.setAutoFillBackground(False)
        self.ExampleButton.setStyleSheet("QPushButton::hover\n"
"  {\n"
"     background-color : lightblue;\n"
"   }")
        self.ExampleButton.setAutoDefault(False)
        self.ExampleButton.setDefault(False)
        self.ExampleButton.setFlat(False)
        self.ExampleButton.setObjectName("ExampleButton")
        self.lineEdit = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit.setGeometry(QtCore.QRect(0, 196, 155, 18))
        self.lineEdit.setObjectName("lineEdit")
        self.GenModel_Box = QtWidgets.QComboBox(self.page_4)
        self.GenModel_Box.setGeometry(QtCore.QRect(0, 140, 155, 18))
        self.GenModel_Box.setObjectName("GenModel_Box")
        self.label_4 = QtWidgets.QLabel(self.page_4)
        self.label_4.setGeometry(QtCore.QRect(0, 70, 55, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.page_4)
        self.label_5.setGeometry(QtCore.QRect(0, 120, 55, 16))
        self.label_5.setObjectName("label_5")
        self.InputLabel = QtWidgets.QLabel(self.page_4)
        self.InputLabel.setGeometry(QtCore.QRect(0, 170, 161, 16))
        self.InputLabel.setText("")
        self.InputLabel.setObjectName("InputLabel")
        self.GenPaper_Box = QtWidgets.QComboBox(self.page_4)
        self.GenPaper_Box.setGeometry(QtCore.QRect(0, 40, 155, 18))
        self.GenPaper_Box.setObjectName("GenPaper_Box")
        self.label_6 = QtWidgets.QLabel(self.page_4)
        self.label_6.setGeometry(QtCore.QRect(0, 15, 55, 16))
        self.label_6.setObjectName("label_6")
        self.toolBox.addItem(self.page_4, "")
        self.verticalLayout_4.addWidget(self.toolBox)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.verticalLayout_2.addWidget(self.slide_menu)
        self.horizontalLayout.addWidget(self.slide_menu_container)
        self.main_body = QtWidgets.QFrame(self.centralwidget)
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_body)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.main_body)
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.header)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Menu_button = QtWidgets.QPushButton(self.frame_2)
        self.Menu_button.setStyleSheet("QPushButton::hover\n"
"  {\n"
"     background-color : lightgrey;\n"
"   }")
        self.Menu_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("TileAutomataSimV1/Icons/tabler-icon-align-justified.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Menu_button.setIcon(icon2)
        self.Menu_button.setIconSize(QtCore.QSize(32, 32))
        self.Menu_button.setObjectName("Menu_button")
        self.horizontalLayout_4.addWidget(self.Menu_button)
        self.horizontalLayout_2.addWidget(self.frame_2, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.frame = QtWidgets.QFrame(self.header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.First_button = QtWidgets.QPushButton(self.frame)
        self.First_button.setStyleSheet("QPushButton::hover\n"
"  {\n"
"     background-color : lightgrey;\n"
"   }")
        self.First_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("TileAutomataSimV1/Icons/tabler-icon-player-skip-back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.First_button.setIcon(icon3)
        self.First_button.setObjectName("First_button")
        self.horizontalLayout_6.addWidget(self.First_button)
        self.Prev_button = QtWidgets.QPushButton(self.frame)
        self.Prev_button.setStyleSheet("QPushButton::hover\n"
"  {\n"
"     background-color : lightgrey;\n"
"   }")
        self.Prev_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("TileAutomataSimV1/Icons/tabler-icon-player-track-prev.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Prev_button.setIcon(icon4)
        self.Prev_button.setObjectName("Prev_button")
        self.horizontalLayout_6.addWidget(self.Prev_button)
        self.Play_button = QtWidgets.QPushButton(self.frame)
        self.Play_button.setStyleSheet("QPushButton::hover\n"
"  {\n"
"     background-color : lightgrey;\n"
"   }")
        self.Play_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("TileAutomataSimV1/Icons/tabler-icon-player-play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Play_button.setIcon(icon5)
        self.Play_button.setObjectName("Play_button")
        self.horizontalLayout_6.addWidget(self.Play_button)
        self.Next_button = QtWidgets.QPushButton(self.frame)
        self.Next_button.setStyleSheet("QPushButton::hover\n"
"  {\n"
"     background-color : lightgrey;\n"
"   }")
        self.Next_button.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("TileAutomataSimV1/Icons/tabler-icon-player-track-next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Next_button.setIcon(icon6)
        self.Next_button.setObjectName("Next_button")
        self.horizontalLayout_6.addWidget(self.Next_button)
        self.Last_button = QtWidgets.QPushButton(self.frame)
        self.Last_button.setStyleSheet("QPushButton::hover\n"
"  {\n"
"     background-color : lightgrey;\n"
"   }")
        self.Last_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("TileAutomataSimV1/Icons/tabler-icon-player-skip-forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Last_button.setIcon(icon7)
        self.Last_button.setObjectName("Last_button")
        self.horizontalLayout_6.addWidget(self.Last_button)
        self.horizontalLayout_2.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(self.header)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.minimize_button = QtWidgets.QPushButton(self.frame_3)
        self.minimize_button.setStyleSheet("QPushButton::hover\n"
"  {\n"
"     background-color : lightgrey;\n"
"   }")
        self.minimize_button.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("TileAutomataSimV1/Icons/Programming-Minimize-Window-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize_button.setIcon(icon8)
        self.minimize_button.setIconSize(QtCore.QSize(16, 16))
        self.minimize_button.setObjectName("minimize_button")
        self.horizontalLayout_3.addWidget(self.minimize_button)
        self.maximize_button = QtWidgets.QPushButton(self.frame_3)
        self.maximize_button.setStyleSheet("QPushButton::hover\n"
"  {\n"
"     background-color : lightgrey;\n"
"   }")
        self.maximize_button.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("TileAutomataSimV1/Icons/Programming-Maximize-Window-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.maximize_button.setIcon(icon9)
        self.maximize_button.setIconSize(QtCore.QSize(16, 16))
        self.maximize_button.setObjectName("maximize_button")
        self.horizontalLayout_3.addWidget(self.maximize_button)
        self.close_button = QtWidgets.QPushButton(self.frame_3)
        self.close_button.setStyleSheet("QPushButton::hover\n"
"  {\n"
"     background-color : red;\n"
"   }")
        self.close_button.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("TileAutomataSimV1/Icons/X-icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_button.setIcon(icon10)
        self.close_button.setIconSize(QtCore.QSize(16, 16))
        self.close_button.setObjectName("close_button")
        self.horizontalLayout_3.addWidget(self.close_button)
        self.horizontalLayout_2.addWidget(self.frame_3, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.header, 0, QtCore.Qt.AlignTop)
        self.main_body_contents = QtWidgets.QFrame(self.main_body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_contents.sizePolicy().hasHeightForWidth())
        self.main_body_contents.setSizePolicy(sizePolicy)
        self.main_body_contents.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body_contents.setObjectName("main_body_contents")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.main_body_contents)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label = QtWidgets.QLabel(self.main_body_contents)
        self.label.setObjectName("label")
        self.verticalLayout_9.addWidget(self.label)
        self.frame_8 = QtWidgets.QFrame(self.main_body_contents)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setLineWidth(0)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.sizeDrag_Button = QtWidgets.QPushButton(self.frame_8)
        self.sizeDrag_Button.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("TileAutomataSimV1/Icons/tabler-icon-resize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sizeDrag_Button.setIcon(icon11)
        self.sizeDrag_Button.setIconSize(QtCore.QSize(10, 10))
        self.sizeDrag_Button.setObjectName("sizeDrag_Button")
        self.horizontalLayout_7.addWidget(self.sizeDrag_Button)
        self.verticalLayout_9.addWidget(self.frame_8, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.main_body_contents)
        self.horizontalLayout.addWidget(self.main_body)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title_label.setText(_translate("MainWindow", "    AutoTile"))
        self.New_button.setText(_translate("MainWindow", "New"))
        self.Load_button.setText(_translate("MainWindow", "Load"))
        self.seededLoadButton.setText(_translate("MainWindow", "Load Assembly"))
        self.SaveAs_button.setText(_translate("MainWindow", "Save As ..."))
        self.SaveHistory_Button.setText(_translate("MainWindow", "Save History"))
        self.LoadHistory_Button.setText(_translate("MainWindow", "Load History"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("MainWindow", "File"))
        self.Edit_button.setText(_translate("MainWindow", "Edit"))
        self.Rotate_button.setText(_translate("MainWindow", "Rotate"))
        self.Combine_button.setText(_translate("MainWindow", "Combine"))
        self.X_reflect_button.setText(_translate("MainWindow", "X-Reflect"))
        self.Y_reflect_button.setText(_translate("MainWindow", "Y-Reflect"))
        self.SlowMode_button.setText(_translate("MainWindow", "Slow Mode"))
        self.sCRN_button.setText(_translate("MainWindow", "sCRN Mode"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("MainWindow", "Tools"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("MainWindow", "Available Moves"))
        self.ExampleButton.setText(_translate("MainWindow", "Enter"))
        self.label_4.setText(_translate("MainWindow", "Shape:"))
        self.label_5.setText(_translate("MainWindow", "Model:"))
        self.label_6.setText(_translate("MainWindow", "Paper:"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("MainWindow", "Examples"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
