"""
URL configuration for taskmate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from Todolist_app import views as todolist_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',todolist_views.index, name='index'),
    path('todolist/',include('Todolist_app.urls')),
    path('account/',include('users_app.urls')),
    path('Contact',todolist_views.Contact,name="Contact"),
    path('About',todolist_views.About,name="About"),
    
]
