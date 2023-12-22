from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('viewmarca/', views.viewmarca, name='viewmarca'),
    path('viewmarcasalida/', views.viewmarcasalida, name='viewmarcasalida'),
    path('viewingresoempleado/', views.viewingresoempleado, name='viewingresoempleado'),
    
    
    
]