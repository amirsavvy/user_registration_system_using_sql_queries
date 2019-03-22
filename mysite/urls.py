"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from myapp.views import index, get_register, post_register, get_login, post_login, get_logout,dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^get_register/$', get_register, name='get_register'),
    url(r'^post_register/$', post_register, name='post_register'),
    url(r'^get_login/$', get_login, name='get_login'),
    url(r'^post_login/$', post_login, name='post_login'),
    url(r'^get_logout/$', get_logout, name='get_logout'),
    url(r'^dashboard/$', dashboard, name='dashboard')
]
