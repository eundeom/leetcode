class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height)-1
        maxArea = 0
        
        while (left < right):
            maxArea = max(maxArea, (right-left)*min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                          
        return maxArea
        
        """
        :type height: List[int]
        :rtype: int
        """
        