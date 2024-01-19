class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums.sort()
        # for i,x in enumerate(nums):
        #     if i != x:
        #         return i
        # return len(nums)
        n=sum(nums)
        m=sum(range(0,len(nums)+1))
        return m-n