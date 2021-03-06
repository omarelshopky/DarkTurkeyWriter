# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Designer UI/optionWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_optionWindow(object):
    def setupUi(self, optionWindow):
        optionWindow.setObjectName("optionWindow")
        optionWindow.resize(1033, 709)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 243, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 243, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 243, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(241, 243, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        optionWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        optionWindow.setFont(font)
        optionWindow.setAnimated(True)
        optionWindow.setDocumentMode(False)
        optionWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(optionWindow)
        self.centralwidget.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.centralLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.centralLayout.setObjectName("centralLayout")
        self.mainLayoutH = QtWidgets.QHBoxLayout()
        self.mainLayoutH.setObjectName("mainLayoutH")
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.mainLayoutH.addItem(spacerItem)
        self.centerLayoutV = QtWidgets.QVBoxLayout()
        self.centerLayoutV.setObjectName("centerLayoutV")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.centerLayoutV.addItem(spacerItem1)
        self.titleLayoutH = QtWidgets.QHBoxLayout()
        self.titleLayoutH.setObjectName("titleLayoutH")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.titleLayoutH.addItem(spacerItem2)
        self.titleLblL = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(62, 91, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 91, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.titleLblL.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.titleLblL.setFont(font)
        self.titleLblL.setTextFormat(QtCore.Qt.RichText)
        self.titleLblL.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.titleLblL.setWordWrap(False)
        self.titleLblL.setObjectName("titleLblL")
        self.titleLayoutH.addWidget(self.titleLblL)
        self.titleLblR = QtWidgets.QLabel(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(62, 91, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(62, 91, 105))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.titleLblR.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.titleLblR.setFont(font)
        self.titleLblR.setObjectName("titleLblR")
        self.titleLayoutH.addWidget(self.titleLblR)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.titleLayoutH.addItem(spacerItem3)
        self.centerLayoutV.addLayout(self.titleLayoutH)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.centerLayoutV.addItem(spacerItem4)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.tabWidget.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabletTracking(False)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("\n"
"\n"
"QTabWidget::tab-bar:top {\n"
"    top: 1px;\n"
"    left: 2px\n"
"}")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(100, 40))
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.newDraftTab = QtWidgets.QWidget()
        self.newDraftTab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.newDraftTab.setObjectName("newDraftTab")
        self.ndCentralLayout = QtWidgets.QVBoxLayout(self.newDraftTab)
        self.ndCentralLayout.setObjectName("ndCentralLayout")
        self.ndMainLayoutV = QtWidgets.QVBoxLayout()
        self.ndMainLayoutV.setSpacing(0)
        self.ndMainLayoutV.setObjectName("ndMainLayoutV")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ndMainLayoutV.addItem(spacerItem5)
        self.ndLbl1 = QtWidgets.QLabel(self.newDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ndLbl1.setFont(font)
        self.ndLbl1.setAlignment(QtCore.Qt.AlignCenter)
        self.ndLbl1.setObjectName("ndLbl1")
        self.ndMainLayoutV.addWidget(self.ndLbl1)
        self.ndLbl2 = QtWidgets.QLabel(self.newDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ndLbl2.setFont(font)
        self.ndLbl2.setAlignment(QtCore.Qt.AlignCenter)
        self.ndLbl2.setObjectName("ndLbl2")
        self.ndMainLayoutV.addWidget(self.ndLbl2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ndMainLayoutV.addItem(spacerItem6)
        self.ndBlockInputLayoutH = QtWidgets.QHBoxLayout()
        self.ndBlockInputLayoutH.setObjectName("ndBlockInputLayoutH")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ndBlockInputLayoutH.addItem(spacerItem7)
        self.ndBlockInputLbl = QtWidgets.QLabel(self.newDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ndBlockInputLbl.setFont(font)
        self.ndBlockInputLbl.setObjectName("ndBlockInputLbl")
        self.ndBlockInputLayoutH.addWidget(self.ndBlockInputLbl)
        self.ndBlockInput = QtWidgets.QLineEdit(self.newDraftTab)
        self.ndBlockInput.setFrame(True)
        self.ndBlockInput.setObjectName("ndBlockInput")
        self.ndBlockInputLayoutH.addWidget(self.ndBlockInput)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ndBlockInputLayoutH.addItem(spacerItem8)
        self.ndBlockInputLayoutH.setStretch(0, 5)
        self.ndBlockInputLayoutH.setStretch(1, 4)
        self.ndBlockInputLayoutH.setStretch(2, 2)
        self.ndBlockInputLayoutH.setStretch(3, 5)
        self.ndMainLayoutV.addLayout(self.ndBlockInputLayoutH)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ndMainLayoutV.addItem(spacerItem9)
        self.ndBlockInputLayoutH_3 = QtWidgets.QHBoxLayout()
        self.ndBlockInputLayoutH_3.setObjectName("ndBlockInputLayoutH_3")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ndBlockInputLayoutH_3.addItem(spacerItem10)
        self.ndRadioLayoutV = QtWidgets.QVBoxLayout()
        self.ndRadioLayoutV.setObjectName("ndRadioLayoutV")
        self.ndWordRadioBtn = QtWidgets.QRadioButton(self.newDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ndWordRadioBtn.setFont(font)
        self.ndWordRadioBtn.setChecked(True)
        self.ndWordRadioBtn.setObjectName("ndWordRadioBtn")
        self.ndRadioLayoutV.addWidget(self.ndWordRadioBtn)
        self.ndMntRadioBtn = QtWidgets.QRadioButton(self.newDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ndMntRadioBtn.setFont(font)
        self.ndMntRadioBtn.setChecked(False)
        self.ndMntRadioBtn.setObjectName("ndMntRadioBtn")
        self.ndRadioLayoutV.addWidget(self.ndMntRadioBtn)
        self.ndFreeRadioBtn = QtWidgets.QRadioButton(self.newDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ndFreeRadioBtn.setFont(font)
        self.ndFreeRadioBtn.setChecked(False)
        self.ndFreeRadioBtn.setObjectName("ndFreeRadioBtn")
        self.ndRadioLayoutV.addWidget(self.ndFreeRadioBtn)
        self.ndBlockInputLayoutH_3.addLayout(self.ndRadioLayoutV)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ndBlockInputLayoutH_3.addItem(spacerItem11)
        self.ndBlockInputLayoutH_3.setStretch(0, 5)
        self.ndBlockInputLayoutH_3.setStretch(2, 5)
        self.ndMainLayoutV.addLayout(self.ndBlockInputLayoutH_3)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ndMainLayoutV.addItem(spacerItem12)
        self.ndBtnLayoutH = QtWidgets.QHBoxLayout()
        self.ndBtnLayoutH.setObjectName("ndBtnLayoutH")
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ndBtnLayoutH.addItem(spacerItem13)
        self.ndQuitBtn = QtWidgets.QPushButton(self.newDraftTab)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.ndQuitBtn.setFont(font)
        self.ndQuitBtn.setObjectName("ndQuitBtn")
        self.ndBtnLayoutH.addWidget(self.ndQuitBtn)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ndBtnLayoutH.addItem(spacerItem14)
        self.ndStartBtn = QtWidgets.QPushButton(self.newDraftTab)
        self.ndStartBtn.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.ndStartBtn.setFont(font)
        self.ndStartBtn.setObjectName("ndStartBtn")
        self.ndBtnLayoutH.addWidget(self.ndStartBtn)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ndBtnLayoutH.addItem(spacerItem15)
        self.ndBtnLayoutH.setStretch(0, 6)
        self.ndBtnLayoutH.setStretch(4, 6)
        self.ndMainLayoutV.addLayout(self.ndBtnLayoutH)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ndMainLayoutV.addItem(spacerItem16)
        self.ndMainLayoutV.setStretch(4, 7)
        self.ndMainLayoutV.setStretch(6, 7)
        self.ndMainLayoutV.setStretch(8, 7)
        self.ndCentralLayout.addLayout(self.ndMainLayoutV)
        self.tabWidget.addTab(self.newDraftTab, "")
        self.openDraftTab = QtWidgets.QWidget()
        self.openDraftTab.setObjectName("openDraftTab")
        self.odCentralLayout = QtWidgets.QHBoxLayout(self.openDraftTab)
        self.odCentralLayout.setObjectName("odCentralLayout")
        self.odMainLayoutH = QtWidgets.QVBoxLayout()
        self.odMainLayoutH.setSpacing(0)
        self.odMainLayoutH.setObjectName("odMainLayoutH")
        spacerItem17 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.odMainLayoutH.addItem(spacerItem17)
        self.odFileLayout = QtWidgets.QHBoxLayout()
        self.odFileLayout.setObjectName("odFileLayout")
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.odFileLayout.addItem(spacerItem18)
        self.odFilePathTxt = QtWidgets.QLineEdit(self.openDraftTab)
        self.odFilePathTxt.setReadOnly(True)
        self.odFilePathTxt.setObjectName("odFilePathTxt")
        self.odFileLayout.addWidget(self.odFilePathTxt)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.odFileLayout.addItem(spacerItem19)
        self.odBrowseBtn = QtWidgets.QPushButton(self.openDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.odBrowseBtn.setFont(font)
        self.odBrowseBtn.setObjectName("odBrowseBtn")
        self.odFileLayout.addWidget(self.odBrowseBtn)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.odFileLayout.addItem(spacerItem20)
        self.odFileLayout.setStretch(0, 2)
        self.odFileLayout.setStretch(1, 10)
        self.odFileLayout.setStretch(2, 1)
        self.odFileLayout.setStretch(3, 3)
        self.odFileLayout.setStretch(4, 2)
        self.odMainLayoutH.addLayout(self.odFileLayout)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.odMainLayoutH.addItem(spacerItem21)
        self.odBlockInputLayoutH = QtWidgets.QHBoxLayout()
        self.odBlockInputLayoutH.setObjectName("odBlockInputLayoutH")
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.odBlockInputLayoutH.addItem(spacerItem22)
        self.odBlockInputLbl = QtWidgets.QLabel(self.openDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.odBlockInputLbl.setFont(font)
        self.odBlockInputLbl.setObjectName("odBlockInputLbl")
        self.odBlockInputLayoutH.addWidget(self.odBlockInputLbl)
        self.odBlockInput = QtWidgets.QLineEdit(self.openDraftTab)
        self.odBlockInput.setFrame(True)
        self.odBlockInput.setObjectName("odBlockInput")
        self.odBlockInputLayoutH.addWidget(self.odBlockInput)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.odBlockInputLayoutH.addItem(spacerItem23)
        self.odBlockInputLayoutH.setStretch(0, 5)
        self.odBlockInputLayoutH.setStretch(1, 4)
        self.odBlockInputLayoutH.setStretch(2, 2)
        self.odBlockInputLayoutH.setStretch(3, 5)
        self.odMainLayoutH.addLayout(self.odBlockInputLayoutH)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.odMainLayoutH.addItem(spacerItem24)
        self.odBlockInputLayoutH_2 = QtWidgets.QHBoxLayout()
        self.odBlockInputLayoutH_2.setObjectName("odBlockInputLayoutH_2")
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.odBlockInputLayoutH_2.addItem(spacerItem25)
        self.odRadioLayoutV = QtWidgets.QVBoxLayout()
        self.odRadioLayoutV.setObjectName("odRadioLayoutV")
        self.odWordRadioBtn = QtWidgets.QRadioButton(self.openDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.odWordRadioBtn.setFont(font)
        self.odWordRadioBtn.setChecked(True)
        self.odWordRadioBtn.setObjectName("odWordRadioBtn")
        self.odRadioLayoutV.addWidget(self.odWordRadioBtn)
        self.odMntRadioBtn = QtWidgets.QRadioButton(self.openDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.odMntRadioBtn.setFont(font)
        self.odMntRadioBtn.setChecked(False)
        self.odMntRadioBtn.setObjectName("odMntRadioBtn")
        self.odRadioLayoutV.addWidget(self.odMntRadioBtn)
        self.odFreeRadioBtn = QtWidgets.QRadioButton(self.openDraftTab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.odFreeRadioBtn.setFont(font)
        self.odFreeRadioBtn.setChecked(False)
        self.odFreeRadioBtn.setObjectName("odFreeRadioBtn")
        self.odRadioLayoutV.addWidget(self.odFreeRadioBtn)
        self.odBlockInputLayoutH_2.addLayout(self.odRadioLayoutV)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.odBlockInputLayoutH_2.addItem(spacerItem26)
        self.odBlockInputLayoutH_2.setStretch(0, 5)
        self.odBlockInputLayoutH_2.setStretch(2, 5)
        self.odMainLayoutH.addLayout(self.odBlockInputLayoutH_2)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.odMainLayoutH.addItem(spacerItem27)
        self.odBtnLayoutH = QtWidgets.QHBoxLayout()
        self.odBtnLayoutH.setObjectName("odBtnLayoutH")
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.odBtnLayoutH.addItem(spacerItem28)
        self.odQuitBtn = QtWidgets.QPushButton(self.openDraftTab)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.odQuitBtn.setFont(font)
        self.odQuitBtn.setObjectName("odQuitBtn")
        self.odBtnLayoutH.addWidget(self.odQuitBtn)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.odBtnLayoutH.addItem(spacerItem29)
        self.odStartBtn = QtWidgets.QPushButton(self.openDraftTab)
        self.odStartBtn.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(9)
        self.odStartBtn.setFont(font)
        self.odStartBtn.setObjectName("odStartBtn")
        self.odBtnLayoutH.addWidget(self.odStartBtn)
        spacerItem30 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.odBtnLayoutH.addItem(spacerItem30)
        self.odBtnLayoutH.setStretch(0, 6)
        self.odBtnLayoutH.setStretch(4, 6)
        self.odMainLayoutH.addLayout(self.odBtnLayoutH)
        spacerItem31 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.odMainLayoutH.addItem(spacerItem31)
        self.odMainLayoutH.setStretch(3, 7)
        self.odMainLayoutH.setStretch(5, 7)
        self.odMainLayoutH.setStretch(7, 7)
        self.odCentralLayout.addLayout(self.odMainLayoutH)
        self.tabWidget.addTab(self.openDraftTab, "")
        self.centerLayoutV.addWidget(self.tabWidget)
        spacerItem32 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.centerLayoutV.addItem(spacerItem32)
        self.centerLayoutV.setStretch(1, 1)
        self.centerLayoutV.setStretch(2, 5)
        self.centerLayoutV.setStretch(3, 8)
        self.centerLayoutV.setStretch(4, 9)
        self.mainLayoutH.addLayout(self.centerLayoutV)
        spacerItem33 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.mainLayoutH.addItem(spacerItem33)
        self.mainLayoutH.setStretch(0, 5)
        self.mainLayoutH.setStretch(1, 4)
        self.mainLayoutH.setStretch(2, 5)
        self.centralLayout.addLayout(self.mainLayoutH)
        optionWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(optionWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(optionWindow)

    def retranslateUi(self, optionWindow):
        _translate = QtCore.QCoreApplication.translate
        optionWindow.setWindowTitle(_translate("optionWindow", "optionWindow"))
        self.titleLblL.setText(_translate("optionWindow", "KEYBOARD"))
        self.titleLblR.setText(_translate("optionWindow", "COWBOY"))
        self.ndLbl1.setText(_translate("optionWindow", "You\'ll be able to save your work when you finish."))
        self.ndLbl2.setText(_translate("optionWindow", "Periodic auto-saves are stored in your \"My Documents\" folder."))
        self.ndBlockInputLbl.setText(_translate("optionWindow", "Block everthing until:"))
        self.ndWordRadioBtn.setText(_translate("optionWindow", "Words are typed."))
        self.ndMntRadioBtn.setText(_translate("optionWindow", "Minutes from now."))
        self.ndFreeRadioBtn.setText(_translate("optionWindow", "Don\'t block me."))
        self.ndQuitBtn.setText(_translate("optionWindow", "Quit"))
        self.ndStartBtn.setText(_translate("optionWindow", "Start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.newDraftTab), _translate("optionWindow", "                 New Draft                  "))
        self.odBrowseBtn.setText(_translate("optionWindow", "Browse..."))
        self.odBlockInputLbl.setText(_translate("optionWindow", "Block everthing until:"))
        self.odWordRadioBtn.setText(_translate("optionWindow", "Words are typed."))
        self.odMntRadioBtn.setText(_translate("optionWindow", "Minutes from now."))
        self.odFreeRadioBtn.setText(_translate("optionWindow", "Don\'t block me."))
        self.odQuitBtn.setText(_translate("optionWindow", "Quit"))
        self.odStartBtn.setText(_translate("optionWindow", "Start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.openDraftTab), _translate("optionWindow", "                 Open Draft                  "))
