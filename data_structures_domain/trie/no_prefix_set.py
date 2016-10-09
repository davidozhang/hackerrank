#!/usr/bin/python
import sys

END = 'END'

def add_word_to_trie(word, root):
    current = root
    for letter in word:
        if END in current:
            bad_set(word)
        if letter not in current:
            current[letter] = {}
        current = current[letter]
    if len(current.keys()) > 0:
        bad_set(word)
    current[END] = END
    return True

def bad_set(word):
    print 'BAD SET'
    print word
    sys.exit(0)

def main():
    trie = {}
    s = set()
    for _ in xrange(input()):
        word = raw_input()
        if word in s:
            bad_set(word)
        s.add(word)
        add = add_word_to_trie(word, trie)
        if not add:
            bad_set(word)
    print 'GOOD SET'
    

if __name__ == '__main__':
    main()
