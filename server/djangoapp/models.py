# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # Add any other fields you want to include in the CarMake model

    def __str__(self):
        return self.name


class CarModel(models.Model):
    CAR_TYPES = (
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        # Add more car types as needed
    )

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(choices=CAR_TYPES, max_length=10)
    year = models.IntegerField(validators=[MinValueValidator(2015), MaxValueValidator(2023)])
    # Add any other fields you want to include in the CarModel model

    def __str__(self):
        return self.name
