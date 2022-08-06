from django.urls import path
from .views import *


app_name = "info"

urlpatterns = [
    path('', home,name="home"),
    path('setReason/<slug:username>/<slug:reason>/',setReason,name="set"),
    path('setReason/',setReasonPage,name="setpage"),
    path('setReason/<slug:reason>/',setReasonlist,name="setlist"),


    path('charts/', charts,name="charts"),
    path('charts/DonutChart/', DonutChart,name="DonutChart"),
    path('charts/lineChart/', lineChart,name="lineChart"),
    path('charts/lineChart/Percentage/', lineChartPercentage,name="lineChartPercentage"),
    path('charts/radarChart/', radarChart,name="radarChart"),


    path('orders/',ordersPage,name="ordersPage"),
    path('orders/orderingByReason/', orderingByReason,name="orderingByReason"),

]
