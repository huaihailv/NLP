from importlib.metadata import entry_points
from numpy import character
import math

fr = open('article_chinese_1.txt', 'r', encoding='GBK')


characters = []
rate = {}
puncs = ['……', '，', '。', '？', '！', '——', '“', '”', '：', '‘', '’', '、', '', '；', '（', '）', '《', '》', '。', '…']

for i in range(1,11):
    m = 'article_chinese_'+str(i)+'.txt'
    fr = open(m, 'r', encoding='GBK')
    content = fr.readlines()
    contentLines = ''
    for line in content:
        line = line.strip()
        if len(line) == 0:
            continue
        contentLines = contentLines + line

        for x in range(0, len(line)):
            if line[x] in puncs:
                continue
            elif line[x] not in characters and line[x] not in rate:
                # 如果该汉字第一次出现，则加入characters中，并将rate中对应位置置1
                characters.append(line[x])
                rate[line[x]] = 1
            rate[line[x]] += 1
# print('全文共有%d个字' % len(contentLines))
    print('%d篇文章共有%d种字,%d个字' % (i,len(characters),len(contentLines)))
    # print('\n')
    entropy_sum = 0.0
    for i in rate:
        entropy = rate[i] / len(contentLines)
        entropy_sum += -entropy * (math.log2(entropy))
    print("这段文字中汉字的熵为：", entropy_sum)
    fr.close()
# for i in rate:
#     print("(", i, ")共出现 (", rate[i], ")次")



