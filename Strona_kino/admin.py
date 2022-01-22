from django.contrib import admin
from .models import Film , Bilet

#admin.site.register(Film)


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['tytul','kategoria', 'jezyk', 'status', 'rok_produkcji','wyswietlenia' ]


@admin.register(Bilet)
class BiletAdmin(admin.ModelAdmin):
    list_display = ['rodzaj_biletu','cena_biletu','ilosc_biletow']
