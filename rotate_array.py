# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
class Solution(object):
    def rotateInPlaceAlgorithm(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k%=n
        def reverse(arr,start,end):
            while start<end:
                arr[start],arr[end] = arr[end],arr[start]
                start+=1
                end-=1
        reverse(nums,0,n-k-1)
        reverse(nums,n-k,n-1)
        reverse(nums,0,n-1)
