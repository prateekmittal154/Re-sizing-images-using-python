#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 20:48:15 2022

@author: prateek
"""

from PIL import Image
import PIL
import glob

count=0;

for filename in glob.glob(r'/home/prateek/Desktop/outputs/*.jpg'):
    count=count+1
    image = Image.open(filename)
    print(image.size)
    height_percent =0.50
    height_size = int((float(image.size[1]) * float(height_percent)))
    width_size = int((float(image.size[0]) * float(height_percent)))
    image = image.resize((width_size, height_size), PIL.Image.NEAREST)
    print(image.size)
    file_name= '/home/prateek/Desktop/outputs_1/resized_image' + str(count) + '.jpg'
    image.save(file_name)

