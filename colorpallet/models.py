from django.db import models


class ColorType(models.Model):
    type = models.CharField('色の系統',max_length=10)

    def __str__(self):
        return self.type


class ColorIndex(models.Model):
    index_alphabet = models.CharField('列名(A)',max_length=2)

    def __str__(self):
        return self.index_alphabet


class Color(models.Model):
    name = models.CharField('色番',max_length=4)
    color_code = models.CharField('Hex',max_length=7)
    index_alphabet = models.ForeignKey(ColorIndex,verbose_name='列名(A)',on_delete=models.PROTECT)
    index_number = models.CharField('列名(1)',max_length=2)
    type = models.ManyToManyField(ColorType, verbose_name='色の系統')


    def __str__(self):
        return self.name
