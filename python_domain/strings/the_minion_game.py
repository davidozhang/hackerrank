#!/usr/bin/python
VOWELS = set(['A', 'E', 'I', 'O', 'U'])

def main():
    cons_indices, vowel_indices, cons_count, vowel_count = [], [], 0, 0
    word = raw_input()
    length = len(word)
    for i in xrange(length):
        cons_indices.append(i) if word[i] not in VOWELS else vowel_indices.append(i)
    for j in cons_indices:
        cons_count += length - j
    for k in vowel_indices:
        vowel_count += length - k
    if cons_count > vowel_count:
        print 'Stuart ' + str(cons_count)
    elif cons_count < vowel_count:
        print 'Kevin ' + str(vowel_count)
    else:
        print 'Draw'

if __name__ == '__main__':
    main()
