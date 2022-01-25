from . import views
from django.urls import path, include
from .views import FilmsLista, FilmsDetale

urlpatterns = [
    path('', FilmsLista.as_view, name='Films_Lista'),
    path('login', views.login_site, name='login_site'),
    # path('film/', FilmsLista.as_view, name='Films_Lista.html'),
]


