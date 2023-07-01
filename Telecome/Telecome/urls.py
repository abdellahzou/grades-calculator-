"""
URL configuration for Telecome project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from calculator import views
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('telecome/', views.Telecome, name='Telecome'),
    path('telecomeM1S1/', views.TelecomeM1S1, name='TelecomeM1S1'),
    path('telecomeM1S2/', views.TelecomeM1S2, name='TelecomeM1S2'),
    path('bac/', views.bac_page, name='bac_page'),
    path('bac_ar/', views.bac_page_ar, name='bac_page_ar'),
    path('fr/', views.home_page, name='home_page'),
    path('', views.home_page_ar, name='home_page_ar'),
    path('math/', views.Math, name='Math'),
    path('MathThechnique/', views.Math_Technique, name='Math thechnique'),
    path('science/', views.science, name='science'),
    path('Gestion/', views.Gestion, name='Gestion'),
    path('LesLangues/', views.les_langues, name='les_langues'),
    path('philo/', views.philo, name='philo'),
    path('st/', views.st, name='st'),
    path('st1er/', views.st1er, name='st1er'),
    path('sts1/', views.sts1, name='sts1'),
    path('sts2/', views.sts2, name='sts2'),
    path('mi/', views.mi, name='mi'),
    path('mis1/', views.mis1, name='mis1'),
    path('mis2/', views.mis2, name='mis2'),
    path('google2f06530ea95f0b86.html', TemplateView.as_view(template_name='google2f06530ea95f0b86.html')),

]
