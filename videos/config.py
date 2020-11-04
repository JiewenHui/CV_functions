import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import shutil
from tqdm import tqdm

import func as f

def opt():

	ori_path = 'D:\\学习\\练手项目\\ehualu\\video' # 原始图片的路径
	save_path = 'D:\\haha\\images' # 新图片路径 该路径下会生成 train和valid 两个文件夹  
	max_frames = 50 # 最多截取多少次图片
	jump = 5 # 每几帧抽取一次图片

	return ori_path,save_path,max_frames,jump