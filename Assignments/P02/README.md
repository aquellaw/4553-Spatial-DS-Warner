## P02 - Cities with the most UFO sightings
### Aquella Warner
### Description 
This project reads data from two files and loads at least one of the data files into a geopandas geoseries spatial index. Using the cities.geoson file, the distance us calculated from each city to every other city and store those values in either json file. After calculating the distance between cities, UFO sightings are assigned to a particular city by finding the average distance to the 100 closest UFO's and is stored in a json file.  

|   #   | File                      | Description                                        |
| :---: | ---------------           | -------------------------------------------------- |
|   1   | main.py                   | Main driver of my project that launches program.      |
|   2   | cities.geojson          | Contains cities data           |
|   3   | ufo_data.csv           | Contains UFO data.                       |
|   4   | ufoSubset.csv           | Contains a subset of the UFOdata.                       |
|   4   | cities_distance.json| Contains a json object with cities and the distances from each city to every other city.                      |
|   4   | ufos_distance.json           | Contains a json object with cities, distances from each city to every other city, and the average distance to the closest UFO's                    |





### Instructions
This program ran with the ufoSubset.csv file so results will differ if the full ufo_data.csv file is used. All other files must be downloaded for this project to run.


