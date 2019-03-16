"""np URL Configuration

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
from navp import views as navp_views
from np_users import views as np_users_views
from django.contrib.auth import views as auth_views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', navp_views.home,name = "home"),
    path('register/', np_users_views.signUpForm,name = "register"),
    path('login/', auth_views.LoginView.as_view(template_name='np_users/login.html'),name = "login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='np_users/logout.html'),name = "logout"),
    path('profile/', np_users_views.profile,name = "profile"),


]
urlpatterns+=staticfiles_urlpatterns()
