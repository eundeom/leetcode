class Solution(object):
    def missingNumber(self, nums):
        length = len(nums) + 1
        arr = [0] * length
        
        for i in range(0,length):
            if i in nums:
                arr[i] = 1
            
        for i in range(0,length):
            if arr[i] == 0:
                return i
            
        """
        :type nums: List[int]
        :rtype: int
        """
        # len 만큼 배열안에 숫자가 다 있는지 check 
        
        # list 0으로 된 거 만들고 숫자가 있으면 index의 값을 1로 변경 
        # for문 돌려서 0이 있는지 확인 - 출력.