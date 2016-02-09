#!/usr/bin/python

def mastermind(solution, guess):
	result = {'red': 0, 'white': 0}
	stack = []
	counter=0
	for i in solution:
		stack.append(i)

	for j in guess:
		if j in stack:
			if guess.index(j, counter)==stack.index(j):
				result['red']+=1
			else:
				result['white']+=1
			stack[stack.index(j)]=''
		counter+=1
	return result

def main():
	solution = raw_input('Solution: ')
	guess = raw_input('Guess: ')
	print mastermind(solution, guess)

if __name__=='__main__':
	main()