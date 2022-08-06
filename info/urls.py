from django.urls import path
from .views import *


app_name = "info"

urlpatterns = [
    path('', home,name="home"),
    path('setReason/<slug:username>/<slug:reason>/',setReason,name="set"),
    path('setReason/',setReasonPage,name="setpage"),
    path('setReason/<slug:reason>/',setReasonlist,name="setlist"),
]
