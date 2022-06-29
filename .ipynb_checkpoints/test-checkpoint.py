# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 18:23:42 2022

@author: pieroot
"""

from deepface import DeepFace

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QDesktopWidget, QVBoxLayout, QHBoxLayout, QLabel, QFileDialog, QProgressBar, QMainWindow, QMessageBox
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import QCoreApplication, QBasicTimer, Qt
from PyQt5 import uic

form_class = uic.loadUiType("ui_test.ui")[0]

import sys
import os

class MyApp(QMainWindow, form_class):
    pixmap1_path = ""
    pixmap2_path = ""

    def __init__(self):
        QMainWindow.__init__(self)
        # 연결한 Ui를 준비한다.
        self.setupUi(self)
        self.initUI()
        # 화면을 보여준다.
        self.show()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>Face unlock</b> widget')
        self.setWindowTitle('Face Project!!')
        self.setWindowIcon(QIcon('deepface-icon.png'))

        self.push_compare.clicked.connect(self.compare_btn_clicked)

        self.setIMG()
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def ref_FileLoad(self):
        img1_fname = QFileDialog.getOpenFileName(self)
        print(img1_fname[0])
        self.pixmap1_path = img1_fname[0]
        pixmap1 = QPixmap(img1_fname[0])
        pixmap1 = pixmap1.scaledToHeight(261)
        # self.lbl_size1 = QLabel('img1 Width: ' + str(pixmap1.width()) + ', Height: ' + str(pixmap1.height()))
        self.img_ref.setPixmap(pixmap1)
        # self.lbl_size1.setAlignment(Qt.AlignCenter)
        print(img1_fname[1])

    def cmp_FileLoad(self):
        img2_fname = QFileDialog.getOpenFileName(self)
        print(img2_fname[0])
        self.pixmap2_path = img2_fname[0]
        pixmap2 = QPixmap(img2_fname[0])
        pixmap2 = pixmap2.scaledToHeight(261)
        # self.lbl_size2 = QLabel('img2 Width: ' + str(pixmap2.width()) + ', Height: ' + str(pixmap2.height()))
        self.img_cmp.setPixmap(pixmap2)
        # self.lbl_size2.setAlignment(Qt.AlignCenter)
        print(img2_fname[0])

    def compare_btn_clicked(self):
        if(self.pixmap1_path != "" and self.pixmap2_path != ""):
            result = DeepFace.verify(img1_path=self.pixmap1_path, img2_path=self.pixmap2_path)
            print(result)
            verified = result['verified']
            print(verified)
            self.match_rate.setText("일치율 : " + str(verified))

        else:
            QMessageBox.about(self, 'Warnnig!!', '이미지를 선택하시오')

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def setIMG(self):
        self.push_ref.clicked.connect(self.ref_FileLoad)
        self.push_cmp.clicked.connect(self.cmp_FileLoad)

        pixmap1 = QPixmap('C:\\code\\python\\face_unlock_project\\deepface-icon.png')
        pixmap1 = pixmap1.scaledToHeight(261)
        lbl_size = QLabel('img1 Width: ' + str(pixmap1.width()) + ', Height: ' + str(pixmap1.height()))
        self.img_ref.setPixmap(pixmap1)
        lbl_size.setAlignment(Qt.AlignCenter)

        pixmap2 = QPixmap('C:\\code\\python\\face_unlock_project\\deepface-icon.png')
        pixmap2 = pixmap2.scaledToHeight(261)
        lbl_size2 = QLabel('img2 Width: ' + str(pixmap2.width()) + ', Height: ' + str(pixmap2.height()))
        self.img_cmp.setPixmap(pixmap2)
        lbl_size2.setAlignment(Qt.AlignCenter)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    app.exec_()
