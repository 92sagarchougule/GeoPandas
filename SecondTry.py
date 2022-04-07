# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 21:05:28 2022

@author: Lenovo
"""

import geopandas as gpd

hous = gpd.read_file(r"C:\Users\Lenovo\Documents\GeoPandas\Shapefiles\walwa.shp")

hous.plot(cmap='jet', edgecolor='black', column ='GPNAME')

hous.plot(cmap='hsv', edgecolor='black', column ='VILLNAME', figsize =(10,8))
