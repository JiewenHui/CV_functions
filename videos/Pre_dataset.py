from config import *

if __name__ == '__main__':
    ori_path,save_path,max_frames,jump = opt()
    print('开始抽取图片')
    f.Video_Frames(ori_path,save_path,max_frames,jump)
    print('抽取图片结束')
    
