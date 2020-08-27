#!/usr/bin/env python3

# All this comes from:
# https://pypi.python.org/pypi/pyshp

import pdb
import shapefile

sf = shapefile.Reader("CA_counties.dbf")

shapes = sf.shapes()

print(len(shapes))

for name in dir(shapes[3]):
	if not name.startswith('__'):
		print(name)
		
print(len(list(sf.iterShapes())))

print(shapes[3].shapeType)

bbox = shapes[3].bbox
['%.3f' % coord for coord in bbox]

print(shapes[3].parts)

len(shapes[3].points)

shape = shapes[3].points[7]
['%.3f' % coord for coord in shape]

s = sf.shape(7)
['%.3f' % coord for coord in s.bbox]

fields = sf.fields
print(fields)

records = sf.records()

print(len(records))

print(len(list(sf.iterRecords())))

print(records[3][1:3])




pdb.set_trace()