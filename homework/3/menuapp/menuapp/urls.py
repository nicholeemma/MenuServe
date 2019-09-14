"""menuapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from menuserve.views import index
from menuserve.views import home
from menuserve.views import manageorders
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import staticfiles
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    # url(r'^Menu/', index),
    url(r'^Order/',home,name="Order"),
    url(r'^Submitted-Order/',manageorders,name="manageorder"),
]
