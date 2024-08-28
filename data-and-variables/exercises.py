shuttle_name = "Determination"
shuttle_speed_mph= 17500
distance_to_mars_km = 225000000
distance_to_moon_km = 384400
miles_per_kilometer = 0.621
print(type("Determination"))
print(type(17500))
print(type(225000000))
print(type(384400))
print(type(0.621))
miles_to_mars = distance_to_mars_km * miles_per_kilometer
hours_to_get_to_mars = miles_to_mars/shuttle_speed_mph
days_to_mars = hours_to_get_to_mars/24
print(shuttle_name  +  "will take"  +  str(days_to_mars)  +  "days to reach Mars.")
shuttle_name = "Determination"
shuttle_speed_mph= 17500
distance_to_mars_km = 225000000
distance_to_moon_km = 384400
miles_per_kilometer = 0.621
print(type("Determination"))
print(type(17500))
print(type(225000000))
print(type(384400))
print(type(0.621))
miles_to_moon = distance_to_moon_km * miles_per_kilometer
hours_to_get_to_moon = miles_to_moon/shuttle_speed_mph
days_to_moon = hours_to_get_to_moon/24
print(shuttle_name  +  "will take"  +  str(days_to_moon)  +  "days to reach Moon.")
