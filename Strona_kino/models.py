from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Film(models.Model):
    tytul_filmu = models.CharField(max_length=200)
    id_filmu = models.CharField(max_length=200)
    cena_biletu = models.CharField(max_length=100)
    ocena = models.CharField(max_length=100)
    opis = models.TextField()

    def __str__(self):
        return self.tytul_filmu
        # to robi że w panelu  zamiast obiekt film będzie nazwa filmu
