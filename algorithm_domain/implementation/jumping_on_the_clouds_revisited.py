#!/usr/bin/python

def main():
    n, k = map(int, raw_input().split())
    c = map(int, raw_input().split())
    energy = 100
    i = 0
    game_end = False
    while not game_end:
        i = (i+k) % n
        if c[i] == 1:
            energy -= 2
        if i == 0:
            game_end = True
        energy -= 1
    print energy
    
if __name__ == '__main__':
    main()
