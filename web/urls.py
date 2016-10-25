"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from index import views as iv
from ds import views as dsv
from log import views as lv
from weixin import views as wv

from django.contrib import auth

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',iv.index,name='index'),
    url(r'^dsupload/',dsv.dsupload,name='dsupload'),
    url(r'^dbhome/',dsv.index,name='dbhome'),
    url(r'^dsshow/',dsv.dsshow,name='dsshow'),
    url(r'^dschange/(.*?)/',dsv.dschange,name='dschange'),
    url(r'^login/$',lv.mylogin,name='login'),
    url(r'^logout/',lv.mylogout,name='logout'),
    url(r'^signup/', lv.singup, name='signup'),
    url(r'^weixin/', wv.weixin, name='weixin'),
]
