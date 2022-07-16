"""Entrega URL Configuration

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
from App_mvt.views import mostrar_index, mostrar_busqueda, mostrar_carga
from App_mvt.views import cargar_cliente, buscar_cliente
from App_mvt.views import cargar_coin, buscar_coin
from App_mvt.views import cargar_operacion, buscar_operacion

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', mostrar_index),
    path('carga/', mostrar_carga),
    path('busqueda/', mostrar_busqueda),
    path('cargar-cliente/', cargar_cliente),
    path('buscar-cliente/',buscar_cliente),
    path('cargar-coin/', cargar_coin),
    path('buscar-coin/',buscar_coin),
    path('cargar-operacion/', cargar_operacion),
    path('buscar-operacion/',buscar_operacion),
  
]
