# coding:utf-8
import requests
import re
import os

s = requests.Session()
header = {
    # 'Host':'www.mmjpg.com',
    'Referer': 'http://www.mmjpg.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.3302.400 QQBrowser/9.6.11768.400',
}

if os.path.exists("D:/mmjpg") == False:
    os.mkdir("D:/mmjpg")                # 判断是否存在文件夹，若没有则创建


def fan_ye(html, chu_shi=1, pan_duan=None):
    # 判断数据是不是重复
    p = re.compile(r'src="(.*?)" alt="(.*?)".*?<span class="view">(.*?)<')
    l = p.findall(html)
    if l != pan_duan:

        # 匹配正文内容
        p = re.compile(r'src="(.*?)".*?alt="(.*?)".*?<span class="view">(.*?)<')
        # print(html.text)
        for m in p.finditer(html):
            URL = m.group(1)
            biao_ti = m.group(2)
            liu_lan = m.group(3)

            # 图片保存
            TUPIAN = s.get(URL, headers=header)
            f = open("D:/mmjpg/"+biao_ti + ".jpg", 'wb')    # 保存至文件夹
            f.write(TUPIAN.content)
            f.close()
            print(TUPIAN)
            print(biao_ti + '\t' + URL + '\t' + liu_lan + '\t' + '保存成功')

        # 翻页设置
        chu_shi += 1
        pan_duan = l
        url = "http://www.mmjpg.com/home/" + str(chu_shi)
        html = s.get(url, headers=header)
        html.encoding = 'utf-8'

        # 递归调用
        fan_ye(html.text, chu_shi, pan_duan)


# 爬虫开始位置
url = "http://www.mmjpg.com/"
html = s.get(url, headers=header)
html.encoding = 'utf-8'
fan_ye(html.text)
