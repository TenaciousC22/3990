import csv

data=open("dataset.csv","r")
output=open("regdata.csv","w")
raw=[]
temp=[]
reg=[]
minpre=0
maxpre=0
mintemp=0
maxtemp=0
for line in data:
	temp=[]
	holder=line
	x=0
	holder=holder+','
	for y in range(len(holder)):
		if holder[y]==',':
			temp.append(float(holder[x:y]))
			x=y+1
	raw.append(temp)

for x in range(len(raw)):
	for y in range(131):
		if raw[x][2*y]<mintemp:
			mintemp=raw[x][2*y]
		if raw[x][2*y]>maxtemp:
			maxtemp=raw[x][2*y]
		if raw[x][(2*y)+1]>maxpre:
			maxpre=raw[x][(2*y)+1]

print(minpre)
print(maxpre)
print(mintemp)
print(maxtemp)
print(int(len(raw[0])/2))

for x in range(len(raw)):
	for y in range(int(((len(raw[x]))/2))):
		raw[x][y*2]=(((raw[x][y*2])-mintemp)/((maxtemp-mintemp)/2))-1
		raw[x][(y*2)+1]=(raw[x][(y*2)+1])/maxpre
		#print(y*2+1)

for x in range(len(raw)):
	output.write(','.join(map(str,raw[x])))
	output.write('\n')