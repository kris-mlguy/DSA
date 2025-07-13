# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
class Solution(object):
    def rotateArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k%=n
        return nums[n-k:]+nums[:n-k]
    def rotateInPlace(self, nums, k):
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
def main():
    obj = Solution()
    print(obj.rotateArray([1,2,3,4,5,6],2))
    print(obj.rotateInPlace([1,2,3,4,5,6],2))
  
if __name__ == '__main__':
    main()
