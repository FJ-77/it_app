"""it_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from posts import views
from django.urls import path

urlpatterns = [
#______________main_________________
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
#____________friends______________
    path('friends', views.friends, name = 'friends'),
    path('login', views.login, name = 'login'),
#_________________posts____________________________   
    path('posts', views.post_list, name = 'post_list'),
#_________________ADS____________________    
    path('table', views.advertisement_table, name = 'ad_table'),
    path('table/<pk>', views.advertisement_detail, name = 'advert_detail')
]
