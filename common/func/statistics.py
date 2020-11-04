import os
from tqdm import tqdm



def Collecte(labels,ori_path,save_path):

	if not os.path.exists(save_path):
		os.makedirs(save_path)

	num = [0 for _ in range(len(labels))]

	lis = os.listdir(ori_path)
	for l in tqdm(lis):

		
		

		file = ori_path +'/' + l
		with open(file,'r') as f :
			lines = f.readlines()
			for line in lines:
				temp = line[0:1]
				num[int(temp)] +=  1

	with open(save_path+'/'+ori_path+'.txt','w') as f:
		for i in range(len(labels)):
			s = labels[i] + ': ' + str(num[i]) +'\n'
			f.write(s)

def Modify(ori_path,save_path):

	if not os.path.exists(save_path):
		os.makedirs(save_path)

	lis = os.listdir(ori_path)
	for l in tqdm(lis):

		add = []
		file = ori_path +'/' + l
		with open(file,'r') as f :
			lines = f.readlines()
			for line in lines:
				flag = int(line[0:1]) -1
				if flag == -1:
					continue
				temp = str(flag) + line[1:] 
				add.append(temp)

		with open(save_path+'/'+ l,'w') as f:
			for i in add:
				f.write(i)

			
label = ["plate","mark","top_window","tissue_box","roof_rack","pendant","spaer_wheel_rack"]
ori_path = './gedi_4991'
save_path = './results_'
# Collecte(label,ori_path,save_path)
Modify(ori_path,save_path)
