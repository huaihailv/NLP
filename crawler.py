import re
import requests
from bs4 import BeautifulSoup


def getHTML(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def getContent(url):
    html = getHTML(url)
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('div.mbtitle')
    paras_tmp = soup.select('p')
    paras = paras_tmp[3:]
    return paras


def saveFile(text, i):
    m = 'article_chinese_' + str(i) + '.txt'
    f = open(m, 'w')
    for words in text:
        if len(words) > 0:
            f.writelines(words.get_text() + "\n")
    f.close()


def main():
    url = ['http://book.zongheng.com/chapter/1156893/66838899.html',
           #'http://book.zongheng.com/chapter/1156893/66847678.html',
           #'http://book.zongheng.com/chapter/1156893/66853295.html',
           #'http://book.zongheng.com/chapter/1156893/66857427.html',
           #'http://book.zongheng.com/chapter/1156893/66861628.html',
           #'http://book.zongheng.com/chapter/1156893/66867530.html',
           #'http://book.zongheng.com/chapter/1156893/66874646.html',
           #'http://book.zongheng.com/chapter/1156893/66882035.html',
           #'http://book.zongheng.com/chapter/1156893/66887636.html',
           #'http://book.zongheng.com/chapter/1156893/66894283.html'
           ]
    text = getContent(url[0])
    for i in range(1, len(url)):
        text += getContent(url[i])
    saveFile(text, len(url))


if __name__ == '__main__':
    main()
