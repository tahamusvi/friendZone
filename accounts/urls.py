from django.urls import path
from .views import *


app_name = "accounts"

urlpatterns = [
    path('login/', login,name="login"),
    path('logout/', logout,name="logout"),
    path('signUp/', signUp,name="signUp"),

]
