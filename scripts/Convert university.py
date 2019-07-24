from csv import reader
import sys
from difflib import SequenceMatcher
import pandas as pd
import numpy as np
from tqdm import tqdm
import swifter
import pickle

inputfile = open(r"C:\Users\user\AllUniversities.csv", encoding='utf8') #file containing all distinct universities in the dataset
lines = reader(inputfile, delimiter =',')
outputfile = open("Unicombis.csv", "w+", encoding='utf8')
uni_countrydi = []
allPoss = {}

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

print("start")
for line in lines:
	#structure is "uniold","count"
	#read in all in dictoio, while removing 'Uni of'
	uni= line[0]
	uni = uni.replace("University of ","").replace(" University","").replace("University","").replace("Université de ","")
	uni = uni.replace("Université ","").replace("Universität zu ","").replace("Universitat ","")
	uni = uni.replace("Università di ","").replace("Universidade ","").replace("","").replace("Universidade ","")
	uni = uni.replace("Universiteit ","").replace("Universiteit","")
	uni = uni.replace('  ', ' ') 
	uni_countrydi.append([uni,line[0]])

print("read in unis. Starting comparison")
uni_countrydi2 = uni_countrydi
#then do similarity test
acounter = 0
for UU in uni_countrydi:
	print(acounter)
	uni_countrydi = uni_countrydi2
	del uni_countrydi[acounter]
	localcount =1
	for otherUU in uni_countrydi:
			#do similarity here
			Ushort = otherUU[0]
			z = similar(UU[0], Ushort)
			if z>0.85:
				allPoss[UU[1] + " > "+str(localcount)] = otherUU[1]
				localcount += 1
	acounter+= 1

print("writing to file")

f = open('store.pckl', 'wb')
pickle.dump(allPoss, f)
f.close()

#f = open('store.pckl', 'rb')
#obj = pickle.load(f)
#f.close()

for k, v in allPoss.items():
    outputfile.write(str(k) + '\n'+ str(v) + '\n\n')

print("All done.")
inputfile.close() 
outputfile.close()
