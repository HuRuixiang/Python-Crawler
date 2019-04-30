# 观看指南
## 这是我学习Python时写的一些爬虫Demo，享与诸君，多多指教。

### 1、图片爬取picture_crawler1.0.py

+ 简介：picture_crawler1.0.py是用Python requests库和re库写的一个定向网页图片爬取爬虫，可以将指定网页的图片下载到本地的指定目录。
+ 知识点：requests/re库的应用、正则表达式、文件操作、异常处理。

### 1、图片爬取picture_crawler2.0.py

+ 简介：1.0版本的图片爬虫只能爬取单个的网页，但有的图片网站会有一个目录，而每一个目录又是一个单独的页面，在这种情况下1.0版本就不再适用。**picture_crawler2.0.py在1.0的基础上，增加了一个函数，用于获取目录中各个子页面的url**，然后将得到的子页面url传给图片url获取函数，随后再将获取到的图片url传给图片下载函数，完成图片下载。
+ 知识点：同1.0。
