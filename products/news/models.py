from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField('Название', max_length=50)
    text = models.TextField('Текст')
    sena = models.IntegerField('Цена')
    gram = models.IntegerField('Грам')
    def __str__(self):
        return  self.name
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"