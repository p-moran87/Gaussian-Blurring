# -*- coding: utf-8 -*-
"""
Created on Wed May 24 12:18:59 2017

@author: pmoran
"""
import cv2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

"Get list of images to blurr and store in an array"
with open("list_of_images.txt",'r') as f:
    line = f.readlines()
image_list = []
for elem in line:
        image_list.extend(elem.strip().split(';'))  
        
"Get list of names (including pathes) for the simages to be saved"       
with open("list_of_images_names.txt",'r') as g:
    line_2 = g.readlines()
image_list_names = []
for elem in line_2:
        image_list_names.extend(elem.strip().split(';'))  

"Apply a Gaussian blurring with fixed radius and varied sigmas and save images to file"

for i in range(0,80):
    matplotlib.image.imsave(str(image_list_names[i]) + "_gaussian_50.png", cv2.GaussianBlur(plt.imread(image_list[i]), (21,21),0.5,0.5))
    matplotlib.image.imsave(str(image_list_names[i]) + "_gaussian_60.png", cv2.GaussianBlur(plt.imread(image_list[i]), (21,21),0.6,0.6))
    matplotlib.image.imsave(str(image_list_names[i]) + "_gaussian_75.png", cv2.GaussianBlur(plt.imread(image_list[i]), (21,21),0.75,0.75))
    matplotlib.image.imsave(str(image_list_names[i]) + "_gaussian_85.png", cv2.GaussianBlur(plt.imread(image_list[i]), (21,21),0.85,0.85))
    matplotlib.image.imsave(str(image_list_names[i]) + "_gaussian_95.png", cv2.GaussianBlur(plt.imread(image_list[i]), (21,21),0.95,0.95))
    matplotlib.image.imsave(str(image_list_names[i]) + "_gaussian_110.png", cv2.GaussianBlur(plt.imread(image_list[i]), (21,21),1.1,1.1))
    matplotlib.image.imsave(str(image_list_names[i]) + "_gaussian_130.png", cv2.GaussianBlur(plt.imread(image_list[i]), (21,21),1.3,1.3))
    matplotlib.image.imsave(str(image_list_names[i]) + "_gaussian_150.png", cv2.GaussianBlur(plt.imread(image_list[i]), (21,21),1.5,1.5))
    matplotlib.image.imsave(str(image_list_names[i]) + "_gaussian_180.png", cv2.GaussianBlur(plt.imread(image_list[i]), (21,21),1.8,1.8))
    
