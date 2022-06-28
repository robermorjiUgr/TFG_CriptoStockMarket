"""CriptoStockMarket URL Configuration

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
from django.urls import path, include
from CriptoTracking import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', v.register, name="register"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('userProfile/', v.userProfile, name="userProfile"),
    path('', v.home, name="home"),
    path('visualizar/<criptomoneda>', v.visualizar_criptomoneda, name="visualizar_criptomoneda"),
    path('resumen/', v.resumen_criptomonedas, name="resumen_criptomonedas"),
    path('comparar/', v.comparar_criptomonedas, name="comparar_criptomonedas"),
    path('comparar_prediccion/', v.comparar_prediccion_criptomonedas, name="comparar_prediccion_criptomonedas"),
    path('prediction/', v.prediction, name="prediction"),
    path('ranking/', v.ranking_criptomonedas, name="ranking"),
    path('simulacion/', v.simulacion, name="simulacion")
]