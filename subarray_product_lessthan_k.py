# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        l = 0
        current_product = 1
        result = 0
        for r in range(n):
            current_product*=nums[r]
            while l<=r and current_product>=k:
                current_product = current_product//nums[l]
                l+=1
            result+=(r-l+1)
        return result    
