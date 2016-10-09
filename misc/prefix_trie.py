#!/usr/bin/python

def make_trie(*words):
	root = {}
	end = '_end'
	for word in words:
		current = root
		for letter in word:
			if letter not in current:
				current[letter] = {}
			current = current[letter]
		current[end] = end
	return root

def in_trie(word, trie):
	current = trie
	end = '_end'
	for letter in word:
		if letter not in current:
			return False
		current = current[letter]
	if end in current:
		return True
	else:
		return False


def main():
	trie = make_trie('foo', 'bar', 'baz', 'barzz')
	print in_trie('foo', trie)
	print in_trie('barz', trie)
	print in_trie('abc', trie)
	print in_trie('bart', trie)
	print in_trie('ba', trie)
	print in_trie('barzz', trie)

if __name__ == '__main__':
	main()