#!/usr/bin/python

def main():
    _dict = {}
    words = list(raw_input().lower())
    for i in words:
        if i == ' ':
            continue
        elif i not in _dict:
           _dict[i] = 1
    print 'pangram' if len(_dict.keys()) == 26 else 'not pangram'
                
    
if __name__ == '__main__':
    main()
