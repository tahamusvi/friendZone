from django.urls import path
from .views import *


urlpatterns = [
    path('', home),
    # path('cs/',createusers),
    path('addinfo/',addinfo),
]
