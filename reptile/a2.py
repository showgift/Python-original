# -*- coding = utf-8 -*-
import sys
import os

import re  # 正则表达式，进行文字匹配
from bs4 import BeautifulSoup  # 网页解析，获取数据
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作


def main():
    baseurl = "https://movie.douban.com/top250?start=0"
    # 1.爬取网页
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影250.xls"
    # 3.保存数据
    saveData(datalist, savepath)

    # askURL("https://movie.douban.com/top250")


#  影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')
#  影片图片的链接
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 10):  # 调用获取信息的函数
        url = baseurl + str(i * 25)
        html = askURL(url)  # 保存获取到的网页源码

        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串，形成列表
            # print(item)
            data = []
            item = str(item)
            # print(item)
            link = re.findall(findLink, item)[0]  # re库通过正则表达式查找指定的字符串
            data.append(link)
            Img = re.findall(findImgSrc, item)
            data.append(Img)

            datalist.append(data)

    return datalist


# 得到一个指定的网页
def askURL(url):
    head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息      如果返回418可能是头部信息问题
        "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
    # 用户代理， 表示告诉豆瓣服务器，我们是什么类型的机器，浏览器（告诉我们可以接受什么水平文件
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


# 保存数据
def saveData(datalist, savepath):
    print("save...")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet("豆瓣电影Top250", cell_overwrite_ok=True)
    col = ("电影详情链接", "图片")
    for i in range(0, 2):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        print("第%d条" % i)
        data = datalist[i]
        for j in range(0, 2):
            sheet.write(i + 1, j, data[j])

    book.save(savepath)


if __name__ == "__main__":
    main()
    print("Reptiled.")
