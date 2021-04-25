"""school_log URL Configuration

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
from django.urls import path, re_path

from log import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path("studentslist", views.studentslist),
    path("addstudent", views.addstudent),
    path("student_info/<int:id>", views.student_info),
    path("student_info/edit/<int:id>", views.edit),
    path('student_info/edit/delete/<int:id>', views.delete)
]
