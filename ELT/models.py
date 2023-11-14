from django.db import models

# Create your models here.


class Bookmark(models.Model):
    title = models.CharField(max_length=20)
    opis = models.TextField(max_length=321, default="podaj opis")
    def __str__(self):
        return self.title

