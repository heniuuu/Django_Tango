from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

# Create your views here.
from Strona_kino.models import Film


def main_site(request):
        return render(request, 'Strona_kino/main_site.html', )

def login_site(request):
    return render(request, 'Strona_kino/login_site.html', )

class FilmsLista(ListView):
    model = Film
    #content_name=''
    #template_name = ''

class FilmsDetale(DetailView):
    model = Film
    #template_name = ''




















