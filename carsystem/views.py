from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListAPIView
from .models import Car, Person, Fine
from django.db.models import Count
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
    queryset=Fine.objects.all()
    

class OwnersWithTrafficViolationListAPIView(generics.ListAPIView):
    serializer_class = PersonSerializer
   
   
    def get_queryset(self):
        return (
            Person.objects
            .annotate(num_violations=Count('charge_violations_count'))
            .filter(num_violations__gt=0)
            .order_by('-num_violations')
        )