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
	{"name": "DOTTED QUARTER", "value": 1.5},
]

def generate_right():
	i = 0
	while (i < 4):
		a = randint(0, 11)
		print(NOTES[a], end=" ") 
		
		#rhythm shit, must total 4 quarters 
		if (i == 3.75):
			rhythm = RHYTHMS[0]
		elif (i >= 3.25):
			rhythm = RHYTHMS[randint(0, 1)]
		elif (i > 2.5):
			rhythm = RHYTHMS[randint(0,2)]
		else:
			rhythm = random.choice(RHYTHMS)
		print(rhythm["name"])
		i += rhythm["value"]
		
def generate_left():
	#left hand will not have 16th notes
	i = 0
	while (i < 4):
		a = randint(0, 11)
		print(NOTES[a], end=" ") 
		
		#rhythm shit, must total 4 quarters 
		if (i == 3.5):
			rhythm = RHYTHMS[1]
		elif (i > 2.5):
			rhythm = RHYTHMS[randint(1,2)]
		else:
			rhythm = RHYTHMS[randint(1,3)]
		print(rhythm["name"])
		i += rhythm["value"]
		
def generate_bar():
	print()
	print("Right Hand:")
	generate_right()

	print()
	print("Left Hand:")
	generate_left()
	
def generate_eight():
	print()
	
	print("Right Hand:")
	for i in range(8):
		a = randint(0,11)
		print(NOTES[a], end=" ")
		rhythm = random.choice(RHYTHMS)
		print(rhythm["name"])
		
	print()
	
	print("Left Hand:")
	for i in range(8):
		a = randint(0,11)
		print(NOTES[a], end=" ")
		rhythm = RHYTHMS[randint(1,3)]
		print(rhythm["name"])

if input("1: Begin \n") == '1':
	while True:
		print()
		x = input("1: Generate 1 Bar \n2: Generate 8 Notes \n")
		if (x == '1'):
			generate_bar()
		elif (x == '2'):
			generate_eight()
		else:
			print("Invalid Option")
			print("Exiting Program")
			sys.exit(0)
else:
	sys.exit(0)
		
