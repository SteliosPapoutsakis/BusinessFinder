from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from enum import IntEnum
import datetime
#DROP DATABASE IF EXISTS `businessfinderdb`; CREATE DATABASE `businessfinderdb` DEFAULT CHARACTER SET utf8 DEFAULT COLLATE utf8_general_ci; USE 'mysql'; GRANT ALL PRIVILEGES ON mydb.* TO 'webappuser'@'75.164.93.129' IDENTIFIED BY 'hack20up' WITH GRANT OPTION; FLUSH PRIVILEGES;

class CompanyTypes(IntEnum):
    RESTAURANT = 1
    RECREATION = 2
    GOODS = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

#c = Company(type=CompanyTypes.RECREATION, name='Chicken Shack', address='5000 N Willamette Blvd', ulr='google.com')

# Create your models here.
class Company(models.Model):
    type = models.IntegerField(choices=CompanyTypes.choices()
        , default=CompanyTypes.RESTAURANT)
    name = models.CharField(default='Invalid Name',
        max_length=100)
    address = models.CharField(default='123 N Ali Ave',
        max_length=150)
    url = models.TextField(default='google.com')
    start_time = models.TimeField(
        default=datetime.datetime(2020, 8, 30, 6, 00, 00))
    end_time = models.TimeField(
        default=datetime.datetime(2020, 8, 30, 17, 0, 0))
    coordinatesLat = models.FloatField(default=0.0)
    coordinatesLon = models.FloatField(default=0.0)
    description = models.TextField(default='', max_length=512)
    rating = models.FloatField(
        default=5.0,
        validators=(
            MinValueValidator(0.0), MaxValueValidator(5.0)
        )
    )    
    activities = models.TextField(default='Wears Facemasks',
        max_length=1024)

    def __str__(self):
        return self.name

    def get_company_type_label(self):
        return CompanyTypes(self.type).name.title()

#class Activity(models.Model):
#    title = models.CharField(default='Invalid Name',
#        max_length=100)
#    description = models.TextField(default='',
#        max_length=500)
#    company = models.ForeignKey(Company, on_delete=models.CASCADE)

#    def __str__(self):
#        return self.title
