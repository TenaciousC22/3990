import csv
flag=False

data=open("textdata1.txt","r")
dataArr=[]
years=[]
output=open("Prairies5.csv","a+")
for line in data:
	holder=line
	for x in range(len(holder)):
		if holder[x]==",":
			temp=holder[0:x]
			prec=holder[x+1:-1]
			dataArr.append([temp,prec])
			break
#print(len(dataArr)/12)
temp=[]
for x in range(int(len(dataArr)/12)):
	for y in range(12):
		temp.append(dataArr[12*x+y][0])
		temp.append(dataArr[12*x+y][1])
	years.append(temp)
	temp=[]

datasets=[]

for x in range(len(years)-5):
	for y in range(6):
		for z in range(24):
			temp.append(years[x+y][z])
	datasets.append(temp)
	temp=[]

for x in range(len(datasets)):
	output.write(','.join(datasets[x]))
	output.write('\n')
