import json
import random

def randColor():
    r = lambda: random.randint(0,255)
    return ('#%02X%02X%02X' % (r(),r(),r()))

def makeLineString(x,y):
    #x and y contain cooridinates for different points
    #both are appended to create a line between each point
    feature = {
        "type": "Feature",
        "properties": {
        "stroke":randColor(),
        "stroke-width":3
        },
        "geometry": {
        "type": "LineString",
        "coordinates": []
        }
    }

    feature["geometry"]["coordinates"].append(x)
    feature["geometry"]["coordinates"].append(y)
        
    return feature

   
    return points

def makePoint(city, count):

    feature = {
        "type": "Feature",
        "properties": {
            "marker-color":randColor(),
            "marker-symbol": 0
        },
        "geometry": {
            "type": "Point",
            "coordinates": [0,0]
        }  
    }

    for key,val in city.items():
        #if the key is latitude
        if key == 'latitude':
            #store the value of latitude in 1th index of the coordinates list
            feature['geometry']['coordinates'][1] = val
        elif key == 'longitude':
            #store the value of latitude in 0th index of the coordinates list
            feature['geometry']['coordinates'][0] = val
        else:
            #store everything else as a key in the properties value object and make val their values
            feature['properties'][key] = val

        #gives each marker a unique value  
        if feature['properties']['marker-symbol'] == 0:
            feature['properties']['marker-symbol'] = count
    
    return feature

def getCoordinates(points):

    xyCoords = []
    #gets all the coordinates from points list 
    for items in points:
        for item in items["geometry"]:
            if item == "coordinates":
                xyCoords.append(items["geometry"]["coordinates"])
    return xyCoords

def highestPop(x):
    hiPopCity = []

    #Loops through list of objects
    for state in x:
        hiPop = 0
        #for each item in object 
        for item in x[state]:
            #if the population is greater than hipop (initially set as 0)
            if item['population'] > hiPop:
                #let hipop equal to the value of that population and city contain the info for city w/ highest pop 
                hiPop = item['population']
                city = item
        #Make the state a key, and the value the city's details
        hiPopCity.append(city)

    #Sorts dictionary list on x coordinate
    hiPopCity = sorted(hiPopCity, key = lambda i: (i['longitude']))
    
    return hiPopCity

with open("cities_latlon_w_pop.json", "r") as f:
    data = json.load(f)

statesDat = {}

for cities in data:
    #excluding hawaii and alaska
    if cities["state"] != "Hawaii" and cities["state"] != "Alaska":
        #If state not in statesDat dict
        if cities["state"] not in statesDat:
                #set state as a key and let value be an empty list
                statesDat[cities["state"]] = []

        #Appends cities to a particular state
        statesDat[cities["state"]].append(cities)


points = []
states = highestPop(statesDat)

#Loops through states, grabs state info (object) and passes it into makePoint
#function to make points for geojson file.
#count is passed ot help give each marker a unique symbol
count = 1
for state in states:
    points.append(makePoint(state, count))
    count += 1

#holds coordinates for all the cities
coordinates = getCoordinates(points)

#loops throug coordinates lists, passes i & i+1 values from coordinates list to makeLineString function
# appends features to points list 
for i in range(len(coordinates)):
    if i+1 < len(coordinates):
        points.append(makeLineString(coordinates[i],coordinates[i+1]))

#writes points to geojson file
with open("cities.geojson", "w") as f:
    json.dump(points,f,indent=4)
