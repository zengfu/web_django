from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
# Create your views here.

def mylogin(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username=cd['username']
            password=cd['password']
            print password
            user=authenticate(username=username,password=password)
            login(request,user)
            if request.GET:
                return HttpResponseRedirect(request.GET['next'])
            else:
                return HttpResponseRedirect('/')

        else:
            return render(request, 'login.html', {'form': form,'error':'please enter a correct username and password!'})
    else:
        if request.user.is_authenticated():
            return HttpResponse("logined")
        form=AuthenticationForm()

        return render(request,'login.html',{'form':form})

def mylogout(request):
    logout(request)
    return HttpResponseRedirect('/')
def singup(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print cd
            newuser=User()
            newuser.username=cd['username']
            newuser.set_password(cd['password1'])
            newuser.save()
            user = authenticate(username=cd['username'], password=cd['password1'])
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            a=request.POST['username']
            return render(request, 'signup.html', {'form': form,'data':a})
    else:
        form=UserCreationForm()
        return render(request, 'signup.html', {'form': form})