# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'video.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QTableView
import pandas as pd
import operator
#from vid_recomm import Ui_MainWindow
#import vid_recomm 
#from UI_MainWindow import Ui_MainWindow

class Ui_Dialog(QtWidgets.QMainWindow):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(696, 556)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(10, -10, 681, 561))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 671, 541))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(310, 100, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(310, 60, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(160, 70, 131, 20))
        self.label.setObjectName("label")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Display"))
        self.comboBox.setItemText(0, _translate("Dialog", "Machine Learning"))
        self.comboBox.setItemText(1, _translate("Dialog", "Web Development"))
        self.comboBox.setItemText(2, _translate("Dialog", "Cybersecurity"))
        self.comboBox.setItemText(3, _translate("Dialog", "Data Science"))
        self.comboBox.setItemText(4, _translate("Dialog", "AI"))
        self.label.setWhatsThis(_translate(
            "Dialog", "<html><head/><body><p>Choose a domain</p><p><br/></p></body></html>"))
        self.label.setText(_translate(
            "Dialog", "<html><head/><body><p><span style=\" font-size:12pt;\">Choose a Domain</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab), _translate("Dialog", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tab_2), _translate("Dialog", "Tab 2"))
        self.pushButton.clicked.connect(self.disp)

    def disp(self):
        option = self.comboBox.currentText()
        df = pd.read_csv(
            r"C:\Users\Akshay\Desktop\Minor Proj\DATASETS\df.csv")
        if option == 'Machine Learning':
            z = df[df['category'].str.contains("Machine Learning")].sort_values(by=[
                'rating'], ascending=False)
            z.to_csv('dfr.csv',index=False)
        if option == 'AI':
            z = df[df['category'].str.contains("AI")].sort_values(
                by=['rating'], ascending=False)
            z.to_csv('dfr.csv',index=False)
        if option == 'Web Development':
            z = df[df['category'].str.contains("Web Development")].sort_values(by=[
                'rating'], ascending=False)
            z.to_csv('dfr.csv',index=False)
        if option == 'Cybersecurity':
            z = df[df['category'].str.contains("Cybersecurity")].sort_values(by=[
                'rating'], ascending=False)
            z.to_csv('dfr.csv',index=False)
        if option == 'Data Science':
            z = df[df['category'].str.contains("Data Science")].sort_values(by=[
                'rating'], ascending=False)
            z.to_csv('dfr.csv',index=False)
        
        # self.hide()
        # print('hide executed')
        # app = QtWidgets.QApplication(sys.argv)
        # self.MainWindow = QtWidgets.QMainWindow()
        # ui = Ui_MainWindow()

        # self.MainWindow.show()
       


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
