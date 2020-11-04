import os, random, shutil


def move(ori,lis,out_dir): 
	count = 0
	amount = 0
	for di in lis:
		file_path = ori + '/' + di
		file = os.listdir(file_path)
		amount += len(file)
		count += 1
		print('当前处理文件为%s'%(file_path))
		for i in file:
			name = file_path +'/' + i
			shutil.copy(name, out_dir)


if __name__ == '__main__':
	out_dir = './data/'
	lis_ori = os.listdir('./')
	ori = './'
	move(ori,lis_ori[:-2],out_dir)