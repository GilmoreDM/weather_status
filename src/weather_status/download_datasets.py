"""
This file is to create the working dataset used for our color-coding status program
"""

import urllib3

wx_params = ['maxt','mint','wspd']

def get_data(param):
    http = urllib3.PoolManager()
    r = http.request('GET', f"https://tgftp.nws.noaa.gov/SL.us008001/ST.expr/DF.gr2/DC.ndfd/AR.conus/VP.001-003/ds.{param}.bin")
    fh = open(f"data/ds.{param}.bin",'wb')
    fh.write(r.data)
    fh.close()

for param in wx_params:
    get_data(param)
