#!/usr/bin/python

def get_count(l, a, s, t):
    result = 0
    for d in l:
        if a + d >= s and a + d <= t:
            result += 1
    return result

def main():
    s, t = map(int, raw_input().split())
    a, b = map(int, raw_input().split())
    m, n = map(int, raw_input().split())
    apple_dists = map(int, raw_input().split())
    orange_dists = map(int, raw_input().split())
    
    print(get_count(apple_dists, a, s, t))
    print(get_count(orange_dists, b, s, t))
        
if __name__ == '__main__':
    main()
