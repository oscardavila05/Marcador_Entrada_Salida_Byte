from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('viewmarca/', views.viewmarca, name='viewmarca'),
    path('viewmarcasalida/', views.viewmarcasalida, name='viewmarcasalida'),
    path('viewingresoempleado/', views.viewingresoempleado, name='viewingresoempleado'),
    path('ListaMarcasEntrada/', views.ListaMarcasEntrada, name='ListaMarcasEntrada'),
    path('ListaMarcasSalida/', views.ListaMarcasSalida, name='ListaMarcasSalida'),  
    path('supervisor_panel/', views.supervisor_panel, name='supervisor_panel'),
    path('buscar_marca_individual/', views.buscar_marca_individual, name='buscar_marca_individual'),
    
    
    
]