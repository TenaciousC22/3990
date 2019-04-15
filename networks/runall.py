from Full5 import fitter5
from Full10 import fitter10

if __name__ =="__main__":
	target="DecTemOut"
	trials=10
	avg=0
	for x in range(trials):
		avg+=fitter5(target,"..\data\Prairies5.csv")
		print("",end="")
	print(" Done")
	print("Normal, 5 inputs: ",avg/trials)
	avg=0
	for x in range(trials):
		avg+=fitter10(target,"..\data\Prairies10.csv")
		print("",end="")
	print(" Done")
	print("Normal, 10 inputs: ",avg/trials)
	avg=0
	for x in range(trials):
		avg+=fitter5(target,"..\data\Prairies5aug.csv")
		print("",end="")
	print(" Done")
	print("Augmented, 5 inputs: ",avg/trials)
	avg=0
	for x in range(trials):
		avg+=fitter10(target,"..\data\Prairies10aug.csv")
		print("",end="")
	print(" Done")
	print("Augmented, 10 inputs: ",avg/trials)


	target="DecPreOut"
	avg=0
	for x in range(trials):
		avg+=fitter5(target,"..\data\Prairies5.csv")
		print("",end="")
	print(" Done")
	print("Normal, 5 inputs: ",avg/trials)
	avg=0
	for x in range(trials):
		avg+=fitter10(target,"..\data\Prairies10.csv")
		print("",end="")
	print(" Done")
	print("Normal, 10 inputs: ",avg/trials)
	avg=0
	for x in range(trials):
		avg+=fitter5(target,"..\data\Prairies5aug.csv")
		print("",end="")
	print(" Done")
	print("Augmented, 5 inputs: ",avg/trials)
	avg=0
	for x in range(trials):
		avg+=fitter10(target,"..\data\Prairies10aug.csv")
		print("",end="")
	print(" Done")
	print("Augmented, 10 inputs: ",avg/trials)