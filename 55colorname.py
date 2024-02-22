# 55colorname.py by Ethan Djou

import sys
import math

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

if R < 0 or R > 255: sys.exit('error: R color value must be 0 - 255')
if G < 0 or G > 255: sys.exit('error: G color value must be 0 - 255')
if B < 0 or B > 255: sys.exit('error: B color value must be 0 - 255')

color_distance = []
color_name = []

def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d

def minimum(vals):
	min = vals[0]
	for val in vals[1:]:
		if val < min: min = val
	return min


with open(colorfile) as fp:
	for line in fp:
		color = line.split()	
		values = color[2]
		names = color[0]
		r, g, b = values.split(',')
		color_values = (int(r), int(g), int(b))
		distance = dtc((R, G, B), color_values)
		color_distance.append(distance)
		color_name.append(names)

closest_color = minimum(color_distance)
index_value = color_distance.index(closest_color)

print(color_name[index_value])


		

		

