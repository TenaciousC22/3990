import csv
import pandas as pd
from numpy import genfromtxt
import numpy as np
import random

data=open("Prairies10.csv","r")
output=open("Prairies10aug.csv","a+")

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

print(len(array[0]))

for x in range(len(array)):
	hold=[]
	for y in range(len(array[x])):
		if y%2==0:
			hold.append(float(array[x][y])+(random.randint(-20,20)/10))
		else:
			hold.append(float(array[x][y])+(random.randint(-50,50)/10))
	array.append(hold)

print(len(array[1000]))
dataset=[]

for x in range(len(array)):
	hold=[]
	for y in range(len(array[0])):
		hold.append("{:.1f}".format(float(array[x][y])))
		if y!=len(array[x])-1:
			hold.append(',')
	output.write(''.join(hold))
	output.write('\n')


