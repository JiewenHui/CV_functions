from config import *

if __name__ == '__main__':
    classes , xmlpath , txtpath , newDir_label , is_file , train_file_path , val_file_path , name_length , oriDir , newDir1, have_difficult = opt()
    print('开始转换xml文件')
    xmlList = os.listdir(xmlpath)
    for xml in tqdm(xmlList):
        # print(xml)
        xmlId = xml.strip().split('.')[0]
        f.convert_annotation(xmlId, xmlpath, txtpath,have_difficult,classes) 
    print('转换xml文件结束')
    print('-'*20)
    if is_file:
        print('开始转移训练集')
        f.move(oriDir,newDir1,txtpath,newDir_label,name_length=name_length,is_file=is_file,file_path=train_file_path)
        print('转移训练集结束')
        print('-'*20)
        print('开始转移验证集')
        f.move(oriDir,newDir1,txtpath,newDir_label,name_length=name_length,is_file=is_file,file_path=val_file_path)
        print('转移验证集结束')
    else:
        print('开始转移')
        f.move(oriDir,newDir1,txtpath,newDir_label,name_length=name_length,is_file=is_file,file_path=train_file_path)
        print('转移结束')
