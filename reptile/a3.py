# -*- coding = utf-8 -*-

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


def askURL():


def getData():



def saveData():



if __name__ == "__main__":
    main()