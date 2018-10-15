"""config URL Configuration

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

from school import views

import re

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', views.school_list, name='school-list'),
    url(r'^school_id/(?P<pk>\d+)/$', views.school_detail, name='school-detail'),
    url(r'^student', views.students_list(), name='students-list'),
    url(r'^student_id/(?P<pk>\d+)/$', views.students_detail, name='students-detail'),

]