class Solution(object):
    def countBits(self, n):
        cnt = list(range(0,n+1))
        
        for i in range(0,n+1):
            cnt[i] = format(i,"b").count("1")
        
            
        return cnt
        """
        :type n: int
        :rtype: List[int]
        """
        #2진 표현에서 1의 개수를 세어 array에 담기