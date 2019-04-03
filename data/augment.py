import csv
import pandas as pd
from numpy import genfromtxt
import numpy as np
import random

data=open("Canada10.csv","r")

array=[]
hold=[]

for line in data:
	holder=line
	x=0
	y=0
	while len(hold)<263:
		if str(holder[y])==",":
			hold.append(float(holder[x:y]))
			x=y+1
		y=y+1
	hold.append(holder[x:-1])
	array.append(hold)
	hold=[]

print(len(array))
