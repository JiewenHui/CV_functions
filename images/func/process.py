#process#
import cv2
import os
from tqdm import tqdm

new_root = '../evening_processed'
ori_root = '../evening_upto201021'



def process(ori_root,new_root):
	count = 0
	folder_lis = os.listdir(ori_root)
	for folder in folder_lis:
		new_folder = new_root+'/' + folder
		tqdm.write('当前处理文件夹数目为：%s'%(count+1))
		tqdm.write('当前处理文件夹为：%s'%(folder))
		if not os.path.exists(new_folder):
			os.makedirs(new_folder)
		file_list = os.listdir(ori_root + '/' + folder)
		# for file in tqdm(file_list):
		for file in (file_list):
			file_name = ori_root + '/' + folder + '/' + file
			new_name = new_folder + '/' + file
			if os.path.exists(new_name):
				continue
			img = cv2.imread(file_name)
			cropped = img[1080-830:,:]
			cv2.imwrite(new_name, cropped)
		tqdm.write('%s文件夹处理完成'%(folder))
		tqdm.write('-'*20)
		count += 1

if __name__ == '__main__':
	
	process(ori_root,new_root)