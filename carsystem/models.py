from django.db import models
from django.contrib.gis.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    national_code = models.CharField(max_length=10)
    age = models.PositiveIntegerField()
    charge_violations_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Car(models.Model):
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    length = models.FloatField()
    is_heavy = models.BooleanField(default=False)
    street_width = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.type}"
    
class Fine(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    toll_per_cross = models.IntegerField()
    duration = models.IntegerField()  # in days
    issued_at = models.DateTimeField(auto_now_add=True)
    location = models.PointField(srid=4326)

    
    def __str__(self):
        return f"{self.car}"
