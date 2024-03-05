from django.contrib import admin
from django.contrib.gis import admin
from .models import Car, Person, Fine

@admin.register(Person)
class CarAdmin(admin.OSMGeoAdmin):
    pass



@admin.register(Car)
class CarAdmin(admin.OSMGeoAdmin):
    pass


@admin.register(Fine)
class CarAdmin(admin.OSMGeoAdmin):
    pass