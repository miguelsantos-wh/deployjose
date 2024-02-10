from django.db import models


# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
