#coding:utf-8
from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django import forms
from django.db import IntegrityError
import os
from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import TextMessage
from wechat_sdk import WechatConf

from web.settings import BASE_DIR
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseBadRequest
import hashlib
# Create your views here.
WECHAT_TOKEN = '71451085a'
AppID = ''
AppSecret = ''
import json
import urllib



conf = WechatConf(
    token='71451085a',
    appid='wx65a275d3c1a71d29',
    appsecret='c1e1656bd05b52a4f0858f72b6ef69fa',
    encrypt_mode='normal',  # 可选项：normal/compatible/safe，分别对应于 明文/兼容/安全 模式
    encoding_aes_key='PlrRDX372PXe2b5ORxE0sKMZjY1fqahqQRKmjSksDcb'  # 如果传入此值则必须保证同时传入 token, appid
)
wechat = WechatBasic(conf=conf)
mean={
    'button':[
        {
            'type': 'click',
            'name': '今日歌曲',
            'key': 'V1001_TODAY_MUSIC'
        },
        {
            'type': 'click',
            'name': '歌手简介',
            'key': 'V1001_TODAY_SINGER'
        },
        {
            'name': '菜单',
            'sub_button': [
                {
                    'type': 'view',
                    'name': '搜索',
                    'url': 'http://www.soso.com/'
                },
                {
                    'type': 'view',
                    'name': '视频',
                    'url': 'http://v.qq.com/'
                },
                {
                    'type': 'click',
                    'name': '赞一下我们',
                    'key': 'V1001_GOOD'
                }
            ]
        }
    ]
}
@csrf_exempt
def weixin(request):
    wechat.create_menu()
    if request.method=="GET":
        signature=request.GET['signature']
        timestamp=request.GET['timestamp']
        echostr=request.GET['echostr']
        nonce=request.GET['nonce']
        if wechat.check_signature(signature, timestamp, nonce):
            return HttpResponse(echostr)
        else:
            return HttpResponse(False)
    else:
        try:
            wechat.parse_data(data=request.body)
        except ParseError:
            return HttpResponseBadRequest('Invalid XML Data')
        message = wechat.get_message()
        print message
        response = wechat.response_text(content="test,曾福")
        return HttpResponse(response, content_type="application/xml")
        print wechat.get_access_token()