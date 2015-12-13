#!/usr/bin/python

def capitalize_first_letter(s):
    return s[0].upper() + s[1:] if s!='' else s

def main():
    words = map(capitalize_first_letter, raw_input().split(' '))
    print ' '.join(words)

if __name__ == '__main__':
    main()