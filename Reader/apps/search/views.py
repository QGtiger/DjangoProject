from django.shortcuts import render
from django.http import HttpResponse
import re
import requests
from urllib.request import quote
import json
from bs4 import BeautifulSoup
from .pexels_image import *

index_url = 'https://www.qu.la'
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

def search_book(url):
    html = requests.get(url).text
    res = {"code":0,"message":"success","totalCount":0,"result":[]}
    search_info = re.findall('<span.*?class="s2"><a.*?href="(.*?)".*?>(.*?)</a>.*?</span>.*?<span.*?class="s4">(.*?)</span>.*?<span.*?class="s6">(.*?)</span>',html,re.S)
    for i in range(len(search_info)):
        res['result'].append({"url":search_info[i][0],"bkname":str.strip(search_info[i][1]),"author":search_info[i][2],"latest":search_info[i][3]})
    res['totalCount'] = len(search_info)
    # print(res)
    return json.dumps(res)

def getBookinfo(url):
    if url == 'none':
        return "There is no url..."
    html = requests.get(url,headers=header).text
    res = {"code":0,"message":"success","book_img":"http://pjas65wzi.bkt.clouddn.com/39.jpg","book_info":"","totalCount":0,"latest":[],"result":[]}
    img = re.findall('<div.*?id="fmimg">.*?<img.*?src="(.*?)".*?>',html,re.S)
    book_img = index_url+img[0]
    info = re.findall('<div.*?id="intro">(.*?)</div>',html,re.S)[0]
    re_html = re.findall('<dt.*?<dt>.*?</dt>(.*)</dd>',html,re.S)
    book_zj = re.findall('<dd>.*?<a.*?href="(.*?)".*?>(.*?)</a>.*?</dd>', re_html[0], re.S)
    for i in range(len(book_zj)):
        res['result'].append({'url':index_url+book_zj[i][0],'zj_name':book_zj[i][1]})
    res['book_img'] = book_img
    res['book_info'] = info
    res['totalCount'] = len(book_zj)
    res['latest'].extend(res['result'][-10:])
    return json.dumps(res)


def getbBookContent(url):
    book_url = url.replace(url.split('/')[-1],'')
    html = requests.get(url,headers = header).text
    content = re.findall('<div.*?id="content">(.*?)</div>',html,re.S)[0].replace('<br/>','\n')
    p = re.findall('<a.*?id="A1".*?href="(.*?)".*?</a>',html,re.S)[0]
    pre = p if p != './' else 'none'
    n = re.findall('<a.*?id="A3".*?href="(.*?)".*?</a>',html,re.S)[0]
    next = n if n!='./' else 'none'
    res = {"code": 0, "message": "success","content": content,"pre":book_url+pre,"next":book_url+next}

    return json.dumps(res)


def getPexelsImage(kyword,img_num):
    enword = YouDao(kyword)
    imglist = getPexelPic(enword,img_num)
    res = {"code":0,"message":"success","type":enword,"result":imglist}
    return json.dumps(res)

# Create your views here.
def search(request):
    if request.method == 'POST':
        pass
    else:
        if request.GET.get('bkname'):
            bkname = request.GET.get('bkname')

        else:
            bkname = 'none'

        return HttpResponse(search_book('https://sou.xanbhx.com/search?siteid=qula&q='+quote(bkname)))

def searchBookinfo(request):
    if request.method == 'POST':
        pass
    else:
        if request.GET.get('url'):
            url = request.GET.get('url')
        else:
            url = 'none'
        return HttpResponse(getBookinfo(url))

def getContent(request):
    if request.method == 'POST':
        pass
    else:
        if request.GET.get('url'):
            url = request.GET.get('url')
        else:
            url = 'none'
        return HttpResponse(getbBookContent(url))

def getImage(request):
    if request.method == 'POST':
        pass
    else:
        if request.GET.get('kyword'):
            kyword = request.GET.get('kyword')
        else:
            kyword = 'none'
        if request.GET.get('imgnum'):
            img_num = request.GET.get('imgnum')
        else:
            img_num = 15
        return HttpResponse(getPexelsImage(kyword,img_num))