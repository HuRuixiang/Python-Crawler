#需提前安装requests库
import requests
import re

#获取图片链接，参数(正则表达式，网页url)，返回一个list
def get_picurl(url,regular_expression):
    try:
            pic_url = []
            r = requests.get(url,timeout=30)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            for m in re.finditer(regular_expression,r.text):
                    if m:
                            pic_url.append(m.group(0))
            return pic_url
    except:
            print("获取图片链接异常")

#下载图片，参数(图片url，存储目录)
def download_pic(pic_url,root):
    try:
            url_picture = pic_url
            rp = requests.get(url_picture,timeout=30)
            rp.raise_for_status()
            path = root + url_picture.split("/")[-1]
            with open(path,"wb") as f:
                    f.write(rp.content)
    except:
            print("下载异常")
            
#调用函数
#使用时请将url替换为自己所爬取网站的url
#该正则表达式可以完成大部分网站.jpg/.jpeg图片url的匹配，若无法完成匹配，请自行修改
picurl_list = get_picurl("http://www.woshipm.com/operate/2278926.html",r'(https?|ftp|file)://[-A-Za-z0-9+&@#/%=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|].jpe?g')
for each_picurl in picurl_list:
    #循环打印每张图片url
    print(each_picurl)
    #使用时请将路径替换为本地路径
    download_pic(each_picurl,"C:\\Users\\问津\\Desktop\\download\\")
        
