class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        return str(bin(A))[2:].count('1')
