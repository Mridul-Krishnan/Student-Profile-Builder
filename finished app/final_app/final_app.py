# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
#import mooc_rupdate as mr 
import mooc_tupdate as mt3
import vid_recomm as mt1
import webbrowser
from tfidf import find_index

df_2=pd.read_csv('articles2.csv')
print(df_2.iloc[1])

df_11=pd.read_csv('dfr.csv')

df_3=pd.read_csv('recommend_course.csv')
if list(df_11.columns.values)[0]=='index':
    df_11=df_11.drop(['index'],axis=1)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(752, 599)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_ = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_.setObjectName("gridLayout_")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        ###################################################################################

        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.gridLayout_1 = QtWidgets.QGridLayout(self.tab_1)
        self.gridLayout_1.setObjectName("gridLayout_1")
        self.verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.tableWidget_1 = QtWidgets.QTableWidget(self.tab_1)
        self.tableWidget_1.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_1.setColumnCount(2)
        self.tableWidget_1.setRowCount(50)
        header = self.tableWidget_1.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header = self.tableWidget_1.verticalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        b1=[]
        for i in range(0,50):
            self.tableWidget_1.setItem(i,0, QtWidgets.QTableWidgetItem(df_11.iloc[i][1]))
            b1.append(self.make_button_1(i))
            
        self.tableWidget_1.setObjectName("tableWidget_1")
        self.verticalLayout_1.addWidget(self.tableWidget_1)
        self.pushButton_1 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_1.setObjectName("PushButton")
        self.pushButton_1.clicked.connect(self.table_update_1)
        self.verticalLayout_1.addWidget(self.pushButton_1)
        self.gridLayout_1.addLayout(self.verticalLayout_1, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_1, "")
        ###################################################################################

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabledata()
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        
        self.verticalLayout_2.addWidget(self.tableWidget_2)
        
        
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setObjectName("PushButton")
        
        self.pushButton.clicked.connect(self.table_update_2)    
        
        self.verticalLayout_2.addWidget(self.pushButton)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        


        ###################################################################################
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget_3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setRowCount(100)
        header = self.tableWidget_3.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header = self.tableWidget_3.verticalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        b3=[]
        for i in range(0,100):
            self.tableWidget_3.setItem(i,0, QtWidgets.QTableWidgetItem(df_3.iloc[i][0]))
            b3.append(self.make_button_3(i))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.verticalLayout_3.addWidget(self.tableWidget_3)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setObjectName("PushButton")
        self.pushButton_3.clicked.connect(self.table_update_3)
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        #####################################################################################################
        self.gridLayout_.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_.addLayout(self.verticalLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 752, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #for launcher purpose
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.table_update_1()
        self.table_update_2()
        self.table_update_3()
        self.retranslateUi(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "Update"))
        self.pushButton.setText(_translate("MainWindow", "Update"))
        self.pushButton_1.setText(_translate("MainWindow", "Update"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Videos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Articles"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Courses"))
    
    def tag_update_1(self,link):
        mt1.tupdate(link)
        self.tableWidget_1.update()
    def table_update_1(self):
        
        b1=[]
        df_11 = pd.read_csv('dfr.csv')
        if list(df_11.columns.values)[0]=='index':
            df_11=df_11.drop(['index'],axis=1)
        for i in range(0,50):
            self.tableWidget_1.setItem(i,0, QtWidgets.QTableWidgetItem(df_11.iloc[i][1]))
            #header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
            b1.append(self.make_button_1(i))
        print("table updated")
    def make_button_1(self,i):
        btn=QtWidgets.QPushButton('Watch Video')
        btn.clicked.connect(lambda j=i: self.tag_update_1(df_11.iloc[int(i)][4]))
        self.tableWidget_1.setCellWidget(i,1, btn)
        return btn
###########################################################################################

    def table_update_2(self):
        print("update table")
        b2=[]
        global df_2
        df_2=pd.read_csv('articles2.csv')
        for i in range(0,100):
            self.tableWidget_2.setItem(i,0, QtWidgets.QTableWidgetItem(df_2.iloc[i][0]))
            #header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
            b2.append(self.make_button_2(i))
    def tabledata(self):
        print("table data")
        
        self.tableWidget_2 = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(100)
        
        
        header = self.tableWidget_2.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        
        header = self.tableWidget_2.verticalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        b2=[]
        for i in range(0,100):
            self.tableWidget_2.setItem(i,0, QtWidgets.QTableWidgetItem(df_2.iloc[i][0]))
            #header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
            b2.append(self.make_button_2(i))
            '''btn.append(QtWidgets.QPushButton('Go to course'))
            btn[-1].clicked.connect(lambda j=i: self.tag_update_2(df_2.iloc[int(j)][1]))
            self.tableWidget_2.setCellWidget(i,1, btn[-1])'''
        self.tableWidget_2.setObjectName("tableWidget_2")
        
    def tag_update_2(self,link):
        webbrowser.open(link)
        find_index(link)
        
        #self.tableWidget_2.update()

    def make_button_2(self,i):
        btn=QtWidgets.QPushButton('Go to link')
        btn.clicked.connect(lambda j=i: self.tag_update_2(df_2.iloc[int(i)][1]))
        self.tableWidget_2.setCellWidget(i,1, btn)
        return btn


#########################################################################################
    def tag_update_3(self,link):
        mt3.tupdate(link)
        self.tableWidget_3.update()

    def table_update_3(self):
        b3=[]
        print('course table updating')
        #mr.mooc_update()
        df_3=pd.read_csv('recommend_course.csv')
        for i in range(0,100):
            self.tableWidget_3.setItem(i,0, QtWidgets.QTableWidgetItem(df_3.iloc[i][0]))
            b3.append(self.make_button_3(i))
        print("course table updated") 

    def make_button_3(self,i):
        btn=QtWidgets.QPushButton('Go to course')
        btn.clicked.connect(lambda j=i: self.tag_update_3(df_3.iloc[int(i)][1]))
        self.tableWidget_3.setCellWidget(i,1, btn)
        return btn


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
