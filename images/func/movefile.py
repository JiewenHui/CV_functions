##深度学习过程中，需要制作训练集和验证集、测试集。

import os, random, shutil
from tqdm import tqdm

def move_file_txt(oriDir,newDir1, file_path,txtpath,newDir_label,name_length):


    if not os.path.exists(newDir_label):
        os.makedirs(newDir_label)
    if not os.path.exists(newDir1):
        os.makedirs(newDir1)

    file = 'train' if file_path[-9:]=='train.txt' else 'valid'

    if not os.path.exists(newDir_label+'/'+file):
        os.makedirs(newDir_label+'/'+file)
    if not os.path.exists(newDir1+'/'+file):
        os.makedirs(newDir1+'/'+file)
        
    with open(file_path,'r') as f:
        lines = f.readlines()
        for line in tqdm(lines):
            filename1 = line[:name_length] 
            shutil.move(txtpath+'/'+filename1+'.txt', newDir_label+'/'+file+'/'+filename1+'.txt')
            shutil.move(oriDir+'/'+filename1+'.jpg', newDir1+'/'+file+'/'+filename1+'.jpg')
    return 

def move_file_num(oriDir,newDir1,txtpath,newDir_label):

    image_file = os.listdir(oriDir)
    label_file = os.listdir(txtpath)
    # print(len(label_file))

    file_list = ['train' ,'valid','test']
    for file in file_list:
        if not os.path.exists(newDir_label+'/'+file):
            os.makedirs(newDir_label+'/'+file)
        if not os.path.exists(newDir1+'/'+file):
            os.makedirs(newDir1+'/'+file)


    for i, file in enumerate(tqdm(label_file)):

        ori_path = os.path.join(txtpath,file)
        jpg_name = file.strip().split('.')[0] +'.jpg'
        jpg_path = os.path.join(oriDir,jpg_name)

        if i < 0.6 * len(label_file):
            des_path = newDir_label + '/train/'
            des_path_img = newDir1 + '/train/'
        elif 0.6<= i < 0.8 * len(label_file):
            des_path = newDir_label + '/valid/'
            des_path_img = newDir1 + '/valid/'
        else:
            des_path = newDir_label + '/test/'
            des_path_img = newDir1 + '/test/'
        if os.path.exists(des_path + file) and os.path.exists(des_path_img + file):
            continue

        shutil.move(ori_path, des_path)
        shutil.move(jpg_path, des_path_img) 
    return

def move(oriDir,newDir1,txtpath,newDir_label,name_length=6,is_file=False,file_path=''):
    
    if is_file:
        assert os.path.exists(file_path), '%s不存在'%(file_path)
        move_file_txt(oriDir,newDir1,file_path,txtpath,newDir_label,name_length)
    else:
        move_file_num(oriDir,newDir1,txtpath,newDir_label)
    return

# if __name__ == '__main__':
# 	fileDir = "/home/wangshuang/project/YoloV5_2/YOLO-v5-master/ws_dataset/images_1/test/"
# 	fileDir1 = "VOCtrainval_06-Nov-2007/VOCdevkit/VOC2007/new_txt/"#源图片文件夹路径
# 	tarDir = 'VOCtrainval_06-Nov-2007/VOCdevkit/VOC2007/train_txt/'    #移动到新的文件夹路径
# 	moveHui(fileDir1,tarDir)