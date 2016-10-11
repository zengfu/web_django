from django.shortcuts import render
from django import forms
from .models import ic
from django.http import HttpResponse
from reportlab.pdfgen import canvas

# Create your views here.

class DSForm(forms.Form):
    mypn= forms.CharField()
    value= forms.CharField()
    type=forms.CharField()
    description=forms.CharField()
    venderpn =forms.CharField(required=False)
    datasheet = forms.FileField()
    refdesign = forms.URLField(required=False)
    refcode = forms.FileField(required=False)
    refsch = forms.FileField(required=False)


def dsupload(request):
    if request.method=='POST':
        form=DSForm(request.POST,request.FILES)
        if form.is_valid():

            cd=form.cleaned_data
            print cd['datasheet']
            ic1=ic(mypn=cd['mypn'],value=cd['value'],
                   type=cd['type'],description=cd['description'],venderpn=cd['venderpn'],
                   datasheet=cd['datasheet'],refdesign=cd['refdesign'],refcode=cd['refcode'],
                   refsch=cd['refsch'])
            ic1.save()
            return HttpResponse("ok")
    else:
        form = DSForm(
            initial={'subject': 'I love your site!'})
    return render(request,'ds_upload.html',{'form':form})
def show(request):
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='filename="cp2103.pdf"'
    p = canvas.Canvas(response)

    p.drawString(100, 100, "Hello world.")
    p.showPage()
    p.save()
    return response