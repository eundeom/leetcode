class Solution(object):
    def hammingWeight(self, n):
        total = 0
        stringNums = str(format(n,"b"))
        print(stringNums)
        
        for i in stringNums:
            if i == '1':
                total += 1
        
        return total
        
        """
        :type n: int
        :rtype: int
        """
        