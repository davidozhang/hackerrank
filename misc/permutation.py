#!/usr/bin/python

def permute(prefix, str):
	if len(str)==0:
		print prefix
	else:
		 for i in range(0,len(str)):
		 	permute(prefix+str[i], str[0:i]+str[i+1:])

def main():
	input = raw_input('Input: ')
	print permute('', input)

if __name__=="__main__":
	main()
