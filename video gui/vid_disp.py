# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
#import mooc_rupdate as mr 
import vid_recomm as mt
df=pd.read_csv('dfr.csv')

if list(df.columns.values)[0]=='index':
    df=df.drop(['index'],axis=1)
class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(752, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_5)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(50)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header = self.tableWidget.verticalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        b=[]
        for i in range(0,50):
            self.tableWidget.setItem(i,0, QtWidgets.QTableWidgetItem(df.iloc[i][1]))
            #header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
            b.append(self.make_button(i))
            '''btn.append(QtWidgets.QPushButton('Go to course'))
            btn[-1].clicked.connect(lambda j=i: self.tag_update(df.iloc[int(j)][1]))
            self.tableWidget.setCellWidget(i,1, btn[-1])'''
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.pushButton = QtWidgets.QPushButton(self.tab_5)
        self.pushButton.setObjectName("PushButton")
        self.pushButton.clicked.connect(self.table_update)
        self.verticalLayout_4.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 752, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Update"))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Tab 2"))

    def tag_update(self,link):
        mt.tupdate(link)
        self.tableWidget.update()
    def table_update(self):
        
        b=[]
        df2 = pd.read_csv('dfr.csv')
        df2=df2.drop(['index'],axis=1)
        for i in range(0,50):
            self.tableWidget.setItem(i,0, QtWidgets.QTableWidgetItem(df2.iloc[i][1]))
            #header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
            b.append(self.make_button(i))
        print("table updated")
    def make_button(self,i):
        btn=QtWidgets.QPushButton('Watch Video')
        btn.clicked.connect(lambda j=i: self.tag_update(df.iloc[int(i)][4]))
        self.tableWidget.setCellWidget(i,1, btn)
        return btn


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
