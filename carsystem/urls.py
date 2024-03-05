from django.urls import path
from . import views
from .views import(
RedAndBlueCarsListAPIView, 
PersonCreateAPIView, 
CarCreateAPIView, 
HeavyCarsInNarrowStreetsListAPIView, 
ElderlyOwnersCarsListAPIView,
OwnersWithTrafficViolationListAPIView,
LocationLightCars
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'carsystem'
urlpatterns = [
    path('api/cars/', RedAndBlueCarsListAPIView.as_view(), name='red_and_blue_cars_list'),
    path('api/register/', PersonCreateAPIView.as_view(), name='person_create'),
    path('api/cars/register/', CarCreateAPIView.as_view(), name='car_create'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/heavy-cars/', HeavyCarsInNarrowStreetsListAPIView.as_view(), name='heavy_cars_in_narrow_streets_list'),
    path('api/elderly-owners-cars/', ElderlyOwnersCarsListAPIView.as_view(), name='elderly_owners_cars_list'),
    path('api/locations-light-cars/', LocationLightCars.as_view(), name='locations_of_light_cars'),
    path('api/owners-with-traffic-violations/', OwnersWithTrafficViolationListAPIView.as_view(), name='owners_with_traffic_violations_list'),
]
