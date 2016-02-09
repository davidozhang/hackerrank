#!/usr/bin/python

def reverse(word):
	if word=='':
		return word
	else:
		return reverse(word[1:])+word[0]

def main():
	input = raw_input(': ')
	print reverse(input)

if __name__=='__main__':
	main()