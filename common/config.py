import os
from os import listdir, getcwd
from os.path import join
import shutil
from tqdm import tqdm

import func as f

def opt():

	classes = ['aeroplane','bicycle' ,'bird', 'boat', 'bottle', 'bus', 'car', 
        'cat', 'chair','cow','diningtable', 'dog', 'horse', 'motorbike', 
        'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']  # 目标类别

	save_path = 'D:\\学习\\练手项目\\ehualu\\data\\VOCdevkit\\VOC2007\\Annotations' # xml文件的路径
	ori_path = 'D:\\学习\\练手项目\\ehualu\\data\\VOCdevkit\\VOC2007\\new_txt' # 将xml转换成txt之后的路径
	
	return classes , ori_path , save_path 