#!/usr/bin/python
# -*- coding: UTF-8 -*-
import glob
import os
import re
import sys
import cv2
import numpy as np
import random
def shuffle_file(filename):
	f = open(filename, 'r+')
	lines = f.readlines()
	random.shuffle(lines)
	f.seek(0)
	f.truncate()
	f.writelines(lines)
	f.close()

if 0:
    label = "vggface2_train.txt"
else:
    label = "vggface2_test.txt"

vgglabmap_train = 'labelmap.txt'

def generate_labels(img_dir):
	dirs = os.listdir(img_dir)
	label = 0
	_str = ""
	for dir in dirs:
		if os.path.isdir(os.path.join(img_dir, dir)):
			imgs = glob.glob(os.path.join(os.path.join(img_dir, dir), "*.jpg"))
			for img in imgs:
				path = os.path.abspath(img).split(".jpg")[0]
				label_str = path + " " + str(label) + "\n"
				print(label_str)
				_str += label_str
			label += 1
	return _str


def generat_labelmap(img_dir):
	dirs = os.listdir(img_dir)
	label = 0
	_str = ""
	for dir in dirs:
		if os.path.isdir(os.path.join(img_dir, dir)):
			content_labelmap_str = dir + ' ' + str(label) + "\n"
			print(content_labelmap_str)
			_str += content_labelmap_str
			label += 1
	return _str


if __name__ == '__main__':
	if 0:
		img_dir = sys.argv[1]
		labels_str = generate_labels(img_dir)

		with open(label, "w") as labels_file:
			labels_file.writelines(labels_str)
		shuffle_file(label)
	else:
		img_dir = sys.argv[1]
		labels_str = generat_labelmap(img_dir)

		with open(vgglabmap_train, "w") as labels_file:
			labels_file.writelines(labels_str)
		shuffle_file(vgglabmap_train)

