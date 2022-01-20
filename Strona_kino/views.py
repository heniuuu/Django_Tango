from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.

def main_site(request):
        return render(request, 'Strona_kino/main_site.html', )

def login_site(request):
    return render(request, 'Strona_kino/login_site.html', )
























