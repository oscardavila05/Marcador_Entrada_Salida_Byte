from django.urls import path
from . import views

urlpatterns = [
    path('viewmarca/', views.viewmarca, name='viewmarca'),
    path('viewingresoempleado/', views.viewingresoempleado, name='viewingresoempleado'),
    
]