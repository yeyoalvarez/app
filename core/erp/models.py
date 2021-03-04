from django.db import models

from datetime import datetime


# Create your models here.


class Usuarios(models.Model):
    names = models.CharField(max_length=150, verbose_name='Nombres')

    ci = models.CharField(max_length=10, unique=True, verbose_name='ci')

    contrasena = models.CharField(max_length=150, verbose_name='contrasena')

    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha de registro')

    date_creation = models.DateTimeField(auto_now=True)

    age = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Usuarios'

        verbose_name_plural = 'Usuarios'

        db_table = 'usuarios'

        ordering = ['id']