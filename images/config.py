import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import shutil
from tqdm import tqdm

import func as f

def opt():

	classes = ['Person', 'Vehicle', 'nonmotorvehicle']  # 目标类别

	xmlpath = 'D:\\学习\\练手项目\\ehualu\\project\\data\\xml' # xml文件的路径
	txtpath = 'D:\\学习\\练手项目\\ehualu\\data\\VOCdevkit\\VOC2007\\new_txt' # 将xml转换成txt之后的路径
	newDir_label = 'D:\\学习\\练手项目\\ehualu\\project\\data\\aa\\labels' # 新标签路径 该路径下会生成 train和valid 两个文件夹

	is_file = False # 是否存在已经分好类的train.txt文件和val.txt文件
	train_file_path = 'D:\\学习\\练手项目\\ehualu\\data\\VOCdevkit\\VOC2007\\ImageSets/Main/train.txt' # 已经分好类的train.txt文件
	val_file_path = 'D:\\学习\\练手项目\\ehualu\\data\\VOCdevkit\\VOC2007/ImageSets/Main/val.txt' # 已经分好类的val.txt文件
	name_length = 6 # 根据文件名字长度修改 例如 000001.jpg

	oriDir = 'D:\\学习\\练手项目\\ehualu\\project\\data\\images\\train' # 原始图片的路径
	newDir1 = 'D:\\学习\\练手项目\\ehualu\\project\\data\\aa\\images' # 新图片路径 该路径下会生成 train和valid、test 三个文件夹
	have_difficult = False # 标注文件里 是否存有 difficul

	return classes , xmlpath , txtpath , newDir_label , is_file , train_file_path , val_file_path , name_length , oriDir , newDir1 , have_difficult