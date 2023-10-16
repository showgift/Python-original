# -*- coding = utf-8 -*-


from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # 进行SQLite数据库操作


def main():
    baseurl = "https://movie.douban.com/top250?start=0&filter="
    # 1.爬取网页
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影Top250.xls"
    print(datalist, datalist)
    # 3.保存数据
    saveData(savepath)


    # askURL("https://movie.douban.com/top250?start=")


#  影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')  # 创建正则表达式对象，表示规则(字符串模式)
#  影片图片的链接
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)  # re.S 让换行符包含在字符中
#  影片名
findTitle = re.compile(r'<span class="title">(.*)</span>')


#  影片评分
#

# 爬取网页
def getData(baseurl):
    datalist = []
    print("1")
    for i in range(0, 10):  # 调用获取信息的函数
        url = baseurl + str(i + 25)
        html = askURL(url)  # 保存获取到的网页源码
        print("diyig  for")
        # 2.解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串，形成列表
            # print(item)
            data = []
            item = str(item)

            link = re.findall(findLink, item)[0]  # re库通过正则表达式查找指定的字符串
            data.append(link)
            imgSrc = re.findall(findImgSrc, item)[0]
            data.append(imgSrc)
            titles = re.findall(findTitle, item)
            print("2 for")
            if (len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/", "")
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ')
            print(datalist)
    return datalist


# 得到一个指定的网页
def askURL(url):
    head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息      如果返回418可能是头部信息问题
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
    # 用户代理， 表示告诉豆瓣服务器，我们是什么类型的机器，浏览器（告诉我们可以接受什么水平文件
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        respose = urllib.request.urlopen(request)
        html = respose.read().decode("utf-8")
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
    sheet = book.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)
    col = ("电影详情链接","照片")
    for i in range(0, 8):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print("第%d条" %i)
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])


    book.save('student.xls')


if __name__ == "__main__":
    # 调用函数
    main()
