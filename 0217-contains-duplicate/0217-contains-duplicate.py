class Solution(object):
    def containsDuplicate(self, nums):
        # set(집합)은 중복을 허용하지 않는다.
        # set과 array의 길이가 다르면 중복이 있다는 뜻 (True)
        
        num_set = set(nums)
        
        if len(num_set) != len(nums):
            return True
        else:
            return False