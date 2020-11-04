import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import shutil
#20190227@new-only 2007 data
#sets=[('2007', 'train'), ('2007', 'val'), ('2007_test', 'test')]
#sets =[('2014', 'train')]
# classes = ['person', 'vehicle', 'non_motor_vehicle']
 
 
def convert(size, box):
    dw = 1./(size[0])
    dh = 1./(size[1])
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)
 
def convert_annotation(image_id, path,out_path,have_difficult,classes):
    # print("2-open annotations")
    in_file = open(path + '/%s.xml'%(image_id))
    # print("3-convert to txt")
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    ss = out_path +'/%s.txt'%(image_id)
    if os.path.exists(ss):
        return
    out_file = open(out_path +'/%s.txt'%(image_id), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    for obj in root.iter('object'):
        if have_difficult:
            difficult = obj.find('difficult').text 
        else:
            difficult = 0
        cls = obj.find('name').text
        #print("666",cls)
        # if cls == others:
            # continue
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        # print("666",b)
        bb = convert((w,h), b)
        # print(bb)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')
        # print("write ok")
        
 
if __name__=='__main__':
    xmlpath = './xml'
    out_path = './new_txt'
    #path = os.getcwd()
    #path = os.path.join(path, 'yolo_test_dataset_7k')
    #xmlpath = os.path.join(path, 'xmls')
    xmlList = os.listdir(xmlpath)
    for xml in xmlList:
        # print(xml)
        xmlId = xml.strip().split('.')[0]
        convert_annotation(xmlId, xmlpath) 
