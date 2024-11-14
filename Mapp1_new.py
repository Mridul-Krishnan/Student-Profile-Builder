# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mapp1.py'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import webbrowser

from tfidf import find_index
df_2=pd.read_csv('articles2.csv')
print(df_2.iloc[1])

class Ui_MainWindow(object):
	
	def table_update(self):
		print("update table")
		b=[]
		df_2=pd.read_csv('articles2.csv')
		for i in range(0,100):
			self.tableWidget_2.setItem(i,0, QtWidgets.QTableWidgetItem(df_2.iloc[i][0]))
			#header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
			b.append(self.make_button(i))
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
		b=[]
		for i in range(0,100):
			self.tableWidget_2.setItem(i,0, QtWidgets.QTableWidgetItem(df_2.iloc[i][0]))
			#header.setSectionResizeMode(i, QtWidgets.QHeaderView.ResizeToContents)
			b.append(self.make_button(i))
			'''btn.append(QtWidgets.QPushButton('Go to course'))
			btn[-1].clicked.connect(lambda j=i: self.tag_update(df_2.iloc[int(j)][1]))
			self.tableWidget_2.setCellWidget(i,1, btn[-1])'''
		self.tableWidget_2.setObjectName("tableWidget_2")
		
	
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(752, 599)
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout_2.setObjectName("gridLayout_2")
		
		self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
		self.tabWidget.setObjectName("tabWidget")
		
		self.tab_2 = QtWidgets.QWidget()
		self.tab_2.setObjectName("tab_2")
		
		self.gridLayout = QtWidgets.QGridLayout(self.tab_2)
		self.gridLayout.setObjectName("gridLayout")
		self.tabledata()
		self.verticalLayout_4 = QtWidgets.QVBoxLayout()
		self.verticalLayout_4.setObjectName("verticalLayout_4")
		
		
		self.verticalLayout_4.addWidget(self.tableWidget_2)
		
		
		self.pushButton = QtWidgets.QPushButton(self.tab_2)
		self.pushButton.setObjectName("PushButton")
		
		self.pushButton.clicked.connect(self.table_update)	
		
		self.verticalLayout_4.addWidget(self.pushButton)
		self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
		self.tabWidget.addTab(self.tab_2, "")
		
		
		"""self.tab_6 = QtWidgets.QWidget()
		self.tab_6.setObjectName("tab_6")
		self.tabWidget.addTab(self.tab_6, "")"""
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
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Articles"))
	def tag_update(self,link):
		find_index(link)
		webbrowser.open(link)
		#self.tableWidget_2.update()

	def make_button(self,i):
		btn=QtWidgets.QPushButton('Go to link')
		btn.clicked.connect(lambda j=i: self.tag_update(df_2.iloc[int(i)][1]))
		self.tableWidget_2.setCellWidget(i,1, btn)
		return btn
		


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
