class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1=set(nums1)
        s2=set(nums2)
        a=[]
        for i in s1:
            if i in s2:
                a.append(i)
        return a