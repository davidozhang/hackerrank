class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        n = int(A)
        binary = str(bin(n))[2:]
        return 1 if len(binary) > 1 and binary.count('1') == 1 else 0
