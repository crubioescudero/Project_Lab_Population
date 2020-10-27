# -*- coding: utf-8 -*-

''' 
World Population

@author: Toñi Reina
REVISED BY: José Antonio Troyano, Daniel Mateos, Mariano González
LAST MODIFICATION: 10/07/2019

In this project we will work with world population data, represented
using lists. We will implement a series of functions that will allow us to display
graphs of population evolution, as well as comparing the population in different
countries.

DATA SETS:
-------------------
The project includes a test data set:
  - population.csv: with population data from different countries or groupings of countries
    in different years.

FUNCTIONS THAT ARE PART OF THE EXERCISE:
-----------------------------------------
- read_populations (file):
    reads the input file and returns a list of tuples
    (country_name, country_code, year, number_inhabitants)
- calculate_countries (populations):
    take a list of tuples (country_name, country_code, year, num_inhabitants)
    and returns an ordered list with the names
    of the countries or sets of countries for which there is data
- filter_by_country (towns, country):
    takes a list of tuples (country_name, country_code, year, number_inhabitants) and
    returns a list of tuples (year, num_inhabitants)
    with the country data that is passed as a parameter.
    The country can be given with its full name or with its code
- filter_by_countries_and_year (populations, year, countries):
    takes a list of tuples (country_name, country_code, year, number_inhabitants) and
    returns a list of tuples (country_name, num_inhabitants)
    with last year's data as a parameter for the countries
    included in the countries parameter.
- show_population_evolution (populations, country):
    take a list of tuples (country_name, country_code, year, num_inhabitants)
    and generates a graph with the evolution of the population
    of the country given as a parameter. The country can be given with its full name or with
    Your code
- show_comparative_countries_year (populations, year, countries):
    takes a list of tuples (country_name, country_code, year, number_inhabitants), a year and
    a group of countries and generates a graph
    of bars with the population of those countries in the year given as a parameter
 

'''
import csv
from matplotlib import pyplot as plt
from collections import namedtuple

Registro = namedtuple('Registro', 'nombre, codigo, año, censo')
########################################################################################
def read_populations(file):
    '''Read the input file and return a list of population tuples
    
    INPUT:
       - file: input file name -> str
    OUTPUT:
       - list of tuples (name, code, year, census) -> [(str, str, int, int)]

    Each line of the file corresponds to the data of a country or group of countries,
    and it is represented by a tuple with the following values:
        - Country name
        - Country code
        - Year
        - Num. Inhabitants of the country in that year
    You have to transform the input (character strings) into numeric values
    in those data that are numeric type.
    '''
    res=list()
    with open(file,"rt",encoding='utf-8') as f:
        misLineas=csv.reader(f)
        for nom,cod,año,num in misLineas:
            res.append(Registro(nom,cod,int(año),int(num)))
    return res
	   
    
############################################################################################

############################################################################################
def calculate_countries(populations):
    '''Calculate the set of countries present in a list of countries
    
    INPUT:
       - populations: list of tuples (name, code, year, census) -> [(str, str, int, int)]
    OUTPUT:
       - list of countries -> [str]

    It takes as input a list of tuples (country, country_code, year, number_inhabitants) and
    produces as output an ordered list with the names of the countries
    for which there is at least one population data.
    The output list will not contain repeating elements.
    '''
    
##############################################################################################

############################################################################################## 
def filter_by_country (towns, country):
    '''Select the tuples corresponding to a specific country
    
    INPUT:
       - populations: list of tuples (name, code, year, census) -> [(str, str, int, int)]
       - country: from which the records will be selected -> str
    OUTPUT:
       - list of tuples (year, census) selected -> [(int, int)]

    It takes as input a list of tuples (country_name, country_code, year, number_inhabitants) and
    produces as output another list of tuples (year, num_inhabitants) with the data of
    population of the country that is passed as a parameter. The country can be indicated
    either giving your full name, or giving your code.
    '''
    
        
##############################################################################################

############################################################################################## 
def filter_by_countries_and_year (populations, year, countries):
   '''Select the tuples corresponding to a set of countries of a specific year
    
    INPUT:
       - populations: list of tuples (name, code, year, census) -> [(str, str, int, int)]
       - year: from which the records will be selected -> int
       - countries: from which the records will be selected -> [str]
    OUTPUT:
       - list of tuples (country, census) selected -> [(str, int)]

    It takes as input a list of tuples (country_name, country_code, year, number_inhabitants) and
    outputs another list of tuples (country_name, num_inhabitants)
    in which only those data are included
    corresponding to the year given as a parameter and of the countries
    included in the countries collection
    '''
    
##############################################################################################

###############################################################################################
def show_population_evolution (populations, country):
   '''Generates a curve with the evolution of the population of a country. The country can
    be given as your full name or by your code.
    
    INPUT:
       - populations: list of tuples (name, code, year, census) -> [(str, str, int, int)]
       - country: from which the graph will be generated -> str
    DISPLAY OUTPUT:
       - diagram with the evolution of the country's census

    It takes as input a list of tuples (country_name, country_code, year, number_inhabitants) and
    produces as an output a graph with the evolution of the country's population given as
    parameter over time.
    
    These are the 'matplotlib' instructions to plot the graph
    starting a string with the title to be displayed on the chart,
    a list of years and another list with the number of inhabitants (in the same order):
        
        plt.title (title)
        plt.plot (l_years, l_inhabitants)
        plt.show ()
    '''
    
            
###############################################################################################

###############################################################################################
def show_comparative_countries_year (populations, year, countries):
    '''Generates a bar graph in which the comparison of
    the population of several countries in a given year
    
    INPUT:
       - populations: list of tuples (name, code, year, census) -> [(str, str, int, int)]
       - year: from which the graph will be generated -> int
       - countries: from which the graph will be generated -> [str]
    DISPLAY OUTPUT:
       - bar chart with the comparison of the census by country

    It takes as input a list of tuples (country_name, country_code, year, number_inhabitants) and
    produces as output a bar graph with the number of inhabitants of the countries
    given as a parameter in the year year.
    Each bar corresponds to a country.
    
    These are the 'matplotlib' instructions to plot the bar chart
    from a string with the chart title,
    a list of country names and another list (in the same order) of
    number of inhabitants of these countries:
       
        plt.title (title)
        index = range (len (l_countries))
        plt.bar (index, l_inhabitants)
        plt.xticks (index, l_countries, fontsize = 8)
        plt.show ()
    '''
    # We calculate the list of populations of the given year for the countries in the list
   
    
###############################################################################################
