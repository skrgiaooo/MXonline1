"""MXonline1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.users import views
import xadmin
from apps.users.views import LoginView
from django.views.generic import TemplateView
from django.conf.urls import url,include
from django.views.static import serve
from MXonline1.settings import MEDIA_ROOT
# from apps import organizitions
# # from apps.organizitions.views import OrgView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/',xadmin.site.urls),
    # path('',views.index)
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('login/',LoginView.as_view(),name='login'),
    #配置授课机构列表展示
    # path('orglist/',OrgView.as_view(),name='org_list')
    url(r'^org/',include(('apps.organizitions.urls','organizitions'),namespace='org')),
    # 配置上传文件的访问url
    url(r'^media/(?P<path>.*)$',serve,{'document_root':MEDIA_ROOT}),
]
