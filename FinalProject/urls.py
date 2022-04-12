"""FinalProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from first import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path('oursite/', views.oursite, name="oursite"),
    path('ps5/', views.PS5, name="ps5"),
    path('xbox/', views.XBOX, name="xbox"),
    path('pc/', views.PC, name="pc"),
    path('search/', views.search, name="search" ),
    #path('fifa22/', fifa22.search, name="fifa22" ),
    #path('callofduty/', callofduty.search, name="callofduty" ),
    #path('ratchetandclank/', ratchetandclank.search, name="ratchetandclank" ),
    #path('forza/', forza.search, name="forza" ),
    #path('halo/', halo.search, name="halo" ),
    #path('ghostrecon/', ghostrecon.search, name="ghostrecon" ),
    #path('minecraft/', minecraft.search, name="minecraft" ),
    #path('fortnite/', fortnite.search, name="fortnite" ),
    #path('pubg/', pubg.search, name="pubg" ),
    path('underdevel/', views.underdevel, name="underdevel" ),

    
    #path('adoptions/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    #path('login', views.LoginInterfaceView.as_view()),  #for login
    #path('signup', views.SignUpView.as_view(), name='signup'),


]
