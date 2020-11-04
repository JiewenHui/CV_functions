from config import *

if __name__ == '__main__':
	
	classes , ori_path , save_path   = opt()
	ll = os.listdir(ori_path)
	print('开始统计')
	for i in ll :
		print('当前处理文件夹%s'%(i))
		f.statistics_label(classes , ori_path , save_path)
		print('%s文件夹处理完成'%(i))
		print('-'*10)
	print('统计结束')
