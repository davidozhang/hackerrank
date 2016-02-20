#!/usr/bin/python

def main():
    fine = 0
    ac_day, ac_month, ac_year = map(int, raw_input().split())
    ex_day, ex_month, ex_year = map(int, raw_input().split())
    
    if ac_year > ex_year:
        fine += 10000
    if ac_year == ex_year and ac_month > ex_month:
        fine += 500 * (ac_month-ex_month)
    if ac_year == ex_year and ac_month == ex_month and ac_day > ex_day:
        fine += 15 * (ac_day-ex_day)
    print fine
    
if __name__ == '__main__':
    main()
