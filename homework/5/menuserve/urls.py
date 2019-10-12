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
from menuserve.views import (managermain,manageremployee,managerstore,managermenu,managermanager,registration,registration_confirmation,manageruser,logout)
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import staticfiles
from django.views.static import serve
from django.conf.urls import  include, url

# Use include() to add URLS from the catalog application and authentication system


#Add Django site authentication urls (for login, logout, password management)



urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    # path('admin/', admin.site.urls),
    # path('',index,name="index"),
    # url(r'^Menu/', index),
    url(r'^accounts/logout/$', logout,name="logout"),
    url(r'^Order/',home,name="Order"),
    url(r'^Submitted-Order/',manageorders,name="manageorder"),
    url(r'^Manager-Main/',managermain,name="managermain"),
    url(r'^Manager-Employee/',manageremployee,name="manageremployee"),
    url(r'^Manager-Store/',managerstore,name="managerstore"),
    url(r'^Manager-Menu/',managermenu,name="managermenu"),
    url(r'^Manager-Manager/',managermanager,name="managermanager"),
    url(r'^Manager-User/',manageruser,name="manageruser"),
    url(r'^registration/',registration,name="registration"),
    url(r'^registration_confirmation/',registration_confirmation,name="registration_confirmation"),
   #s url(r'^media/(?P<path>.*)$', serve, {"document_root":settings.MEDIA_URL}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
