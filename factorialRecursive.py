#!/usr/bin/python3

def factorial(n):
	if n <= 1:
		return 1
	else:
		return n * factorial(n - 1)

for i in range (5):
	print(factorial(i))
