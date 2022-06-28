# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 18:23:42 2022

@author: pieroot
"""

from deepface import DeepFace

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QDesktopWidget, QVBoxLayout, QLabel, QFileDialog
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


import urllib.request

# from camera import Camera

import sys
import os

from tkinter import filedialog
from tkinter import messagebox

from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


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

        select_img1 = QPushButton('원본 이미지 선택', self)
        # select_img1.setFont()
        select_img1.move(30, 5)
        select_img1.resize(select_img1.sizeHint())
        # select_img1.clicked.connect(self.setIMG())

        select_img2 = QPushButton('비교할 이미지 선택', self)
        # select_img2.setFont()
        select_img2.move(170, 5)
        select_img2.resize(select_img1.sizeHint())
        # select_img2.clicked.connect(self)

        self.setWindowTitle('Face Project!!')
        self.setWindowIcon(QIcon('deepface-icon.png'))
        # self.move(300, 300)
        self.resize(700, 500)
        self.setIMG()
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setIMG(self):
        pixmap1 = QPixmap('C:\\code\\python\\face\\img1.jpg')
        lbl_img1 = QLabel()
        # pixmap1 = pixmap1.scaledToWidth(80)
        pixmap1 = pixmap1.scaledToHeight(360)
        lbl_img1.setPixmap(pixmap1)

        pixmap2 = QPixmap('img2.jpg')
        lbl_img2 = QLabel()
        # pixmap2 = pixmap2.scaledToWidth(80)
        pixmap2 = pixmap2.scaledToHeight(120)
        lbl_img2.setPixmap(pixmap2)

        lbl_size = QLabel('Width: ' + str(pixmap1.width()) + ', Height: ' + str(pixmap1.height()))
        lbl_size.setAlignment(Qt.AlignCenter)

        vbox = QVBoxLayout()
        lbl_img1.move(530, 530)
        vbox.addWidget(lbl_img1)
        vbox.addWidget(lbl_size)
        self.setLayout(vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
