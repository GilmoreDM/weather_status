import pandas
import numpy
import matplotlib as plt
import shapefile
import pdb

myshp = open('data/CA_counties.shp','rb')
mydbf = open('data/CA_counties.dbf','rb')

sf = shapefile.Reader(shp=myshp, dbf=mydbf)

shapes = sf.shapes()

bbox = ['%.3f' % coord for coord in shapes[4].bbox]

print(bbox)
