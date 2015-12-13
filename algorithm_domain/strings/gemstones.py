#!/usr/bin/python

def main():
    _sets = []
    for _ in xrange(input()):
        _sets.append(set(list(raw_input())))
    print len(set.intersection(*_sets))
        
if __name__ == '__main__':
    main()
