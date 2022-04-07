import jieba
from collections import Counter
import math

#窗口大小为2
def combine2gram(cutword_list):
    if len(cutword_list) == 1:
        return []
    res = []
    for i in range(len(cutword_list) - 1):
        res.append(cutword_list[i]  + cutword_list[i + 1])
    return res

#窗口大小为3
def combine3gram(cutword_list):
    if len(cutword_list) <= 2:
        return []
    res = []
    for i in range(len(cutword_list) - 2):
        res.append(cutword_list[i] + cutword_list[i + 1]  + cutword_list[i + 2])
    return res



def calculate(corpus,mode):
    if mode == 1:
        # 1-gram
        chars = []
        for para in corpus:
            for i in range(len(para)):
                chars += para[i]
        char_num = len(chars)
        ct = Counter(chars)
        vocab1 = ct.most_common()
        entropy_1gram = sum([-(eve[1] / char_num) * math.log((eve[1] / char_num), 2) for eve in vocab1])
        print("词库总词数：", char_num, " ", "不同词的个数：", len(vocab1))
        print("出现频率前10的1-gram词语：", vocab1[:10])
        print("entropy_1gram:", entropy_1gram)

    if mode == 2:
        # 2-gram
        char_2gram = []
        for para in corpus:
            cutword_list = []
            for i in range(len(para)):
                cutword_list += para[i]
            char_2gram += combine2gram(cutword_list)
        # 2-gram的频率统计
        char_2gram_num = len(char_2gram)
        ct2 = Counter(char_2gram)
        vocab2 = ct2.most_common()

        # 2-gram相同句首的频率统计
        same_1st_word = [eve[0] for eve in char_2gram]
        assert char_2gram_num == len(same_1st_word)
        ct_1st = Counter(same_1st_word)
        vocab_1st = dict(ct_1st.most_common())
        entropy_2gram = 0
        for eve in vocab2:
            p_xy = eve[1] / char_2gram_num
            first_word = eve[0][0]
            entropy_2gram += -p_xy * math.log(eve[1] / vocab_1st[first_word], 2)
        print("词库总词数：", char_2gram_num, " ", "不同词的个数：", len(vocab2))
        print("出现频率前10的2-gram词语：", vocab2[:10])
        print("entropy_2gram:", entropy_2gram)

    if mode == 3:
        # 3-gram
        char_3gram = []
        for para in corpus:
            cutword_list = []
            for i in range(len(para)):
                cutword_list += para[i]
            char_3gram += combine3gram(cutword_list)

        # 3-gram的频率统计
        char_3gram_num = len(char_3gram)
        ct3 = Counter(char_3gram)
        vocab3 = ct3.most_common()
        # print(vocab3[:20])

        # 3-gram相同句首两个词语的频率统计
        same_2st_word = [eve[:2] for eve in char_3gram]
        assert char_3gram_num == len(same_2st_word)
        ct_2st = Counter(same_2st_word)
        vocab_2st = dict(ct_2st.most_common())
        entropy_3gram = 0
        for eve in vocab3:
            p_xyz = eve[1] / char_3gram_num
            first_2word = eve[0][:2]
            entropy_3gram += -p_xyz * math.log(eve[1] / vocab_2st[first_2word], 2)
        print("词库总词数：", char_3gram_num, " ", "不同词的个数：", len(vocab3))
        print("出现频率前10的3-gram词语：", vocab3[:10])
        print("entropy_3gram:", entropy_3gram)





#获取预处理后存储在当前目录下的语料文件
with open("processed_content.txt", "r", encoding="utf-8") as f:
    #取出预处理过的文本
    corpus = [eve.strip("\n") for eve in f]
    #mode表示N-gram中的N，这里可以输入1、2或者3；
    mode =3
    #输入参数即可输出熵计算结果
    calculate(corpus,mode)


