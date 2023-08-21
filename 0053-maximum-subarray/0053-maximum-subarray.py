class Solution(object):
    def maxSubArray(self, nums):
        leng = len(nums)
        sum = 0
        big = 0
        count = 0
        minNum = -1000000000
        
        for i in nums:
            if i < 0:
                count += 1
                if minNum < i:
                    minNum = max(minNum, i)
        
        if leng == 1:
            return nums[0]
        elif leng == count:
            # 전부 음수일 때
            return minNum
        else:
            for i in nums:
                sum += i
                if sum < 0:
                    sum = 0
                else:
                    if sum > big:
                        big = sum
            return big
        
        """
        :type nums: List[int]
        :rtype: int
        """
        