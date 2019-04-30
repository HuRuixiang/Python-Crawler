#需提前安装requests库
import requests
import re

#获取子页面链接，参数(正则表达式，网页url),返回一个list
def get_pageurl(url,regular_expression):
        try:
                r = requests.get(url,timeout=30)
                r.raise_for_status()
                r.encoding = r.apparent_encoding
                list = re.findall(regular_expression,r.text)
                clean_list = sorted(set(list),key=list.index)
                return clean_list
        except:
                print("获取网页链接异常")

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

page_url_list = get_pageurl("http://t66y.com/thread0806.php?fid=8",r'htm_data[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|].html')
for each_page_url in page_url_list[5:]:
        picurl_list = get_picurl("http://t66y.com/"+each_page_url,r'(https?|ftp|file)://[-A-Za-z0-9+&@#/%=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|].jpe?g')
        for each_picurl in picurl_list:
                print(each_picurl)
                path = "C:\\Users\\问津\\Desktop\\download\\"
                download_pic(each_picurl,path)
        