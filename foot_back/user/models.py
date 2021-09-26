from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField
# Create your models here.
class User(AbstractUser):
    # id = models.CharField(primary_key=True,max_length=20)
    shoe_size = models.CharField(verbose_name = 'Размер стопы',max_length=5,null=True)
    age = models.IntegerField(verbose_name='Возраст',null=True)
    # username = CharField(max_length=100 , null=True)
