# -*- coding:utf-8 -*

import os


import random
import re  
import requests  
from bs4 import BeautifulSoup
import markdownify
import json
import codecs


def get_header():
#函数功能：构造协议头

    headers = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
    ]
    #headers="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"
    # return {'User-Agent':headers[random.randint(0,3)],'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8","Accept-Encoding":"gzip, deflate, br"}
    return {'User-Agent': headers[random.randint(0, 3)]}


def get_header2():
#函数功能：构造协议头2

    headers = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
    ]
    #headers="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0"
    # return {'User-Agent':headers[random.randint(0,3)],'Accept':"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8","Accept-Encoding":"gzip, deflate, br"}
    return {'User-Agent': headers[random.randint(0, 3)], "Cookie": "__client_id=6a8c24b4e6fa424babfc00eb87a3a09ffc88ee38; _uid=1094637"}


def get_html(url):
    req = requests.get(url=url, headers=get_header())

    return req.text


def get_html2(url):
    req = requests.get(url=url, headers=get_header2())

    return req.text


def getContext(begin=1000,end=1051):
#函数功能：获取题目内容
#参数：
#@begin:范围开始,默认：1000
#@end:范围结束,默认：1051
    pidlist = range(begin, end)
    ex = '<h1>(.*?)<\/h1>'
    for i in pidlist:
        url = "https://www.luogu.com.cn/problem/P"+str(i)
        html = get_html(url)
        #print(html)
        #img_src_list = re.findall(ex,html,re.S)
        soup = BeautifulSoup(html, 'html.parser')
        article = soup.find('article')
        title = soup.find('h1')
        src_title = re.findall(ex, str(title), re.S)

        md = markdownify.markdownify(str(article))
        name = "P"+str(i)
        dir="./"+name+"-"+str(src_title[0])
        print("题目内容到了："+name)
        # 打开文件，如果文件不存在则创建
        if not os.path.exists(dir):
            os.makedirs(dir)
            
        file = open(dir+"/"+name+"-"+str(src_title[0])+".md", "w")

        # 写入一些数据
        file.write(md)

        # 关闭文件
        file.close()
        # print(md)


def getSolution(begin=1000,end=1051):
#函数功能：获取题目解答
#参数：
#@begin:范围开始,默认：1000
#@end:范围结束,默认：1051

    pidlist = range(begin, end)
    ex = '<script>(.*?)<\/script>'
    ex2 = '"(.*?)"'
    for i in pidlist:
        url = "https://www.luogu.com.cn/problem/solution/P"+str(i)
        html = get_html2(url)
        #print(html)
        #img_src_list = re.findall(ex,html,re.S)
        src_title = re.findall(ex, str(html), re.S)
        # 获取json
        # print(src_title)
        src_title = re.findall(ex2, str(src_title), re.S)

        # json解码
        tow = requests.utils.unquote(src_title[0])
        #src_title = re.findall(ex,str(title),re.S)

        # 读取unicode编码
        #unicode_code = codecs.decode(tow, 'unicode_escape')
        # print(unicode_code)
        # aa=json.loads(unicode_code)
        name = "P"+str(i)
        # print(aa["currentData"]["problem"]["title"])
        # print(aa["currentData"]["solutions"])
        content = json.loads(tow)
        dir="./"+name+"-"+content["currentData"]["problem"]["title"]

        
        name = name+"-"+(content["currentData"]["problem"]["title"]+"-题解")
        print("题解到了："+name)
        file = open(dir+"/"+name+".md", "w")
        ls1=content["currentData"]["solutions"]["result"][0]["content"]
        ls2=ls1.replace('\xa0', ' ')
        ls2=ls2.replace('\u2740', ' ')
        # 写入一些数据
        file.write(str(ls2))  # 只写入第一个答案

        # 关闭文件
        file.close()
        # with open(name+".txt", "r") as f:
        #     content = json.load(f)

        # 打开文件，如果文件不存在则创建
        # file = open(name+"-"+str(src_title[0])+".txt", "w")

        # # 写入一些数据
        # file.write(md)

        # # 关闭文件
        # file.close()
        # print(md)


def main():
#函数功能：获取题目表
    # https://www.luogu.com.cn/problem/list
    ex = '<script>(.*?)<\/script>'
    ex2 = '"(.*?)"'
    url_table = "https://www.luogu.com.cn/problem/list"
    html1 = requests.get(url=url_table, headers=get_header())
    # 获取内容
    src_title = re.findall(ex, str(html1.text), re.S)
    # 获取json
    src_title = re.findall(ex2, str(src_title), re.S)
    # json解码
    tow = requests.utils.unquote(src_title[0])

    # 读取unicode编码
    unicode_code = codecs.decode(tow, 'unicode_escape')

    #print(name)
    file = open("table.md", "w")

    # 写入一些数据
    file.write(unicode_code)

    # 关闭文件
    file.close()
# 难度difficulty
# 总分fullScore
# 类型type
# 通过率totalAccepted/totalSubmit
# {'tags': [2, 108], 'wantsTranslation': False, 'totalSubmit': 999978, 'totalAccepted': 379321, 'flag': 5, 'pid': 'P1000', 'title': '超级玛 丽游戏', 'difficulty': 1, 'fullScore': 100, 'type': 'P'}
    with open("./table.md", "r") as f:
        content = json.load(f)
    print(content["currentData"]["problems"]["result"][0])


if __name__ == '__main__':
    #获取列表
    main()
    #获取题目内容,范围（1000,1051）
    getContext(1000,1051)
    #获取题目解答,范围（1000,1051）
    getSolution(1000,1051)

