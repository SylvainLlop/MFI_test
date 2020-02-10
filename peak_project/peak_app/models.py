from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Peak(models.Model):
    """ Peak model """
    name = models.CharField(max_length=200, unique=True)
    lat = models.FloatField(default=0.0, validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)])
    lon = models.FloatField(default=0.0, validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)])
    altitude = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(10000.0)])

    def __str__(self):
        return self.name
