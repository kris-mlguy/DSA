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
    def maxSubArraySlidingWindow(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        curr_sum = max_sum = nums[0]
        for i in range(1,n):
            if curr_sum<0 and curr_sum<nums[i]:
                curr_sum = nums[i]
            else:
                curr_sum+=nums[i]
            max_sum = max(max_sum,curr_sum)
        return max_sum

def main():
    obj = Solution()
    print(obj.maxSubArrayBruteForce([-2,1,-3,4,-1,2,1,-5,4]))
    print(obj.maxSubArraySlidingWindow([-2,1,-3,4,-1,2,1,-5,4]))
  
if __name__ == '__main__':
    main()
