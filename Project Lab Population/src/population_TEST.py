# -*- coding: utf-8 -*-
'''
Created on 12 oct. 2018

@author: Toñi Reina
REVISED BY: José Antonio Troyano, Daniel Mateos, Mariano González
LAST MODIFICATION: 10/07/2019

File with tests for the populations project
'''
from population import *

################################################################
#  Auxiliary functions
################################################################

def show_enumerated(colection):
    i=0
    for p in colection:
        i=i+1
        print (i, p) 
################################################################
#  Test Functions
################################################################
def test_read_populations():
    print("Reading " , len (POPULATIONS), "data from world population")
    show_enumerated(POPULATIONS)    
        
        
def test_calculate_countries():        
    countries = calculate_countries(POPULATIONS)
    print("Countries")
    print("Read " , len (countries), "different countries")
    show_enumerated(countries)
  
def test_filter_by_country():        
    population_es = filter_by_country(POPULATIONS, "Spain")
    print("Population Spain")
    print("Read " , len (population_es), "data of population from Spain")
    show_enumerated(population_es)

def test_filter_by_countries_and_year():        
    countries= ["Spain","Portugal","France","Mexico","China"]
    population_2016 = filter_by_countries_and_year(POPULATIONS, 2016, countries)
    print("Read " , len (population_2016), "data of year 2016 for countries", countries)
    show_enumerated(population_2016)
        
def test_show_population_evolution():
    show_population_evolution(POPULATIONS, "Spain")

def test_show_comparative_countries_year():
    show_comparative_countries_year(POPULATIONS, 2016,["Spain","Portugal","France","Mexico","China"])
        
################################################################
#  Main Program
################################################################
POPULATIONS = read_populations('../data/population.csv')

test_read_populations()
#test_calculate_countries()
#test_filter_by_country()
#test_filter_by_countries_and_year()
#test_show_population_evolution()
#test_show_comparative_countries_year()