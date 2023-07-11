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
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('sitemap.xml', views.sitemap_xml, name='sitemap_xml'),
    path('admin/', admin.site.urls),
    path('RtelecomeM/', views.RTelecomeM, name='RTelecomeM'),
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
    path('universite/', views.universite, name='universite'),
    path('st1er/', views.st1er, name='st1er'),
    path('sts1/', views.sts1, name='sts1'),
    path('sts2/', views.sts2, name='sts2'),
    path('mi/', views.mi, name='mi'),
    path('mis1/', views.mis1, name='mis1'),
    path('mis2/', views.mis2, name='mis2'),
    path('google2f06530ea95f0b86.html', TemplateView.as_view(template_name='google2f06530ea95f0b86.html')),
    path('droitl1/', views.droitl1, name='droitl1'),
    path('droitl1s1/', views.droitl1s1, name='droitl1s1'),
    path('droitl1s2/', views.droitl1s2, name='droitl1s2'),
    path('autol2s1/', views.autol2s1, name='autol2s1'),
    path('st/', views.st, name='st'),
    path('ge/', views.GE, name='GE'),
    path('auto/', views.auto, name='auto'),
    path('autol2', views.autol2, name='autol2'),
    path('l2s1/', views.autol2s1, name='l2s1'),
    path('autol2s2/', views.autol2s2, name='autol2s2'),
    path('autol3/', views.autol3, name='autol3'),
    path('autol3s1/', views.autol3s1, name='autol3s1'),
    path('autol3s2/', views.autol3s2, name='autol3s2'),
    path('electronique/', views.electronique, name='electronique'),
    path('electroniquel2/', views.electroniquel2, name='electroniquel2'),
    path('electroniquel2s2/', views.electroniquel2s2, name='electroniquel2s2'),
    path('electroniquel3/', views.electroniquel3, name='electroniquel3'),
    path('electroniquel3s1/', views.electroniquel3s1, name='electroniquel3s1'),
    path('electroniquel3s2/', views.electroniquel3s2, name='electroniquel3s2'),
    path('telecome/', views.telecome, name='telecome'),
    path('telecomel2/', views.telecomel2, name='telecomel2'),
    path('telecomel2s2/', views.telecomel2s2, name='telecomel2s2'),
    path('telecomel3/', views.telecomel3, name='telecomel3'),
    path('telecomel3s1/',views.telecomel3s1, name='telecomel3s1'),
    path('telecomel3s2/',views.telecomel3s2, name='telecomel3s2'),
    path('biomedical/', views.biomedical, name='biomedical'),
    path('biomedicall2/', views.biomedicall2, name='biomedicall2'),
    path('biomedicall2s2/', views.biomedicall2s2, name='biomedicall2s2'),
    path('biomedicall3/', views.biomedicall3, name='biomedicall3'),
    path('biomedicall3s1/', views.biomedicall3s1, name='biomedicall3s1'),
    path('biomedicall3s2/', views.biomedicall3s2, name='biomedicall3s2'),
    path('electrotechnique/', views.electrotechnique, name='electrotechnique'),
    path('electrotechniquel2/', views.electrotechniquel2, name='electrotechniquel2'),
    path('electrotechniquel2s2/', views.electrotechniquel2s2, name='electrotechniquel2s2'),
    path('electrotechniquel3/', views.electrotechniquel3, name='electrotechniquel3'),
    path('electrotechniquel3s1/', views.electrotechniquel3s1, name='electrotechniquel3s1'),
    path('electrotechniquel3s2/', views.electrotechniquel3s2, name='electrotechniquel3s2'),

]   
