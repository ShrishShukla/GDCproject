from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class SensorData(models.Model):
    Location = models.CharField(max_length=100)
    Voltage_value = models.IntegerField() 
    Current_value = models.IntegerField() 
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Location