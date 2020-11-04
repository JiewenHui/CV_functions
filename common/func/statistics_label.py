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

if __name__ == '__main__':
	
	label = ["mark","top_window","tissue_box","roof_rack","pendant","spaer_wheel_rack"]
	ori_path = './xuzhou_23k_2'
	save_path = './results'
	Collecte(label,ori_path,save_path)

