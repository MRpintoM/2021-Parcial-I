from django.db import models

class Categoria(models.Model):
    nomcat = models.CharField(max_length=75)



    def __str__(self):
        return self.nomcat