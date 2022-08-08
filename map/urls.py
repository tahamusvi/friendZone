from django.urls import path
from .views import *


app_name = "map"

urlpatterns = [
    path('map/', CreateMapdjango,name="mapPersonCity"),

]
