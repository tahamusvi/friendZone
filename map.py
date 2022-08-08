import folium



#Create map
map = folium.Map(location=[32.29,52.95],zoom_start=6)
print("ok this")
#save Map
map.save("map1.html")
