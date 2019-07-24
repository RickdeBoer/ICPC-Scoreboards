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
	# 1/106 
	# 7
	# 0 is nothing
	localcount = 0
	for score in separatescores:
		if("/" not in score and score != "0" and score != "0\n"):		
			separatescores[localcount] = score.strip() + "/-"
		elif(score == "0" or score == 0 or score == "0\n"):
			separatescores[localcount] = ""
		else:			
			separatescores[localcount] = score.strip()
		localcount= localcount +1
	return separatescores

def splitScoreAndTime(scoreandtime): 
	#expected format: 6 / 859
	pieces = scoreandtime.split(" / ")
	finalscore = pieces[0]
	finaltime = pieces[1]
	return finalscore + "," + finaltime

def getUniversity(teamanduniversity):
	#expected format: "team001: UW1 (U Warsaw) Mateusz Radecki, Konrad Paluszek, Jakub Boguta"	
	university = str(teamanduniversity).split(') ')[0].split(" (")[1]
	return university

def getTeam(teamanduniversity):
	#expected format: "team001: UW1 (U Warsaw) Mateusz Radecki, Konrad Paluszek, Jakub Boguta"	
	team = teamanduniversity.strip().split(" (")[0].split(": ")[1]
	return team

##########################################################################

lines = reader(fileX, delimiter =',')
linecounter= 0
for line in lines:
	if(linecounter == 0): #handle header
		#find column index of all values
		Rank_index = line.index("Rank")
		TeamAndUniversity_index = line.index("TeamAndUniversity")
		ScoreAndTime_index = line.index("ScoreAndTime")			
		ScoresStart_index = line.index("A")		
		numberofproblems = findnumberofproblems(line)

		outputfile.write("#,Team,University,A,B,C,D,E,F,G,H")		
		write_nr_ofproblems(numberofproblems)
		outputfile.write(",Solved,Time\n")

	else: #clean rows
		rank_final = line[0] #can choose custom numbering 'linecounter' or file numbering 'line[0]'

		#clean teamname
		team_final = getTeam_CERC(line[TeamAndUniversity_index])

		#clean university
		university_final = getUniversity_CERC(str(line[TeamAndUniversity_index]))

		#format individual scores
		allscores = line[ScoresStart_index:(numberofproblems + ScoresStart_index)]		
		allscores = scoreFormatter(allscores) 
		allscores = ",".join(allscores)

		#format total scores and time
		scoreAndTime_final = splitScoreAndTime_CERC(line[ScoreAndTime_index])

		#write all formatted pieces to outputfile
		outputfile.write(",".join([rank_final,team_final,university_final])+","+
						 allscores+","+ scoreAndTime_final +"\n")

	linecounter=linecounter+1

print('Done.')