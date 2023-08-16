<h3>Note</h3>
<hr>
<p><strong class="example">Time Limit Exceeded :</strong></p>
<pre>class Solution(object):
    def containsDuplicate(self, nums):
        left, right = 0, 1
        leng = len(nums)
        
        while left < leng:
            if right == leng:
                    left += 1
                    right = left + 1
            else:
                if nums[left] != nums[right]:
                    right += 1

                else:
                    return True
        return False
</pre>
<p><strong class="example">Note :</strong></p>
<p>* <strong>set</strong>(집합)을 사용함 - <i>중복</i> 없음!<br> set의 length와 기존 array의 length 비교 ⇢ 다르면 중복 / 같으면 중복 x</p>​
