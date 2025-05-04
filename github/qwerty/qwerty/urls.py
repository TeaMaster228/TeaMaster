"""
URL configuration for qwerty project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from vkbot1.views import admin as bot_admin
from vkbot1.views import script as script
from vkbot1.views import get_message, init, admin as bot_admin
from vkbot1.views import client_server as cl_ser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vkbot1/', bot_admin),
    path('vkbot1/', script),
    path('admin/', admin.site.urls),
    path("botVk/", init),
    path("bot_admin/", bot_admin),
    path("client_server/", cl_ser)
]


