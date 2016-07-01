def Winner(PlayerA, PlayerB):

	Awins = PlayerA / float(PlayerA + PlayerB) #Function that performs formula to work out Player A winner probability.
	return Awins


def PlayerWin(PlayerA, PlayerB, Score=11, Margin=2): #Function that returns winner and total points of one match.

	import random

	Ascore = 0 #Set Variables.
	Bscore = 0 #Set Variables.
	Win = 0 #Set Variables.
	ScoreT = 0 #Set Variables.

	while 1:
		
		Chance = random.random() #Generate random number

		if Winner(PlayerA, PlayerB) >= Chance: #Calls Winner function and compares to random number generated.
			Ascore += 1
			ScoreT += 1
		elif Winner(PlayerA, PlayerB) <= Chance: #Calls Winner function and compares to random number generated.
			Bscore += 1
			ScoreT += 1
		if Ascore >= Score and Bscore <= (Ascore - Margin): #Checks who winner is compared to score and margin set.
			Win = 1
			break
		elif Bscore >= Score and Ascore <= (Bscore - Margin): #Checks who winner is compared to score and margin set.
			Win = 2
			break

	Ascore = 0 #Reset variables.
	Bscore = 0 #Reset variables.

	return Win, ScoreT #Return Win variable and total points played.


def PlayerWinTest(TestNo, PlayerA, PlayerB, Score=11, Margin=2): #Function that repeates PlayerWin function n times and returns Win probability for A and average points played.

	Atotal = 0
	Btotal = 0
	PointsT = [] #Empty list.

	for x in range(TestNo): #Run n times.

		GameFair, GameScore = PlayerWin(PlayerA, PlayerB, Score, Margin) #Variables = results of PlayerWin function.

		if GameFair == 1:
			Atotal += 1
		elif GameFair == 2:
			Btotal += 1

		PointsT.append(GameScore) #Add total points player each game to list.

	return (float((float(Atotal) / float(TestNo)))), (sum(PointsT) / len(PointsT)) #Returns probability of A winning and Average points played for all iterations.


def PlayerGraph(TestNo, PlayerA, PlayerB, Score=0, Margin=2): #Creates 2 graphs. One for fairness and one for total points played while incrementing the winning score.

	LiFair = [] #Create empty list.
	LiPoint = [] #Create empty list.
	LiScore = [] #Create empty list.

	for x in range(1, 51): #Repeat 50 times.

		Score = x #Replace score with value of X.

		Fair, Points = PlayerWinTest(TestNo, PlayerA, PlayerB, Score, Margin) #Assign 2 variables based on return of PlayerWinTest.

		LiFair.append(Fair) #Append all lists.
		LiPoint.append(Points) #Append all lists.
		LiScore.append(x) #Append all lists.

	import matplotlib.pyplot as plt #Import Matplotlib and assign it to variable plt.
	plt.plot(LiScore, LiFair) #Plot Lists.
	plt.xlabel('Winning Score') #Name axis.
	plt.ylabel('Fairness') #Name axis.
	plt.show() #Disply graph.
	plt.plot(LiScore, LiPoint) #Plot Lists.
	plt.xlabel('Winning Score') #Name axis.
	plt.ylabel('Average Points Played') #Name axis.
	plt.show() #Disply graph.


def GamesWin(TestNo, GamesWin, PlayerA, PlayerB, Score=11, Margin=2): #Function that returns probability of A winning a game if the winner must win a user defined number of matches.

	TotalAWin = 0 #Set variable.
	TotalBWin = 0 #Set variable.

	for x in range(TestNo): #Run n times.

		GamesAWin = 0 #Reset variable.
		GamesBWin = 0 #Reset variable.

		while 1:
			
			Winner, Empty = PlayerWin(PlayerA, PlayerB, Score, Margin) #Assign 2 variables based on return of PlayerWin.

			if Winner == 1: #Check Winner variable.
				GamesAWin += 1 #Increment by one.
			elif Winner == 2: #Check Winner variable.
				GamesBWin += 1 #Increment by one.

			if GamesAWin >= GamesWin: #Check who wins the game.
				TotalAWin += 1 #Increment total wins.
				break
			elif GamesBWin >= GamesWin: #Check who wins the game.
				TotalBWin += 1 #Increment total wins.
				break

	return float(TotalAWin) / TestNo #Return proability.


def GamesWinTest(TestNo, PlayerA, PlayerB, Score=11, Margin=2): #Function that returns probability of A winning a game if the winner must win n matches.

	TotalAWin = 0 #Set variable.
	TotalBWin = 0 #Set variable.
	GamesWin = 1 #Set variable
	y = 1 #Set variable

	while y == 1:

		for x in range(TestNo): #Run n times.

			GamesAWin = 0 #Reset variable.
			GamesBWin = 0 #Reset variable.

			while 1:
				
				Winner, Empty = PlayerWin(PlayerA, PlayerB, Score, Margin) #Assign 2 variables based on return of PlayerWin.

				if Winner == 1: #Check Winner variable.
					GamesAWin += 1 #Increment by one.
				elif Winner == 2: #Check Winner variable.
					GamesBWin += 1 #Increment by one.

				if GamesAWin >= GamesWin: #Check who wins the game.
					TotalAWin += 1 #Increment total wins.
					break
				elif GamesBWin >= GamesWin: #Check who wins the game.
					TotalBWin += 1 #Increment total wins.
					break


		if float(TotalAWin) / TestNo > 0.9: #Check if probability is above 0.9.
			y = 0 #Stop Loop by changing y to 0.
			return float(TotalAWin) / TestNo, GamesWin #Return probability of winning and Number of games that were required to win at this point.
		elif float(TotalAWin) / TestNo <= 0.9: #Check if probability is above 0.9.
			TotalAWin = 0 #Reset variable.
			TotalBWin = 0 #Reset variable.
			y = 1 #Keep loop active.
			GamesWin += 1 #Increase amount of games to win by 1 each loop


def TeamPlay(TestNo, Score=11, Margin=2):

	TeamA = [40, 50, 60] #Team skills. 
	TeamB = [75, 25, 30] #Team skills.

	import itertools

	TeamProb=dict() #Create blank dictionary.

	for item in itertools.product(TeamA, TeamB): #Find combinations.

		TeamAPlay, TeamBPlay = item #Assign variables to current result of 'item'.

		Prob = GamesWin(TestNo, 2, TeamAPlay, TeamBPlay, Score=11, Margin=2) #Run x games with the win parameter.

		TeamProb[TeamAPlay, TeamBPlay]=Prob #Append dictionary with probability of each matchup.

	return TeamProb #Return dictionary.


def TeamPlayTest(TestNo, Score=11, Margin=2):

	TeamA = [40, 50, 60] #Team skills. 
	TeamB = [70, 80, 90] #Team skills.
	ProbLi = []
	TotalAWin = 0
	TotalBWin = 0
	Atrack = 0
	Btrack = 0

	import itertools

	for itema, itemb in itertools.product(TeamA, itertools.permutations(TeamB)): #Find combinations.

		TeamBPlay1, TeamBPlay2, TeamBPlay3 = itemb #Assign variables to current result of 'item'.

		TeamAPlay1, TeamAPlay2, TeamAPlay3 = TeamA

		print TeamAPlay1, TeamAPlay2, TeamAPlay3

		print TeamBPlay1, TeamBPlay2, TeamBPlay3

		Atotal = 0
		Btotal = 0
		PointsT = [] #Empty list.

		for x in range(TestNo): #Run n times.

			GameFair, GameScore = PlayerWin(TeamAPlay1, TeamBPlay1, Score, Margin) #Variables = results of PlayerWin function.

			if GameFair == 1:
				Atotal += 1
			elif GameFair == 2:
				Btotal += 1

		if Atotal > Btotal:
			Atrack += 1
			print Atrack
		elif Btotal > Atotal:
			Btrack += 1

		ProbLi.append((float(Atotal)/TestNo))

		Atotal = 0
		Btotal = 0
		PointsT = [] #Empty list.

		for x in range(TestNo): #Run n times.

			GameFair, GameScore = PlayerWin(TeamAPlay2, TeamBPlay2, Score, Margin) #Variables = results of PlayerWin function.

			if GameFair == 1:
				Atotal += 1
			elif GameFair == 2:
				Btotal += 1

		if Atotal > Btotal:
			Atrack += 1
			print Atrack
		elif Btotal > Atotal:
			Btrack += 1

		ProbLi.append((float(Atotal)/TestNo))

		if Atrack >= 2:

			return ProbLi

		elif Atrack == Btrack:

			for x in range(TestNo): #Run n times.

				GameFair, GameScore = PlayerWin(TeamAPlay2, TeamBPlay2, Score, Margin) #Variables = results of PlayerWin function.

				if GameFair == 1:
					Atotal += 1
				elif GameFair == 2:
					Btotal += 1

			if Atotal > Btotal:
				Atrack += 1
				print Atrack
			elif Btotal > Atotal:
				Btrack += 1

			ProbLi.append((float(Atotal)/TestNo))

	return sum(ProbLi) / TestNo