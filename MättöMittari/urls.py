from django.urls import path
from . import views

app_name = 'MättöMittari'
urlpatterns =[
    path('', views.index, name='index'),
    path('ruoat/', views.ruoat, name='ruoat'),
    path('ruoat/<int:ruoka_id>/', views.ruoka, name='ruoka'),
    path('arvio/<int:ruoka_id>/', views.arvio, name='arvio'),
    path('muuta_arvio/<int:arvio_id>/', views.muuta_arvio, name='muuta_arvio'),
    path('poista_arvio/<int:arvio_id>/', views.poista_arvio, name='poista_arvio'),
]