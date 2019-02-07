import csv
flag=False

data=open("textdata1.txt","r")
dataArr=[]
for line in data:
	holder=line
	for x in range(len(holder)):
		if holder[x]==",":
			temp=holder[0:x]
			prec=holder[x+1:-1]
			dataArr.append([temp,prec])
			break

for x in range(len(dataArr)):
	print(dataArr[x])