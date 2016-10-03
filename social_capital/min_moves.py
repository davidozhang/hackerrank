# Complete the function below.

def left_one(avg, index, count):
    result = 0
    for j, k in zip(index, [i for i in xrange(count)]):
        result += k-j
    return abs(result)

def right_one(avg, index, count, _len):
    result = 0
    count = 0
    for j, k in zip(index, [_len-1-i for i in xrange(count)]):
        result += j-k
    return abs(result)

def minMoves(avg):
    index = []
    count = 0
    for i in xrange(len(avg)):
        if avg[i] == 1:
            index.append(i)
            count += 1
    return max(left_one(avg, index, count), right_one(avg, index, count, len(avg)))
