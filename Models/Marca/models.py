from django.db import models

class Marca(models.Model):
    nommarc = models.CharField(max_length=75)


    def __str__(self):
        return self.nommarc