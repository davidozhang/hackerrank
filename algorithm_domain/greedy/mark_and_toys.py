# Enter your code here. Read input from STDIN. Print output to STDOUT
def max_toys(prices, dollars):
  #Compute and return final answer over here
  _sum, _amount = 0, 0
  for i in sorted(prices):
    if _sum + i > dollars:
        break
    _sum += i
    _amount += 1
  print _amount
        

if __name__ == '__main__':
  n, k = map(int, raw_input().split())
  prices = map(int, raw_input().split())
  max_toys(prices, k)
