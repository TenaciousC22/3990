#import Prairies10temp
#import Prairies5temp
#import Canada10temp
#import Canada5temp
#import Prairies10pre
#import Prairies5pre
#import Canada10pre
#import Canada5pre

from Full5 import fitter5
from Full10 import fitter10

if __name__ =="__main__":
	for x in range(10):
		fitter10("JanTemOut","..\data\Canada10.csv")
		print("",end="")
	print("Done")
	for x in range(10):
		fitter5("JanTemOut","..\data\Canada5.csv")
		print("",end="")
	print("Done")