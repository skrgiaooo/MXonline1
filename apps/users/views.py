from django.shortcuts import render
from django import views
from django.http import HttpResponse,HttpResponseRedirect
from apps.users import form
from django.contrib.auth import authenticate,login
from django.urls import reverse
# Create your views here.
def index(request):
    return render(request,'index.html')
class LoginView(views.View):
    def get(self,request,*args,**kwargs):
        return render(request,'login.html')
    def post(self,request,*args,**kwargs):
        # return HttpResponse('ok')
        login_form = form.LoginForm(request.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=user_name,password=password)
            if user is not None:
                #查询到用户信息不为空
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request,'login.html',{'msg':'用户名或密码错误','login_form':login_form})
        else:
            return render(request,'login.html',{'login_form':login_form})