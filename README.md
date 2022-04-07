# DL-NLP2022-Homework

___作业索引___
---------------
+ DL-NLP2022-Homework-Liuqiange.pdf 作业一的实验报告
+ /dataset 数据库存储目录，内涵金庸小说
+ preprocess.py 语料库预处理代码，运行后将处理后的预料存储至processed_content.txt文件
+ entropy_calculating_word.py 以词为单位计算平均信息熵
+ entropy_calculating_char.py 以字为单位计算平均信息熵
+ processed_content.txt 处理后的语料库存储文件，由preprocessed.py自动生成，可删除后重新运行

___代码说明___
---------------

###开发环境
+ python 3

###运行说明
+ processed_content.txt文件中的编码（code line 27），因为我使用的设备是Mac M1，编码使用的是gb18030。若您为windows系统，烦请更换为ANSI，否则可能存在问题。

+ entropy_calculating_word.py 与entropy_calculating_char.py 文件中的mode参数表示n-gram的N，可在函数入口自行更换后运行；
