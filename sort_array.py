# Given an array of integers nums, sort the array in ascending order without using the built-in function and return it.
class Solution(object):
    def bubbleSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n):
            for j in range(i,n):
                if nums[i]>nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
        return nums  
    def mergeSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n>1:        
            left_arr = nums[:(n//2)]
            right_arr = nums[(n//2):]
            
            self.mergeSortArray(left_arr)
            self.mergeSortArray(right_arr)
            i,j,k = 0,0,0
            while i<len(left_arr) and j<len(right_arr):
                if left_arr[i] <= right_arr[j]:
                    nums[k] = left_arr[i]
                    i+=1
                else:
                    nums[k] = right_arr[j]
                    j+=1
                k+=1
            while i<len(left_arr):
                nums[k] = left_arr[i]
                i+=1
                k+=1
            while j<len(right_arr):
                nums[k] = right_arr[j]
                j+=1
                k+=1
        return nums 
