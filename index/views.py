#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import urllib
import re
import urllib2
from bs4 import BeautifulSoup
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from django import forms



# Create your views here.
def index(request):
    if 'search' in request.GET:
        search=request.GET['search'].encode('utf8')
        f1={
        'bing':"https://www.bing.com/search?"+urllib.urlencode({'q':search}),
        'baidu':'https://www.baidu.com/s?'+urllib.urlencode({'wd':search}),
        'google':"https://www.google.com/search?"+urllib.urlencode({'q':search}),
        }
        f2={
            'github':'https://github.com/search?utf8=✓&'+urllib.urlencode({'q':search}),
            'zhihu':"https://www.zhihu.com/search?type=content&"+urllib.urlencode({'q':search}),
            'weibo':"http://s.weibo.com/weibo/"+str(search),
            'quora':"https://www.quora.com/search?"+urllib.urlencode({'q':search})
        }
        f3={
            'taobao':"https://s.taobao.com/search?"+urllib.urlencode({'q':search}),
            'jingdong':"https://search.jd.com/Search?"+urllib.urlencode({'keyword':search})
        }
    if 'bing' in request.GET:
        return HttpResponseRedirect(f1['bing'])
    elif 'baidu' in request.GET:
        return HttpResponseRedirect(f1['baidu'])
    elif 'github' in request.GET:
        return HttpResponseRedirect(f2['github'])
    elif 'google' in request.GET:
        return HttpResponseRedirect(f1['google'])
    elif 'zhihu' in request.GET:
        return HttpResponseRedirect(f2['zhihu'])
    elif 'weibo' in request.GET:
        return HttpResponseRedirect(f2['weibo'])
    elif 'taobao' in request.GET:
        return HttpResponseRedirect(f3['taobao'])
    elif 'jingdong' in request.GET:
        return HttpResponseRedirect(f3['jingdong'])
    elif 'quora' in request.GET:
        return HttpResponseRedirect(f2['quora'])
    elif 'all' in request.GET:
        res1=baidus(f1['baidu'])
        res2=bings(f1['bing'])
        res3=zhihu(f2['zhihu'])
        return render(request,'result.html',{'baidu':res1,'bing':res2,'zhihu':res3})
    else:
        return render(request,'index.html',)





def zhihu(url):
    User_Agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    headers={'User-Agent':User_Agent}
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    html=response.read()
    soup=BeautifulSoup(html,'lxml')
    content=soup.select('.title')
    res=[]
    for i in content:
        item=re.findall('<a class="js-title-link" href="(.*?)" target="_blank">(.*?)</a>',str(i),re.S)
        if item:
            des=re.sub('[(<em>)(</em>)]','',item[0][1])
            a={'href':"http://www.zhihu.com"+str(item[0][0]),'des':des}
            res.append(a)

    return res


def bings(url):
    User_Agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    headers={'User-Agent':User_Agent}
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    html=response.read()
    soup=BeautifulSoup(html,'lxml')
    content=soup.select('.b_algo h2')
    res=[]
    for i in content:
        item=re.findall('<a h="ID=SERP,\d+.1" href="(.*?)" target="_blank">(.*?)</a>',str(i),re.S)
        if item:
            des=re.sub('[(<strong>)(</strong>)]','',item[0][1])
            a={'href':item[0][0],'des':des}
            res.append(a)
    return res

def baidus(url):
    User_Agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    headers={'User-Agent':User_Agent}
    request = urllib2.Request(url,headers=headers)
    response = urllib2.urlopen(request)
    html=response.read()
    soup=BeautifulSoup(html,'lxml')
    content=soup.select('.c-container  h3')
    res=[]
    for i in content:
        item=re.findall('href="(.*?)" target="_blank">\s*(.*?)</a>',str(i),re.S)
        if item:
            des=re.sub('[(<em>)(</em>)]','',item[0][1])
            a={'href':item[0][0],'des':des}
            res.append(a)
    return res