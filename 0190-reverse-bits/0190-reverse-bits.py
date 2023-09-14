class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # int to binary
        num = '{0:032b}'.format(n)
        
        # reverse
        revNum = num[::-1]
        
        # binary to int
        return int(revNum, 2)
        