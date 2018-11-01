#程序每次需要改三个地方
#1 out_file    #输出文件
#2 name_pic   #用来存放图片名字的txt文件
#3 root_xml_dir  #xml的目录，用来遍历
#4 path_pic   #图片的路径


import xml.etree.ElementTree as ET
import pickle
import string
import os
import shutil
from os import listdir, getcwd
from os.path import join
import sys
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
import cv2


def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(xml_path,out_txt_path):
    #xml_path为输入的xml文件路径
    in_file = open(xml_path)
    print(xml_path)
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    pic_name = root.find('filename').text
    #out_file为输出的txt文件名
    out_file = open(out_txt_path+'%s.txt'%(pic_name), 'w')

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
    return pic_name






if __name__ == "__main__":
    # 对文件实现遍历
    # name_pic用来存放jpg图片路径的txt文件
    #root_xml_dir为需要遍历的xml文件夹的路径
    name_pic = open('/home/zhongzhixing01/桌面/name_pic_1.txt', 'w')
    root_xml_dir = '/home/zhongzhixing01/桌面/xml_10-17'
    out_txt_path = '/home/zhongzhixing01/桌面/new_pic_labels_1'
    pic_path = '/home/zhongzhixing01/桌面/new_pic/'
    list = os.listdir(root_xml_dir)
    list_name = ''
    classes = ['red', 'green', 'yellow', 'none']
    for i in range(0, len(list)):
        xml_path = os.path.join(root_xml_dir, list[i])
        pic_name = convert_annotation(xml_path,out_txt_path)
        path_pic = pic_path + pic_name + '.jpg'
        list_name = list_name + path_pic + '\n'
        # print(path)
    print('writing the path of pic')
    name_pic.write(list_name)
    print('done')
