from collections import Counter
def main():
    s1 = Counter(raw_input())
    s2 = Counter(raw_input())
    count = 0

    for i in range(97, 123):
        count += abs(s1.get(chr(i), 0) - s2.get(chr(i), 0))
    print count

if __name__ == '__main__':
    main()
