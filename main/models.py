from django.db import models
from django.utils.html import mark_safe


class Shoes(models.Model):
    BRAND_CHOICES = [
        ('Uno' , 'Uno'),
        ('Baldi' , 'Baldi'),
        ('Addidas' , 'Addidas'),
        ('Puma' , 'Puma'),
        ('Nike' , 'Nike')
    ]

    image = models.ImageField(upload_to='media', null=True) 

    brand = models.CharField(max_length=10 , choices=BRAND_CHOICES)
    size = models.DecimalField(max_digits=2 , decimal_places=0)
    price = models.PositiveSmallIntegerField()
    model = models.CharField(max_length=30)

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True,  null=True)



    def img_preview(self):
        return mark_safe(f'<img src="{self.image.url}" width="60px">')

    def __str__(self):
        return self.model


    class Meta:
        verbose_name = 'Shoe'
        verbose_name_plural = 'Shoe'
