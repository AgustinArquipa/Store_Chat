from django.urls import path, include
from str_cha import views

#urls de la app
urlpatterns = [
    path('', views.productIndex , name='index')
]
