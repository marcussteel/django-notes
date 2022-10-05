from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30) 
    last_name= models.CharField(max_length=30)
    number = models.IntegerField()
    description = models.TextField(null=True, blank=True) #birisi frontend biri backend ile ilgili
    register_date = models.DateField(auto_now_add=True) #burası ilk kayıt alıyor bırakıyor sonra değişmiyor
    last_update = models.DateTimeField(auto_now=True) # autonow yeniliyor kendini
    is_active = models.BooleanField(default=True)


