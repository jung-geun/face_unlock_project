# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 18:23:42 2022

@author: jgbon
"""

from deepface import DeepFace
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from camera import Camera
import os
from tkinter import filedialog
from tkinter import messagebox


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Quit', self)
        # btn.setFont('<b>exit</b>')
        btn.move(320, 5)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        img1_btn = QPushButton('이미지 선택', self)
        # img1_btn.setFont()
        img1_btn.resize(img1_btn.sizeHint())

        self.setWindowTitle('Face Project!!')
        self.setWindowIcon(QIcon('deepface-icon.png'))
        self.move(300, 300)
        self.resize(400, 200)
        self.show()

    def setIMG(self):
        img1_name = "img1.jpg"
        img2_name = "null"
        list_file = []  # 파일 목록 담을 리스트 생성
        files = filedialog.askopenfilenames(initialdir="/", title="파일을 선택 해 주세요", filetypes=(("*.xlsx", "*xlsx"), ("*.xls", "*xls"), ("*.csv", "*csv")))
        result = DeepFace.verify(img1_path="img1.jpg", img2_path="img2.jpg")
        print(result)


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())