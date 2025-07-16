# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
class Solution(object):
    def subarraySumHashmapSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        counts = {0:1}
        current_sum = 0
        res = 0
        for i in range(n):
            current_sum += nums[i]
            if current_sum - k in counts:
                res+=counts[current_sum-k]
            if current_sum in counts:
                counts[current_sum]+=1
            else:
                counts[current_sum] = 1
        return res
