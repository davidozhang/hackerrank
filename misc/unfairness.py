# Complete the function below.


def minUnfairness(k, arr):
    _min = None
    sorted_arr = sorted(arr)
    for i in xrange(len(sorted_arr)-k):
        val = max(sorted_arr[i:i+k]) - min(sorted_arr[i:i+k])
        if val < _min or not _min:
            _min = val
    return _min
