from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from enum import IntEnum


class CompanyTypes(IntEnum):
    RESTAURANT = 1
    RECREATION = 2
    GOODS = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

# Create your models here.
class Company(models.Model):
    type = models.IntegerField(choices=CompanyTypes.choices()
        , default=CompanyTypes.RESTAURANT)
    name = models.CharField('Company Name', max_length=100)
    address = models.CharField('Company Address', max_length=150)
 
    hours_start = models.IntegerField('Company Hours Start',
        default=0,
        validators=(
            MinValueValidator(0), MaxValueValidator(24)
        )
    )
    hours_end = models.PositiveIntegerField('Company Hours End',
        default=0,
        validators=(
            MinValueValidator(0), MaxValueValidator(24)
        )
    )
    coordinatesLon = models.FloatField('Coordinates Longitude')
    coordinatesLat = models.FloatField('Coordinates Latitude')
    description = models.TextField('Company Description', max_length=512)
    rating = models.FloatField('Company Rating',
        default=5.0,
        validators=(
            MinValueValidator(0.0), MaxValueValidator(5.0)
        )
    )
    
    def __str__(self):
        return "%s" % (self.name)

    def get_company_type_label(self):
        return CompanyTypes(self.type).name.title()

class Activity(models.Model):
    title = models.CharField('Activity Title',
        max_length=100)
    description = models.TextField('Activity Description',
        max_length=500)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
