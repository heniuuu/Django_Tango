from . import views
from django.contrib import admin
from django.urls import path, include
from .views import FilmsLista , FilmsDetale
urlpatterns = [
    path('', views.main_site, name='main_site'),
    path('login', views.login_site, name='login_site')
]


urlpatterns1 = [
    path('', FilmsLista.as_view() , name='Films_Lista'),
    path('<int:pk>', FilmsDetale.as_view() , name='Films_Detale'),
]
