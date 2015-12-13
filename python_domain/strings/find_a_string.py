#!/usr/bin/python

def main():
    _str, _substr, result = raw_input(), raw_input(), 0
    for i in xrange(len(_str)):
        result += 1 if _str[i: i+len(_substr)] == _substr else 0
    print result

if __name__ == '__main__':
    main()

