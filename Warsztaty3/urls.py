"""Warsztaty3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from Address_Book.views import show_person
from Address_Book.views import show_all
from Address_Book.views import show_new
from Address_Book.views import add_new
from Address_Book.views import delete_person
from Address_Book.views import edit_person


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^edit_person/(?P<id>\d+)/$', edit_person),
    url(r'^edit_person_get/(?P<id>\d+)/$', edit_person),
    url(r'^delete_person/(?P<id>\d+)/$', delete_person),
    url(r'^show_person/(?P<id>\d+)/$', show_person),
    url(r'^show_new/(?P<id>\d+)/$', show_new),
    url(r'^add_new/$', add_new),
    url(r'^show_all/$', show_all),
]
