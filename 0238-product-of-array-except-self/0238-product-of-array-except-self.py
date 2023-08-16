class Solution(object):
    def productExceptSelf(self, nums):
        leng = len(nums)
        answer = [0] * leng
        mul = 1
        count = 0 # 0의 개수
        index = 0
        
        for i in nums:
            if i==0:
                count += 1
                index = nums.index(i)
                print(index)
            else:
                mul *= i
        
        if count == 0:
            for i in range(0,leng):
                answer[i] = mul / nums[i]
            return answer
        elif count == 1:
            # 그 인덱스만 빼고 다 곱한 값 넣기
            answer[index] = mul
            return answer
        else:
            #answer을 0으로 초기화하기
            # answer = {0}
            return answer
            
    
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        