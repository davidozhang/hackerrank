# Complete the function below.
import math

def divisors(n):
    divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                divisors.append(n / i)
    for divisor in divisors:
        yield divisor

def odd_divisors_sum(n):
    return sum([i for i in divisors(n) if i%2 != 0])

def count(numbers):
    result = 0
    for i in numbers:
        result += odd_divisors_sum(i)
    return result
