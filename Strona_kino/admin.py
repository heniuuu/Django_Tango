from django.contrib import admin
from .models import Post , Film
# Register your models here.
admin.site.register([Post, Film])