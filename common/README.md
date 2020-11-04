将整个项目下载，直接在cofig中修改参数，运行statistics_classes.py即可

## 参数说明：

```python
classes = ["mark","top_window","tissue_box","roof_rack","pendant","spaer_wheel_rack"]  # 目标类别

save_path = 'D:\\学习\\练手项目\\ehualu\\data\\VOCdevkit\\VOC2007\\Annotations' # 生成统计文件的路径
ori_path = 'D:\\学习\\练手项目\\ehualu\\data\\VOCdevkit\\VOC2007\\new_txt' # 原始txt标签路径
	
```



## 注意：
1、save_path 是 所有要统计的文件夹
2、如果只需要统计一个文件夹种类多少，请在func的statistics.py中修改参数 并运行函数Collecte()
3、Modify()是用来删除无用种类的，具体的规则需要自己写。。

