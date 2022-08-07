from django.urls import path
from .views import *


app_name = "info"

urlpatterns = [
    path('', home,name="home"),

    path('sets/', setsPage,name="setsPage"),


    path('setReason/<slug:username>/<slug:reason>/',setReason,name="set"),
    path('setReason/',setReasonPage,name="setpage"),
    path('setReason/<slug:reason>/',setReasonlist,name="setlist"),

    path('setCity/<slug:username>/<slug:cityName>/',setCity,name="setCity"),
    path('setCity/',setCityPage,name="setCityPage"),
    path('setCity/<slug:cityName>/',setCitylist,name="setCitylist"),


    path('charts/', charts,name="charts"),
    path('charts/DonutChart/', DonutChart,name="DonutChart"),
    path('charts/lineChart/', lineChart,name="lineChart"),
    path('charts/lineChart/Percentage/', lineChartPercentage,name="lineChartPercentage"),
    path('charts/lineChartCity/Percentage/', lineChartPercentageCity,name="lineChartPercentageCity"),
    path('charts/radarChart/', radarChart,name="radarChart"),


    path('orders/',ordersPage,name="ordersPage"),
    path('orders/orderingByReason/', orderingByReason,name="orderingByReason"),
    path('orders/orderingByCity/', orderingByCity,name="orderingByCity"),

]
