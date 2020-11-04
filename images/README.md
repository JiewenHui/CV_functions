将整个项目下载，直接在cofig中修改参数，运行Pre_dataset.py即可

## 参数说明：

```python
classes = ['person','car'] # 目标类别

xmlpath = './VOC2007/Annotations' # xml文件的路径
have_difficult = True # 标注文件里 是否存有 difficul
txtpath = './VOC2007/new_txt' # 将xml转换成txt之后的路径
newDir_label = '../data/labels' # 新标签路径 该路径下会生成 train和valid 两个文件夹

is_file = True # 是否存在已经分好类的train.txt文件和val.txt文件
train_file_path = './VOC2007/ImageSets/Main/train.txt' # 已经分好类的train.txt文件
val_file_path = './VOC2007/ImageSets/Main/val.txt' # 已经分好类的val.txt文件
name_length = 6 # 根据文件名字长度修改 例如 000001.jpg

oriDir = './VOC2007/JPEGImages' # 原始图片的路径
newDir1 = '../data/images' # 新图片路径 该路径下会生成 train和valid 两个文件夹
```



## 注意：
需要将图片放到一个文件夹下，如果在多个文件夹下，可用move.py文件进行转移

最终得到的 /images 和 /labels 即位所求