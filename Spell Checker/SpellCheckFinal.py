def spellCheck(textFileName):
	"""
    >>> spellCheck("test1.txt")
    {'exercsie': 1, 'finised': 1}
    >>> spellCheck("test2.txt")
    {'bechause': 1, 'c++': 1}
    >>> spellCheck("test3.txt")
    {'lissard': 1, 'chamelon': 1, 'gerbal': 2, 'hampster': 3, 'tortise': 1}
    >>> type(spellCheck("test1.txt"))
    <type 'dict'>
	"""

	words = open("words.txt")
	wordsList = words.readlines()
	words.close()

	FileName = open(textFileName)
	wordsToCheck = FileName.readlines()
	FileName.close()

	for i in range(0,len(wordsList)): wordsList[i]=wordsList[i].replace("\n","")
	for i in range(0,len(wordsToCheck)): wordsToCheck[i]=wordsToCheck[i].replace("\n","")

	spellingErrors=dict()

	templist = []
	x = 0

	for i in range(0, len(wordsToCheck)):
		word = wordsToCheck[x]
		lowerword = word.lower()
		templist.append(lowerword)
		if templist[x] not in wordsList and templist[x] not in spellingErrors:
			spellingErrors[templist[x]] = 1
		elif templist[x] not in wordsList and templist[x] in spellingErrors:
			spellingErrors[templist[x]] += 1
		x += 1
	return spellingErrors







	# Return the dictionary


