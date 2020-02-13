import random
# Hangman game!

# Assume the answer is "hangman"

Answer = ['h', 'a','n', 'g', 'm', 'a', 'n']

Guess = ['_', '_', '_', '_', '_', '_', '_']

play = 6


while play > 0:
	# Ask the user to guess a letter
	letter = str(input("Guess a letter: "))

	#Check to see if the letter is in the Answer
	LetterInTheAnswer = 0
	for currentLetter in Answer:
		#If the letter the user guessed is found in the answer,
		# set the underscore in the user's answer to that letter
		if letter == currentLetter:
			Guess[LetterInTheAnswer] = letter
		LetterInTheAnswer = LetterInTheAnswer + 1
	# Display what the player has thus far (L) with a space
	# separating each letter
	print (' '.join(str(n) for n in Guess))

	if letter not in Answer:
		play -= 1
		print ("Bad Guess!!")
		print ("You have", + play, "more guesses")
	# Test to see if the word has been successfully completed,
	# and if so, end the loop
	if play == 0:
		print ("You lose")
	elif Answer == Guess:
		print ("You win...Great job")
		break
#print ("GREAT JOB")