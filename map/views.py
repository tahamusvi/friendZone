from django.shortcuts import render
import folium
from accounts.models import City



def setColor(amount):
    if(amount<5):
        return 'gray'
    elif(amount < 15):
        return 'orange'
    elif(amount < 25):
        return 'red'
    else:
        return 'maroon'


def CreateMap(cities):
    #Create map
    map = folium.Map(location=[32.29,52.95],zoom_start=6, tiles = "CartoDB dark_matter")

    #  marker
    # folium.Marker(location=[35.7,51.4], popup = "Google HQ", icon=folium.Icon(color = 'gray')).add_to(map)
    # circle
    # folium.CircleMarker(location=[35.7, 51.4], radius = 9, popup=str("Tehran"), fill_color='red', color="gray", fill_opacity = 0.9).add_to(map)



    # add circles for cities

    for city in cities:
        folium.CircleMarker(location=[city.north,city.east], radius = 6, popup=str(city.user.all().count())+' person - '+city.name, fill_color=setColor(city.user.all().count()), color="black", fill_opacity = 0.9).add_to(map)


    #save Map
    map.save("map/templates/map/map1.html")



def CreateMapdjango(request):
    cities = City.objects.all()
    CreateMap(cities)
    return render(request,'map/map1.html')
