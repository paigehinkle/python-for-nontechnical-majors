#!/usr/bin/python3
import random
from time import sleep

def getDirection():
	v = random.random()
	mu = .6
	
	if v< mu:
		return -1
	elif v > (1-mu):
		return 1
	else:
		return 0

def printCharacter():
	print("$", end="")

def printManyCharacters(n):
	for i in range(n):
		printCharacter()
	print()

length = 20
while(length > 0):
	printManyCharacters(length)
	length += getDirection()

	length = min(length, 20)
	sleep(0.02)
