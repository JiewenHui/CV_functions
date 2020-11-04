# -*- coding: utf-8 -*- 

import cv2
import os
NN = ['_','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def Judge(s,NN):
	s = s.strip()
	for i in list(s):
		if i not in NN:
			return False
	return True

def Frames(ori_path,name,save_path,max_frames,jump,count): 
	file = ori_path +'/'+ name
	capture=cv2.VideoCapture(file)  #视频名称
	# print(capture.isOpened())
	file_name = (name.strip().split('.')[0]) if Judge((name.strip().split('.')[0]),NN) else str(count)
	count = count if Judge((name.strip().split('.')[0]),NN) else (count + 1)
	name_path =  save_path +'/'+ file_name
	print(name_path)
	if not os.path.exists(name_path):
		os.makedirs(name_path)
	frame_counter = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
	max_frames = min(max_frames,frame_counter)
	num=0
	while True: 
	    ret , img = capture.read()  
	    if not ret:
	        break	
	    if jump: # 是否跳帧抽取
	    	if num%jump == 0:
	    		cv2.imwrite((name_path + '/'+ str(num)+ '.jpg'),img)
	    else:
	    	cv2.imwrite((name_path + '/'+ str(num)+ '.jpg'),img)  #写出视频图片.jpg格式
	    if num>= max_frames:                                  #导出视频的前max_frames帧图像
	        break
	    num=num+1
	capture.release() 
	print(name + ' is finished ')

def Video(ori_path,save_path,max_frames,jump):
	if not os.path.exists(save_path):
		os.makedirs(save_path)
		
	names = os.listdir(ori_path)
	count = 1
	for name in names:
		Frames(ori_path,name,save_path,max_frames,jump,count)