# Given an integer array nums, find the subarray with the largest sum, and return its sum.
class Solution(object):
    def maxSubArrayBruteForce(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_sum = float('-inf')
        for i in range(n):
            curr_sum = 0
            for j in range(i,n):
                curr_sum += nums[j]
                max_sum = max(max_sum, curr_sum)
        return max_sum
