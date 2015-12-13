#!/usr/bin/python

def main():
    result = ''
    for i in raw_input():
        result += i.lower() if i.isupper() else i.upper()
    print result

if __name__ == '__main__':
    main()
