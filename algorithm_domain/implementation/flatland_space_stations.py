#!/usr/bin/python



'''
Recursive attempt

def distance_to_nearest_station(c, n, stations, memo):
    if c < 0 or c >= n:
        return float('inf')
    if c in stations:
        return 0
    if c-1 in stations or c+1 in stations:
        return 1
    
    if c not in memo:
        memo[c] = min(
            1+distance_to_nearest_station(c-1, n, stations, memo),
            1+distance_to_nearest_station(c+1, n, stations, memo)
        )
    return memo[c]

def main():
    n, m = map(int, raw_input().split())
    stations = set(map(int, raw_input().split()))
    distances = []
    memo = {}
    
    for i in xrange(n):
        distances.append(distance_to_nearest_station(i, n, stations, memo))
    print max(distances)

if __name__ == '__main__':
    main()
'''
