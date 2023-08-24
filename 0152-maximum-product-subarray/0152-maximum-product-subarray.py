class Solution(object):
    def maxProduct(self, nums):
        res = minNum = maxNum = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            minNum, maxNum =  min(num, min(minNum * num, maxNum * num)), max(num, max(minNum * num, maxNum * num))
            res = max(res, max(minNum, maxNum))
        return res