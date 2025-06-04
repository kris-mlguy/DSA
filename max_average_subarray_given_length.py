# Given an integer array nums consisting of n elements, and an integer k,
# find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        max_avg = float(sum(nums[:k])) / k
        for i in range(n-k+1):
            curr_avg = float(sum(nums[i:i+k])) / k
            max_avg = max(max_avg,curr_avg)
        return max_avg
