from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Cities(models.Model):

    code=models.CharField(max_length=20, verbose_name='Regional_Abbreviation')
    name = models.CharField(max_length=20, verbose_name='city_name')


    class Meta:
        db_table = 'tb_cities'
        verbose_name = 'cities'

    def __str__(self):
        return self.name


class Hotels(models.Model):
    # code = models.CharField(max_length=20, verbose_name='Regional_Abbreviation')
    code = models.ForeignKey('Cities', on_delete=models.SET_NULL, related_name='hotels', null=True,  verbose_name='hotels')
    hotel_code=models.CharField(max_length=20, verbose_name='Hotel_code')
    name = models.CharField(max_length=50, verbose_name='Hotel_name')
    class Meta:
        db_table = 'tb_hotels'
        verbose_name = 'hotels'

    def __str__(self):
        return self.name

class Users(User):
    class Meta:
        verbose_name = 'user_info'
        verbose_name_plural = verbose_name
        db_table = 'User'