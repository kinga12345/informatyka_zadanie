# -*- coding: utf-8 -*-
"""
Created on Tue May 11 11:25:41 2021

@author: Ja
"""


# Wykonały 
# Kinga Przybylska
# Weronika Polinska


import geopandas
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime


gdf = geopandas.read_file('PD_STAT_GRID_CELL_2011.shp')


gdf['centroid'] = gdf.centroid


import shapely
#
xmin, ymin, xmax, ymax= [13 ,48 , 25, 56]
# 
n_cells=30
cell_size = (xmax-xmin)/n_cells
#
grid_cells = []
for x0 in np.arange(xmin, xmax+cell_size, cell_size ):
    for y0 in np.arange(ymin, ymax+cell_size, cell_size):
        x1 = x0-cell_size
        y1 = y0+cell_size
        grid_cells.append( shapely.geometry.box(x0, y0, x1, y1) )
cell = geopandas.GeoDataFrame(grid_cells, columns=['geometry'])
ax = gdf.plot(markersize=.1, figsize=(12, 8), column='TOT', cmap='jet')

plt.autoscale(False)
cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("off")


gdf.to_crs("EPSG:4326")
merged = geopandas.sjoin(gdf, cell, how='left', op='within')

dissolve = merged.dissolve(by="index_right", aggfunc="sum")

ax = cell.plot(column='TOT', figsize=(12, 8), cmap='viridis', vmax=700000, edgecolor="grey", legend = True)
plt.autoscale(False)
ax.set_axis_off()
plt.axis('equal');
plt.title('liczba ludności w siatce')




gdw = geopandas.read_file('Województwa.shp')
ax = gdw.plot(markersize=.1, figsize=(12, 8), column='TOT_0_14', cmap='jet')
gdw.to_crs("EPSG:4326")
plt.autoscale(False)
cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")
merged = geopandas.sjoin(gdw, cell, how='left', op='within')
dissolve = merged.dissolve(by="index_right", aggfunc="sum")
cell.loc[dissolve.index,'TOT_O_14']= dissolve.TOT_0_14.values
ax = cell.plot(column='TOT_0_14', figsize=(12, 8), cmap='viridis', vmax=700000, edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_off()
plt.axis('equal');
plt.title('liczba ludności w wieku 0-14')



ax = gdw.plot(markersize=.1, figsize=(12, 8), column='TOT_15_64', cmap='jet')
gdw.to_crs("EPSG:4326")
plt.autoscale(False)
cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")
merged = geopandas.sjoin(gdw, cell, how='left', op='within')
dissolve = merged.dissolve(by="index_right", aggfunc="sum")
cell.loc[dissolve.index,'TOT_15_64']= dissolve.TOT_0_14.values
ax = cell.plot(column='TOT_15_64', figsize=(12, 8), cmap='viridis', vmax=700000, edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_off()
plt.axis('equal');
plt.title('liczba ludności w wieku 15-64')


ax = gdw.plot(markersize=.1, figsize=(12, 8), column='TOT_64_', cmap='jet')
gdw.to_crs("EPSG:4326")
plt.autoscale(False)
cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")
merged = geopandas.sjoin(gdw, cell, how='left', op='within')
dissolve = merged.dissolve(by="index_right", aggfunc="sum")
cell.loc[dissolve.index,'TOT_64_']= dissolve.TOT_0_14.values
ax = cell.plot(column='TOT_64_', figsize=(12, 8), cmap='viridis', vmax=700000, edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_off()
plt.axis('equal');
plt.title('liczba ludności w wieku >64')




ax = gdw.plot(markersize=.1, figsize=(12, 8), column='TOT_MALE_0_14', cmap='jet')
gdw.to_crs("EPSG:4326")
plt.autoscale(False)
cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")
merged = geopandas.sjoin(gdw, cell, how='left', op='within')
dissolve = merged.dissolve(by="index_right", aggfunc="sum")
cell.loc[dissolve.index,'TOT_MALE_O_14']= dissolve.TOT_0_14.values
ax = cell.plot(column='TOT_MALE_0_14', figsize=(12, 8), cmap='viridis', vmax=700000, edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_off()
plt.axis('equal');
plt.title('liczba mezczyzn w wieku 0-14')
ax = gdw.plot(markersize=.1, figsize=(12, 8), column='TOT_MALE_15_64', cmap='jet')
gdw.to_crs("EPSG:4326")
plt.autoscale(False)
cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")
merged = geopandas.sjoin(gdw, cell, how='left', op='within')
dissolve = merged.dissolve(by="index_right", aggfunc="sum")
cell.loc[dissolve.index,'TOT_MALE_15_64']= dissolve.TOT_0_14.values
ax = cell.plot(column='TOT_MALE_15_64', figsize=(12, 8), cmap='viridis', vmax=700000, edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_off()
plt.axis('equal');
plt.title('liczba mezczyzn w wieku 15-64')
ax = gdw.plot(markersize=.1, figsize=(12, 8), column='TOT_MALE_64_', cmap='jet')
gdw.to_crs("EPSG:4326")
plt.autoscale(False)
cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")
merged = geopandas.sjoin(gdw, cell, how='left', op='within')
dissolve = merged.dissolve(by="index_right", aggfunc="sum")
cell.loc[dissolve.index,'TOT_MALE_64_']= dissolve.TOT_0_14.values
ax = cell.plot(column='TOT_MALE_64_', figsize=(12, 8), cmap='viridis', vmax=700000, edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_off()
plt.axis('equal');
plt.title('liczba mezczyzn w wieku >64')




ax = gdw.plot(markersize=.1, figsize=(12, 8), column='TOT_FEMALE_0_14', cmap='jet')
gdw.to_crs("EPSG:4326")
plt.autoscale(False)
cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")
merged = geopandas.sjoin(gdw, cell, how='left', op='within')
dissolve = merged.dissolve(by="index_right", aggfunc="sum")
cell.loc[dissolve.index,'TOT_FEMALE_O_14']= dissolve.TOT_0_14.values
ax = cell.plot(column='TOT_FEMALE_0_14', figsize=(12, 8), cmap='viridis', vmax=700000, edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_off()
plt.axis('equal');
plt.title('liczba kobiet w wieku 0-14')
ax = gdw.plot(markersize=.1, figsize=(12, 8), column='TOT_FEMALE_15_64', cmap='jet')
gdw.to_crs("EPSG:4326")
plt.autoscale(False)
cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")
merged = geopandas.sjoin(gdw, cell, how='left', op='within')
dissolve = merged.dissolve(by="index_right", aggfunc="sum")
cell.loc[dissolve.index,'TOT_FEMALE_15_64']= dissolve.TOT_0_14.values
ax = cell.plot(column='TOT_FEMALE_15_64', figsize=(12, 8), cmap='viridis', vmax=700000, edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_off()
plt.axis('equal');
plt.title('liczba kobiet w wieku 15-64')
ax = gdw.plot(markersize=.1, figsize=(12, 8), column='TOT_FEMALE_64_', cmap='jet')
gdw.to_crs("EPSG:4326")
plt.autoscale(False)
cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("on")
merged = geopandas.sjoin(gdw, cell, how='left', op='within')
dissolve = merged.dissolve(by="index_right", aggfunc="sum")
cell.loc[dissolve.index,'TOT_FEMALE_64_']= dissolve.TOT_0_14.values
ax = cell.plot(column='TOT_FEMALE_64_', figsize=(12, 8), cmap='viridis', vmax=700000, edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_off()
plt.axis('equal');
plt.title('liczba kobiet w wieku >64')
