class Solution:
    def sortColors(self, nums: List[int]) -> None:
        prefix = Counter(nums)

        for i in range(prefix[0]): nums[i] = 0

        prefix[1] += prefix[0]

        for i in range(prefix[0], prefix[1]): nums[i] = 1

        prefix[2] += prefix[1]

        for i in range(prefix[1], prefix[2]): nums[i] = 2
        