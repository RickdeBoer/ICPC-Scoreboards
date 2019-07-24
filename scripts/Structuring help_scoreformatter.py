#this file contains all possible formats for scores found. One can be copied to the main structuring script.
#the expected format is different for a problem that is Solved, Attempted, or Not tried. Each
#function expects a specific notation for each format.

def formattime(timestring):
	#Expected inputformat: 0:43:58
	timestuff = timestring.split(":")
	cleanedtime = int(timestuff[0])*60 + int(timestuff[1]) + int(round(float(timestuff[2])/60, 0))

	return str(cleanedtime)

def formatter1(separatescores):
	#notation is here:
	# 3(0:18:37 + 0:40:00) or 1(2:33:32)
	# 5
	# 0
	localcount = 0
	for score in separatescores:
		print(score)
		if(score == "0"):
			separatescores[localcount] = ""
		elif(score != "0" and "(" not in score):
			separatescores[localcount] = score + "/-"
		elif("+" in score):
			xz = score.split(" ")
			yz = xz[0].split("(")
			tries = yz[0]
			time = formattime(yz[1])
			separatescores[localcount] = tries + "/" + time
		else:
			#1(2:39:28)
			xz = score.split("(")			
			separatescores[localcount] = "1/" + formattime(xz[1].replace(")","")) 
		localcount= localcount +1
	return separatescores

def formatter2(separatescores):
	#notation is here:
	# 3 (0:18:37 + 0:40:00) or 1 (2:33:32)
	# 5
	# 0
	localcount = 0
	for score in separatescores:
		print(score)
		if(score == "0"):
			separatescores[localcount] = ""
		elif(score != "0" and "(" not in score):
			separatescores[localcount] = score + "/-"
		elif("+" in score):
			xz = score.split(" ")
			tries = xz[0]
			time = formattime(xz[1].replace("(", ""))
			separatescores[localcount] = tries + "/" + time
		else:
			#1 (2:39:28)
			xz = score.split(" ")
			separatescores[localcount] = "1/" + formattime(xz[1].replace(")","").replace("(","")) 
		localcount= localcount +1
	return separatescores

def formatter3(separatescores):
	#notation is here:
	# 0:43:58 + 0:20:002 tries or 1:12:481 try
	# 2 tries or 1 try
	# ""
	localcount = 0
	for score in separatescores:
		if(score == ""):
			separatescores[localcount] = score
		elif(":" not in score):
			separatescores[localcount] = score.split(" ")[0] + "/-"
		elif("+" in score):
			xz = score.split(" + ")
			cleanedtime = formattime(xz[0])
			tries = xz[1].split(" ")[0][7:]			
			separatescores[localcount] = tries + "/" + str(cleanedtime) 
		else:
			#4:27:381 try
			xy = score.split(" ")
			tries = xy[0][:6]
			cleanedtime = formattime(xy[0])
			separatescores[localcount] = "1/" + str(cleanedtime) 

		localcount= localcount +1
	return separatescores

def formatter4(separatescores):
	#notation is here:
	# "x,x"
	# "x,"
	# "0,"
	localcount = 0
	prevscore = -1
	outputlist= []
	for score in separatescores:
		if(localcount > 0 and localcount % 2 == 1):	
			if(prevscore != "" and score != ""):
				outputlist.append(prevscore + "/" + score)
			elif(prevscore != "" and score == "" and prevscore != "0"):
				outputlist.append(prevscore + "/-")
			else:
				outputlist.append("")
		prevscore = score
		localcount= localcount +1
	return outputlist

def formatter5(separatescores):
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

def formatter6(separatescores):	
	#notation is here:
	# "1/11"
	# "1/--"
	# "0/--"
	localcount = 0
	for score in separatescores:
		if("--" not in score):	
			separatescores[localcount] = score
		elif(score == "0/--"):				
			separatescores[localcount] = ""
		else:	
			separatescores[localcount] = score.split("/")[0] +  "/-"
		localcount= localcount +1
	return separatescores

def formatter7(separatescores):	
	#notation is here:
	# "1/11"
	# "1/0"
	# "0/0"
	localcount = 0
	for score in separatescores:
		yo = score.split("/")
		if(yo[1] != "0"):			
			separatescores[localcount] = score
		elif(yo[0] == "0"):
			separatescores[localcount] = ""
		else:
			separatescores[localcount] = yo[0] + "/-"
		localcount= localcount +1
	return separatescores

def formatter8(separatescores):
	#notation is here:
	# "1/11"
	# "1/-"
	# "-/-"
	localcount = 0
	for score in separatescores:
		if(score == "-/-"):		
			separatescores[localcount] = ""
		else:
			separatescores[localcount] = score
		localcount= localcount +1
	return separatescores

def formatter9(separatescores):	
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


def formatter10(separatescores):	
	#notation is here:
	# 1(01:16) with hour:minutes
	# 11
	# - is nothing
	localcount = 0
	for score in separatescores:
		if("(" in score):	
			allx = score.split("(")
			attempts = allx[0]
			time = allx[1].split(")")[0].split(":")
			formattedtime = int(time[0])*60 + int(time[1])			
			separatescores[localcount] = str(attempts.strip()) + "/" + str(formattedtime).strip()			
		elif("(" not in score and "-" not in score and score != "" and score != " "):
			separatescores[localcount] = score.strip() + "/-"
		else:			
			separatescores[localcount] = ""
		localcount= localcount +1
	return separatescores

def formatter11(separatescores):	
	#notation is here:
	# +1 115:00 of + 115:00 with min:sec
	# -17
	# . is nothing
	localcount = 0
	for score in separatescores:
		if(score == "."):		
			separatescores[localcount] = ""
		elif("-" in score):
			separatescores[localcount] = score.split("-")[1] + "/-"	
		else:
			allx = score.split("+")
			more = allx[1].split(" ")
			if(more[0] == ""):
				attempts = 1
			else:				
				attempts = 1 + int(more[0])		
			timepieces = more[1].split(":")
			formattedtime = int(timepieces[0]) + int(round(float(timepieces[1])/60, 0))
			separatescores[localcount] = str(attempts) + "/" + str(formattedtime)	
		localcount= localcount +1
	return separatescores


def formatter12(separatescores):	
	#notation is here:
	# +1 (2:31) of + (4:23)
	# -17
	# empty is nothing
	localcount = 0
	for score in separatescores:
		if(score == ""):		
			separatescores[localcount] = ""
		elif("-" in score):
			separatescores[localcount] = score.split("-")[1] + "/-"	
		else:			
			allx = score.split("+")
			more = allx[1].split(" ")
			if(more[0] == ""):
				attempts = 1
			else:				
				attempts = 1 + int(more[0])				
			time = more[1].replace("(","").replace(")","")
			timepieces = time.split(":")
			formattedtime = int(timepieces[0]) * 60 + int(timepieces[1])
			separatescores[localcount] = str(attempts) + "/" + str(formattedtime)
		localcount= localcount +1
	return separatescores

def formatter13(separatescores):	
	#notation is here:
	# "1 / 	          11"
	# "1 / 	           	              --"
	# "0 / 	           	              --"
	localcount = 0
	for score in separatescores:
		yz = score.split('"')
		allx = yz[1].split(" / ")
		attempts = allx[0]
		time = allx[1].strip()
		if("--" in attempts):	
			if(attempts == "0" or attempts == 0):
				separatescores[localcount] = ""
			else:				
				separatescores[localcount] = attempts + "/-"		
		else:			
			separatescores[localcount] = attempts + "/" + time
		localcount= localcount +1
	return separatescores


def formatter14(separatescores):	
	#notation is here:
	# 4:54 + 100 or 2:17
	# "" for nothing
	localcount = 0
	for score in separatescores:
		score.strip()
		if(score == ""):
			separatescores[localcount] = ""
		else:
			if("+" in score):
				time = score.split(" + ")[0]
				timepieces = time.split(":")
				formattedtime = int(timepieces[0]) * 60 + int(timepieces[1])
				attempts = int(score.split(" + ")[1]) / 20
				separatescores[localcount] = str(attempts).split(".")[0] + "/" + str(formattedtime)
			else:		
				timepieces = score.split(":")
				formattedtime = int(timepieces[0]) * 60 + int(timepieces[1])	
				separatescores[localcount] = "1/" + str(formattedtime)
		localcount= localcount +1
	return separatescores

def formatter15(separatescores):	
	#notation is here:
	# 4 (123 + 60)
	# 5
	# 0
	localcount = 0
	for score in separatescores:
		if(score == "0" or score == 0 or score == "0\n"):				
			separatescores[localcount] = ""
		elif("(" not in score):
			formattedscore = score.rstrip() + "/-"
			separatescores[localcount] = formattedscore
		else:			
			yz = score.split(" ")
			attempts = yz[0]
			time = yz[1].replace("(","")
			separatescores[localcount] = attempts + "/" + time
		localcount= localcount +1
	return separatescores


def formatter16(separatescores):	
	#notation is here:
	# 4:47:06 (0) 
	# ------- (2) 
	# empty
	localcount = 0
	for time in separatescores:
		if(time != ""):
			yz = time.split(" ")
			attempts = yz[1].replace("(","").replace(")","")
			if("-" not in time): #solved so has time
				timestuff = yz[0].split(":")
				cleanedtime = int(timestuff[0])*60 + int(timestuff[1]) + int(round(float(timestuff[2])/60, 0))
				attempts = str(int(attempts) + 1)
			else: #not solved
				cleanedtime = "-"		
			separatescores[localcount] = attempts + "/" + str(cleanedtime)
		localcount= localcount +1
	return(separatescores)

def formatter17(separatescores):
	#1:071 try or 3:422 tries
	#–1 try or –3 tries
	#""
	localcount = 0
	for score in separatescores:
		if(("try" in score or "tries" in score) and ":" in score):
			numbers = score.split(" ")[0]	
			tries = numbers[-1:] + "/"	

			time = numbers[:-1]
			timepieces = time.split(":")
			formattedtime = int(timepieces[0]) * 60 + int(timepieces[1])

			formattedscore = str(tries) + str(formattedtime)
			separatescores[localcount] = formattedscore
		elif(("try" in score or "tries" in score) and "–" in score):
			numbers = score.split(" ")[0]
			separatescores[localcount] = numbers.replace("–","") + "/-"	

		localcount= localcount +1
	return separatescores