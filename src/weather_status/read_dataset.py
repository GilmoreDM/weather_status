"""
This file is to read the working datasets used for our color-coding status program
"""

import pygrib
import shapefile

wx_params = ['maxt','mint','wspd']

for param in wx_params:
    fname = "data/ds.{0}.bin".format(param)
    gr = pygrib.open(fname)

    for g in gr:
        print(g)

    gmsg = gr[1]
    print(gmsg)
    lats,lons = gmsg.latlons()
    print("Max Lat: {0}".format(max(lats[-1])))
    print("Min Lat: {0}".format(min(lats[0])))
    print("Max Lon: {0}".format(max(lons[-1])))
    print("Min Lon: {0}".format(min(lons[0])))
    #print(gmsg.latlons())
    #print(gmsg.values)
        
