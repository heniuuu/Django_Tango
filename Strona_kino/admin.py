from django.contrib import admin

from .models import Film

#admin.site.register(Film)
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['tytul','kategoria', 'jezyk', 'status', 'rok_produkcji','wyswietlenia' ]
