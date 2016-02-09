# Complete the function below.

def isPalindrome(s):
    return s==s[::-1]

def shortPalin(s):
    if isPalindrome(s):
        return 0
    else:
        temp = s
        largest_common = 0
        common = 0
        while (len(temp) > 0):
            for i in zip(list(temp), list(s[::-1])):
                if i[0] == i[1]:
                    common += 1
            if common > largest_common:
                largest_common = common
            common = 0
            temp = temp[1:]
        return len(s) - largest_common
        
