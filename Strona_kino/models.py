from django.db import models
from django.db.models import Model

CATEGORY_CHOICE = (
    ('A', 'AKCJA'),
    ('D', 'DRAMAT'),
    ('K', 'KOMEDIA'),
    ('R', 'ROMANS'),
)
LANGUAGE_CHOICE = (
    ('PL', 'POLSKI'),
    ('EN', 'ENGLISH')
)
STATUS_CHOICES = (
    ('ND', 'NIEDAWNO DODANE'),
    ('NO', 'NAJCZĘŚCIEJ OGLĄDANE'),
    ('TR', 'NAJLEPIEJ OCENIANE')
)
BILET_CHOICE = (
    ('N','NORMALNY'),
    ('U','ULGOWY'),
    ('R','RODZINNY'),
)

class Film(models.Model):
    tytul = models.CharField(max_length=100)
    opis = models.TextField(max_length=1000)
    obraz = models.ImageField(upload_to='Strona_kino')
    kategoria = models.CharField(choices=CATEGORY_CHOICE, max_length=1)
    jezyk = models.CharField(choices=LANGUAGE_CHOICE, max_length=2)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    rok_produkcji = models.IntegerField(default=0)
    wyswietlenia = models.IntegerField(default=0)

    def __str__(self):
        return self.tytul

class Bilet(models.Model):
    rodzaj_biletu = models.CharField(choices=BILET_CHOICE, max_length=10)
    cena_biletu = models.IntegerField(default=0)
    ilosc_biletow = models.IntegerField(default=0)
    #film = id(Film)
    #to ma brać konkretny film ale nwm jak to zrobić pog

