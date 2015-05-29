import random
from init import *
import os

def check_word(word, player):
	flag = 0
	for i in wordlist:
		if i==word:
			if len(word)>3:
				print 'A word greater than three letters !'
				print 'Player', player+1, 'loses the game.'
				exit(0)
			else:
				print 'Player', player+1,'wins the game.'
				exit(0)
		elif i[:len(word)] == word:
			flag = 1
	if flag==1:
		return
	else:
		print 'No word can be formed with this set !'
		print 'Player', player+1, 'loses the game.'
		exit(1)

def input_letter():
	while 1:
		letter = raw_input('Enter letter : ')
		if len(letter)>1:
			print 'You cannot enter a word, enter a letter.'
		else:
			break

	return letter

def ghost():
	word = ''
	print '\n\n\t\tWelcome to Ghost\t\t\n\n'
	print 'The Rules of this game are simple : '
	print '\nThis is a two player game and for any player, there are two ways to lose this game :'
	print '1. Forming a word longer than 3 letters ("PEA" is ok, but "PEAR" is not)'
	print '2. Creating a fragment (of any size) which cannot become a word by adding more letters (forexample, "QZ")'
	print '\nWinning Ghost is simply not losing!\n\n'
	while(1):
		for player in range(0,2):
			print 'Player', player+1, ': '
			letter = input_letter()
			word = word + letter
			print 'New word :',word
			if check_word(word, player) == True:
				continue
			else:
				'Game aborted !'

if __name__ == '__main__':
	wordlist = load_words()
	os.system('clear')
	ghost()
