from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('peliculas/', views.peliculas, name='peliculas'),
    path('promociones/', views.promociones, name='promociones'),
    path('dulceria/', views.dulceria, name='dulceria'),
    path('procesar_pago/', views.procesar_pago, name='procesar_pago'),
]