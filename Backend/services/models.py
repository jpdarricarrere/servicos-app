from django.db import models

# Create your models here.


class ServiceModel(models.Model):
    id = models.IntegerField(primary_key=True, blank=False, default='')
    nome = models.CharField(max_length=255, blank=False, default='')
    categoria = models.CharField(max_length=255, blank=False, default='')
    telefone = models.CharField(max_length=255, blank=False, default='')
    email = models.CharField(max_length=255, blank=False, default='')
    link_imagem = models.CharField(max_length=1023, blank=False, default='')
    contratado = models.BooleanField(default=False)
