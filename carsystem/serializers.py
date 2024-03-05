from rest_framework import generics
from rest_framework import serializers
from .models import Person, Car, Fine
from rest_framework_gis.serializers import GeoFeatureModelSerializer

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'



class FineSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Fine
        geo_field = "location"
        fields = '__all__'



        
  