#!/usr/bin/python3

def printCharacter():
	print("$", end="")

def printManyCharacters(n):
	for i in range(n):
		printCharacter()
	print()


printManyCharacters(10)
