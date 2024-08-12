# Name: Tahjae Jackson
# Date: November 3, 2021
# Purpose: To create a Cit class that will be used to store data retrieved from a file


class City:
    def __init__(self,code, name, region, population, latitude, longitude):
        self.code = code
        self.name = name
        self.region = region
        self.population = population
        self.latitude = latitude
        self.longitude = longitude


    def __str__(self):
        return (self.name +","+ str(self.population) +","+ str(self.latitude) +","+ str(self.longitude))
