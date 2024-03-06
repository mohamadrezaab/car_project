from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListAPIView
from .models import Car, Person, Fine
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance 
from .serializers import CarSerializer, PersonSerializer, FineSerializer
from rest_framework.permissions import IsAuthenticated


class RedAndBlueCarsListAPIView(generics.ListAPIView):
    serializer_class = CarSerializer
    
    def get_queryset(self):
        colors = self.request.query_params.get('color', None)
        if colors:
            colors_list = colors.split(',')
            return Car.objects.filter(color__in=colors_list)
        return Car.objects.none()

class PersonCreateAPIView(generics.CreateAPIView):
    serializer_class = PersonSerializer

class CarCreateAPIView(generics.CreateAPIView):
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated]


class HeavyCarsInNarrowStreetsListAPIView(generics.ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return Car.objects.filter(is_heavy=True, street_width__lt=20)
    

class ElderlyOwnersCarsListAPIView(generics.ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        elderly_owners = Person.objects.filter(age__gt=70)
        return Car.objects.filter(owner__in=elderly_owners)



class LocationLightCars(generics.ListAPIView):
    serializer_class = FineSerializer
    
    def get_queryset(self):
        # Define target locations
        target_location = Point(51.388187, 35.689197, srid=4326)  # Toll coordinates 1
        distance_threshold = Distance(m=600)

        # Filtering fines based on the locations
        queryset = Fine.objects.filter(
            location__distance_lte=(target_location, distance_threshold),
            car__is_heavy=False  
        )
        return queryset


    
class OwnersWithTrafficViolationListAPIView(generics.ListAPIView):
    serializer_class = PersonSerializer
   
   
    def get_queryset(self):
        return (
            Person.objects
            .annotate(num_violations=Count('charge_violations_count'))
            .filter(num_violations__gt=0)
            .order_by('-num_violations')
        )
