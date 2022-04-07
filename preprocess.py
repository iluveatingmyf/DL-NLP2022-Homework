#!/usr/bin/env python
# coding=utf-8

import os
import re
from collections import Counter

#去除广告
def ridofad(content):
    ad = ['本书来自www.cr173.com免费txt小说下载站\n更多更新免费电子书请关注www.cr173.com', '新语丝电子文库']
    for a in ad:
        content = content.replace(a, '')
    return content

def preprosessing(root_path):
    # corpus 存储语料库，以每一个自然段为一个分割
    corpus = []

    #遍历dataset下所有语料文件
    for i in os.listdir(root_path):
        #判定所选文件以txt结尾
        if i[-3:] == 'txt':
            path = root_path + r'/' + i
            # 使用的设备是Mac M1，由此ANSI编码方式对我不适用，代码使用的是gb18030
            with open(path, 'r', encoding='gb18030') as f:
                text = [line.strip("\n").replace("\u3000", "").replace("\t", "") for line in f][3:]
                corpus += text

    #利用正则匹配，消除无关字符
    regex_str = ".*?([^\u4E00-\u9FA5]).*?"
    english = u'[a-zA-Z0-9’!"#$%&\'()*+,-./:：;「<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
    symbol = []
    for j in range(len(corpus)):
        corpus[j] = re.sub(english, "", corpus[j])
        symbol += re.findall(regex_str, corpus[j])
    #对出现的字符进行匹配与统计
    count_ = Counter(symbol)
    count_symbol = count_.most_common()
    noise_symbol = []

    for eve_tuple in count_symbol:
        #将出现次数小于200次的字符消除
        if eve_tuple[1] < 200:
            noise_symbol.append(eve_tuple[0])
    noise_number = 0
    for line in corpus:
        for noise in noise_symbol:
            line.replace(noise, "")
            noise_number += 1

    print("完成的噪声数据替换点：", noise_number)
    print("替换的噪声符号：")
    for i in range(len(noise_symbol)):
        print(noise_symbol[i], end=" ")

    with open("processed_content.txt", "a", encoding="utf-8") as f:
        for line in corpus:
            #去掉没有意义的广告
            line = ridofad(line)
            f.write(line)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    content = preprosessing('./dataset')