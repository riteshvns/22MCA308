class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = lb = 0
        for i in range(len(nums)-2):
            if nums[i] == 0: continue
            lb = i + 2
            for j in range(i+1, len(nums)-1):
                lb = bisect_left(nums, nums[i]+nums[j], lb+(lb==j))
                count += lb - j - 1
        
        return count