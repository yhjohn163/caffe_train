# -*- coding:UTF-8 -*-
import numpy as np
import argparse
import sys,os  
import cv2
from PIL import Image, ImageDraw, ImageFont
caffe_root = '../../../../caffe_deeplearning_train/'
sys.path.insert(0, caffe_root + 'python')  
import caffe  

provNum, alphaNum, adNum = 34, 25, 35
provinces = ["皖", "沪", "津", "渝", "冀", "晋", "蒙", "辽", "吉", "黑", "苏", "浙", "京", "闽", "赣", "鲁", "豫", "鄂", "湘", "粤", "桂",
             "琼", "川", "贵", "云", "藏", "陕", "甘", "青", "宁", "新", "警", "学", "O"]
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
             'X', 'Y', 'Z', 'O']
ads = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
       'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'O']

def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', type=str, required=True, help='.prototxt file for inference')
    parser.add_argument('--weights', type=str, required=True, help='.caffemodel file for inference')
    return parser
parser1 = make_parser()
args = parser1.parse_args()
net_file= args.model
caffe_model= args.weights
test_dir = "../annoImg"

if not os.path.exists(caffe_model):
    print(caffe_model + " does not exist")
    exit()
if not os.path.exists(net_file):
    print(net_file + " does not exist")
    exit()
caffe.set_mode_gpu();
caffe.set_device(0);
net = caffe.Net(net_file,caffe_model,caffe.TEST)  

CLASSES = ('background',
           'liceneseplate')


font = ImageFont.truetype('NotoSansCJK-Black.ttc', 20)
fillColor = (255,0,0)

def preprocess(src):
    img = cv2.resize(src, (128, 64))
    img = img - 127.5
    img = img * 0.007843
    return img


def detect(imgfile):
    origimg = cv2.imread(imgfile)
    img = preprocess(origimg)
    print(img.shape)
    img = img.astype(np.float32)
    img = img.transpose((2, 0, 1))
    

    net.blobs['data'].data[...] = img
    out = net.forward()
    box = out['ccpd_output'][0,0,:,0:7]
    print(box)
    
    cv2.imshow("facedetector", origimg)
 
    k = cv2.waitKey(0) & 0xff
        #Exit if ESC pressed
    if k == 27 : return False
    return True

for f in os.listdir(test_dir):
    if detect(test_dir + "/" + f) == False:
       break
