class Solution(object):
    def twoSum(self, nums, target):
        length = len(nums)
        ans = []
        for i in range(0, length):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    ans = [i, j]
                    return ans
