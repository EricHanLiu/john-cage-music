import math
import sys
from random import randint
import random

NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
#base value is 1 for quarter in terms of counting
RHYTHMS = [
	{"name": "SIXTEENTH", "value": 0.25},
	{"name": "EIGHTH", "value": 0.5},
	{"name": "QUARTER", "value": 1},
]

def generate_bar():
	print
	i = 0
	while (i < 4):
		a = randint(0, 11)
		print NOTES[a], 
		#rhythm shit
		if (i > 3):
			rhythm = RHYTHMS[0]
		else:
			rhythm = random.choice(RHYTHMS)
		print rhythm["name"]
		i += rhythm["value"]
	
def generate_eight():
	print
	for i in range(8):
		a = randint(0,11)
		print NOTES[a],
		#random rhythm doesn't need to fit in a 4/4
		rhythm = random.choice(RHYTHMS)
		print rhythm["name"]

if input("1: Begin \n"):
	while True:
		print
		x = input("1: Generate 1 Bar \n2: Generate 8 Notes \n")
		if (x == 1):
			generate_bar()
		elif (x == 2):
			generate_eight()
		else:
			print "Invalid Option"
			print "Exiting Program"
			sys.exit(0)
else:
	sys.exit(0)
		