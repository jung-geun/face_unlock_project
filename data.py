# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 10:47:48 2022

@author: face
"""

from deepface import DeepFace

result = DeepFace.verify(img1_path = "img1.jpg", img2_path = "img2.jpg")