# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#importing and ploting shapefiles
import geopandas as gpd
import matplotlib.pyplot as plt

village = gpd.read_file('C:/Users/Lenovo/Documents/Shapefiles/contour.shp')
village.plot(cmap = 'jet', column = 'ID', figsize = (10,10))

#AOI = gpd.read_file('C:/Users/Lenovo/Documents/Shapefiles/Gut_No-4.shp')
#AOI.plot(cmap = 'jet', column ='Gut No', figsize = (10,10))

village.plot()
plt.autoscale(False)
