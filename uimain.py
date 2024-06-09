# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
@contact: 微信 1257309054
@file: main.py
@time: 2022/5/19 10:15
@author: LDC
"""
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from Myui import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self) # 渲染页面控件
        self.connect_signals() # 设置信号槽

    def connect_signals(self):
      self.btn_sure_clicked() # 绑定确定按钮事件
      self.btn_cancel_clicked()# 绑定取消按钮时间

    def btn_sure_clicked(self):
        self.showFullScreen()# 点击确定按钮显示hello world

    def btn_cancel_clicked(self):
        self.show()# 点击取消按钮清空显示框

def main():
    app = QApplication(sys.argv)
    mywindow = Window()
    mywindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
