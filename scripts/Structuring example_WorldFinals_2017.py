from csv import reader
import sys

print("Running ICPC data parser on: ", str(sys.argv[1])) #input should be on raw HTML table converted to csv file 
fileX = open(str(sys.argv[1]), encoding='utf8')
outputfile = open("formattedICPCfile.csv", "w+", encoding='utf8')

##################################################################

def findnumberofproblems(line):			
	if("N" in line):
		return(14)
	elif("M" in line):
		return(13)
	elif("L" in line):
		return(12)
	elif("K" in line):
		return(11)
	elif("J" in line):
		return(10)
	elif("I" in line):
		return(9)
	else:
		return(8)

def write_nr_ofproblems(amountofproblems):
	if(amountofproblems == 9):
		outputfile.write(",I")
	elif(amountofproblems == 10):
		outputfile.write(",I,J")
	elif(amountofproblems == 11):
		outputfile.write(",I,J,K")
	elif(amountofproblems == 12):
		outputfile.write(",I,J,K,L")
	elif(amountofproblems == 13):
		outputfile.write(",I,J,K,L,M")

#########################
def scoreFormatter(separatescores):
	#notation is here:
	# "1              32"
	# "1              --"
	# ""
	localcount = 0
	for score in separatescores:
		if("" == score):	
			separatescores[localcount] = score
		elif("--" in score):
			separatescores[localcount] = score.split(" ")[0] + "/-"
		else:	
			delen = score.split(" ")
			separatescores[localcount] = delen[0] + "/" + delen[-1]
		localcount= localcount +1
	return separatescores

##########################################################################

lines = reader(fileX, delimiter =',')
linecounter= 0
for line in lines:
	if(linecounter == 0): #handle header
		#find column index of all values

		Rank_index = line.index("Rank")
		University_index = line.index("University")
		Score_index = line.index("Score")		
		Time_index = line.index("Time")			
		ScoresStart_index = line.index("A")		
		numberofproblems = findnumberofproblems(line)

		outputfile.write("#,Team,University,A,B,C,D,E,F,G,H")		
		write_nr_ofproblems(numberofproblems)
		outputfile.write(",Solved,Time\n")

	else: #clean rows
		rank_final = str(linecounter) #can choose custom numbering 'str(linecounter)' or file numbering 'line[0]'

		#clean teamname
		team_final = "" #there is no teamname for World Finals

		#clean university
		university_final = line[University_index]

		#format individual scores
		allscores = line[ScoresStart_index:(numberofproblems + ScoresStart_index)]		
		allscores = scoreFormatter(allscores) 
		allscores = ",".join(allscores)

		#format total scores and time
		score_final = line[Score_index]
		print(line)
		time_final = line[Time_index]

		#write all formatted pieces to outputfile
		outputfile.write(",".join([rank_final,team_final,university_final])+","+
						 allscores+","+ score_final+","+time_final+"\n")

	linecounter=linecounter+1

print('Done.')