#-*-coding:utf8-*-

import re
import string
import sys
import os
import urllib
import urllib2
from BeautifulSoup import BeautifulSoup
import requests
from lxml import etree

reload(sys)
sys.setdefaultencoding('utf-8')
if(len(sys.argv) >=2):
    user_id = (int)(sys.argv[1])
else:
    user_id = (int)(raw_input(u"请输入user_id: "))

cookie={"Cookie":"_T_WM=f07f8247c1cd4448233388946c5d7bde; SCF=AvIUxBL7l0HvD65qHT9pOCJU_hNnxCYLhxw-8X55W90cXmkKCEYxrLhcTTwuq85rH_ZgcfvWhpLgc19iTMzKyNI.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWPqbDg2u21hlE1bLKZmxq_5JpX5o2p5NHD95Qfe0efSh5Ne0e7Ws4DqcjbPNiLIgUVMEH8Sb-4BEHW1FH8SCHFeFHWSEH81CHWeE-RxBtt; SUB=_2A250FDaADeRhGeNN6FcV8CnPyDyIHXVX91rIrDV6PUJbkdANLVrhkW0QaLkY17Tcq2_0XWrKCy4fI44dIg..; SUHB=0nluMpzagqBk02; SSOLoginState=1494238930; H5_INDEX=3; H5_INDEX_TITLE=_reigns%E6%9C%A8%E5%B0%A7%E9%A3%8E; M_WEIBOCN_PARAMS=featurecode%3D20000320%26lfid%3D2302835335407330%26luicode%3D20000173%26uicode%3D20000174; _T_H5TOWAP=1"}
url = 'http://weibo.cn/u/%d?filter=1&page=1'%user_id

html = requests.get(url, cookies = cookie).content
selector = etree.HTML(html)
pageNum = (int)(selector.xpath('//input[@name="mp"]')[0].attrib['value'])
result = ""
urllist_set = set()
word_count = 1
print u'爬虫准备就绪...'
for page in range(1,pageNum+1):

  #获取lxml页面
  url = 'http://weibo.cn/u/%d?filter=1&page=%d'%(user_id,page)
  lxml = requests.get(url, cookies = cookie).content

  #文字爬取
  selector = etree.HTML(lxml)
  content = selector.xpath('//span[@class="ctt"]')
  for each in content:
    text = each.xpath('string(.)')
    if word_count >= 4:
      text = "%d :"%(word_count-3) +text+"\n\n"
    else :
      text = text+"\n\n"
    result = result + text
    word_count += 1

fo = open("/home/reigns/%s"%user_id, "wb")
fo.write(result)
word_path=os.getcwd()+'/%d'%user_id
print u'文字微博爬取完毕'
print u'原创微博爬取完毕，共%d条，保存路径%s'%(word_count-4,word_path)
