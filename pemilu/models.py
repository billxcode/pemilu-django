# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Parpol(models.Model):
    nama = models.CharField(max_length=200)
    keterangan = models.TextField()

class Person(models.Model):
    nama = models.CharField(max_length=200)
    nomor_urut = models.IntegerField(default=0)
    parpol = models.ForeignKey(Parpol, on_delete=models.CASCADE)

class President(models.Model):
    capress = models.ForeignKey(Person, on_delete=models.CASCADE)

class WakilPresident(models.Model):
    cawapress = models.ForeignKey(Person, on_delete=models.CASCADE)

class Terpilih(models.Model):
    capress = models.ForeignKey(President, on_delete=models.CASCADE)
    cawapress = models.ForeignKey(WakilPresident, on_delete=models.CASCADE)
    suara = models.IntegerField