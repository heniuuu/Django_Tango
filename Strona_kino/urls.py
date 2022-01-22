from . import views

from django.urls import path, include

urlpatterns = [
    path('', views.main_site, name='main_site'),
    path('login', views.login_site, name='login_site')
]


