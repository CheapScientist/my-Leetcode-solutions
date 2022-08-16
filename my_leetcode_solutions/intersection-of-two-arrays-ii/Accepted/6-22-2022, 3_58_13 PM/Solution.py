// https://leetcode.com/problems/intersection-of-two-arrays-ii

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2): 
            nums2, nums1 = nums1, nums2
        memo = {}
        for num in nums1: 
            memo[num] = memo.get(num, 0) + 1
        ans = []
        for num in nums2: 
            if num in memo and memo[num]: 
                ans.append(num)
                memo[num] -= 1
        return ans