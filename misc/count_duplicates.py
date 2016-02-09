# Complete the function below.
from itertools import groupby

def countDuplicates(numbers):
    result = 0
    for i, j in groupby(sorted(numbers)):
        if len(list(j)) >= 2:
            result += 1
    return result
