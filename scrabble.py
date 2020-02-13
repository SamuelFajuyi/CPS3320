
word = str(input("Enter a letter: "))

word = word.upper()


def letterScore(letter):

	if (letter in ['A', 'E', 'I', 'L', 'N', 'O', 'R', 'S', 'T', 'U']):
		return 1
	elif (letter in ['D', 'G']):
		return 2
	elif (letter in ['B', 'C', 'M', 'P']):
		return 3
	elif (letter in ['F', 'H', 'V', 'W', 'Y']):
		return 4
	elif (letter in ['K']):
		return 5
	elif (letter in ['J','X']):
		return 8
	elif (letter in ['Q', 'Z']):
		return 10
	else:
		return 0


score = {	"A": 1 , "B": 3 , "C": 3 , "D": 2 ,
			"E": 1 , "F": 4 , "G": 2 , "H": 4 ,
			"I": 1 , "J": 8 , "K": 5 , "L": 1 ,
			"M": 3 , "N": 1 , "O": 1 , "P": 3 ,
			"Q": 10, "R": 1 , "S": 1 , "T": 1 ,
			"U": 1 , "V": 4 , "W": 4 , "X": 8 ,
			"Y": 4 , "Z": 10}

def WordScore(string):
	total = 0;
	for i in word:
		total = total + score[i];
	return total;


if (len(word) == 1):
	print("The score for the letter is: ", letterScore(word))
else:
	print("The score for the word is: ", WordScore(word));


