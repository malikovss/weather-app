from django.db import models

# Create your models here.


class Weather(models.Model):
    region = models.CharField(max_length=50)
    day = models.TextField()
    forecast = models.TextField()
    forecast_desc = models.TextField()
    humidity = models.TextField()
    wind = models.TextField()
    pressure = models.TextField()
    moon = models.TextField()
    sunrise = models.TextField()
    sunset = models.TextField()
    morning = models.TextField()
    afternoon = models.TextField()
    evening = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.region