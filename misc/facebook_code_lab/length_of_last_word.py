class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        arr = A.split()
        if len(arr) == 0:
            return 0
        return len(arr[-1])
