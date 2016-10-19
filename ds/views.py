from django.shortcuts import render
from django import forms
from .models import ic,choice
from django.db import IntegrityError
import os
from web.settings import BASE_DIR

from django.http import HttpResponse
#from reportlab.pdfgen import canvas

# Create your views here.

def index(request):
    dic=[{'dbname':'Datasheets','url':'dsshow'},
         {'dbname':'Papers','url':'index'}]
    return render(request,'ds_index.html',{'list':dic})

class DSForm(forms.Form):
    mypn= forms.CharField()
    value= forms.CharField()
    type=forms.ChoiceField(choices=choice,required=False)
    description=forms.CharField()
    venderpn =forms.CharField(required=False)
    datasheet = forms.FileField(required=False)
    refdesign = forms.URLField(required=False)
    refcode = forms.FileField(required=False)
    refsch = forms.FileField(required=False)



def dsupload(request):
    if request.method=='POST':
        form=DSForm(request.POST,request.FILES)
        if form.is_valid():
            cd=form.cleaned_data
            ic1=ic(mypn=cd['mypn'],value=cd['value'],
                   type=cd['type'],description=cd['description'],venderpn=cd['venderpn'],
                   datasheet=cd['datasheet'],refdesign=cd['refdesign'],refcode=cd['refcode'],
                   refsch=cd['refsch'])

            try:
                ic1.save()
            except IntegrityError:
                path=os.path.join(BASE_DIR, "media\datasheet\\")
                file=path+str(cd['datasheet'])
                os.remove(file)
                return render(request, 'ds_upload.html', {'form': form,'error_mypn':'Duplicated!','data':form.data})

            return render(request,"ds_sucess.html")


    else:
        form = DSForm(
            initial={'subject': 'I love your site!'})
    return render(request, 'ds_upload.html', {'form':form,})
def dsshow(request):
    a=ic.objects.all()
    result=[]
    for i in a:
        type=choice[int(i.type)][1]
        new={'mypn':i.mypn,'value':i.value,'type':type,'description':i.description,
                       'venderpn':i.venderpn,'datasheet':i.datasheet,'refdesign':i.refdesign,'refcode':i.refcode,
                       'refsch':i.refsch,'time':i.time}
        result.append(new)
    #return HttpResponse('ok')
    return render(request, 'ds_show.html', {'result':result})
def dschange(request,mypn):
    ic1 = ic.objects.filter(mypn=mypn)
    lastds=ic1[0].datasheet
    if request.method == 'POST':
        ic1.delete()
        form = DSForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            if not cd['datasheet']:
                cd['datasheet']=lastds
            else:
                path = os.path.join(BASE_DIR, "media\\")
                file = path + str(lastds)
                os.remove(file)
            ic1 = ic(mypn=cd['mypn'], value=cd['value'],
                     type=cd['type'], description=cd['description'], venderpn=cd['venderpn'],
                     datasheet=cd['datasheet'], refdesign=cd['refdesign'], refcode=cd['refcode'],
                     refsch=cd['refsch'])

            try:
                ic1.save()
            except IntegrityError:
                return render(request, 'ds_change.html', {'form': form, 'error': 'Duplicated!', 'data': form.data})
            return render(request, "ds_sucess.html")
    else:

        form = DSForm(
            initial={'subject': 'I love your site!'})
        for i in ic1:
            data = {'mypn': i.mypn, 'value': i.value, 'type': type, 'description': i.description,
                   'venderpn': i.venderpn, 'datasheet': i.datasheet, 'refdesign': i.refdesign, 'refcode': i.refcode,
                   'refsch': i.refsch,}

        return render(request, 'ds_change.html', {'form': form, 'data': data})
